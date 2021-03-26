import numpy as np
import os
import time
import cv2
import math

import pickle
import torch
from collections import Counter

import torch.nn as nn
import torch.nn.functional as F
import torchvision.models

alexnet = torchvision.models.alexnet(pretrained=True)

model_buildings = pickle.load(open('./NS model data/IsolationForest_buildings.h5', 'rb'))
model_forest = pickle.load(open('./NS model data/IsolationForest_forest.h5', 'rb'))
model_glacier = pickle.load(open('./NS model data/IsolationForest_glacier.h5', 'rb'))
model_mountain = pickle.load(open('./NS model data/IsolationForest_mountain.h5', 'rb'))
model_sea = pickle.load(open('./NS model data/IsolationForest_sea.h5', 'rb'))
model_street = pickle.load(open('./NS model data/IsolationForest_street.h5', 'rb'))

base_llist_buildings = torch.load('./NS model data/base_list_buildings.pt')
base_llist_forest= torch.load('./NS model data/base_list_forest.pt')
base_llist_glacier= torch.load('./NS model data/base_list_glacier.pt')
base_llist_mountain= torch.load('./NS model data/base_list_mountain.pt')
base_llist_sea = torch.load('./NS model data/base_list_sea.pt')
base_llist_street = torch.load('./NS model data/base_list_street.pt')

model_list = [model_buildings,model_forest,model_glacier,model_mountain,model_sea,model_street]
base_list_list = [base_llist_buildings,base_llist_forest,base_llist_glacier,base_llist_mountain,base_llist_sea,base_llist_street]


class CNN_AlexNet(nn.Module):

    def __init__(self):
        self.name = "CNN_AlexNet"
        super(CNN_AlexNet, self).__init__()
        self.conv1 = nn.Conv2d(256, 60, 2)  # in_channels, out_chanels, kernel_size
        self.conv2 = nn.Conv2d(60, 10, 2)  # in_channels, out_chanels, kernel_size

        self.fc1 = nn.Linear(160, 32)
        # self.fc2 = nn.Linear(32, 6)
        self.fc2 = nn.Linear(32, 7)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(-1, 160)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# device = torch.device("cpu")

model_final = CNN_AlexNet()
load_path = './NS model data/model_CNN_AlexNet_bs32_lr0.001_epoch5_other.pt'
model_final.load_state_dict(torch.load(load_path,map_location='cpu'))

"""
Info Processing: Processe output from the reformat_ouput function, find secs with potential
"""
def fill_up_empty_spaces(start_frame_id, end_frame_id,input_map):
  # print("Fill up frames, ",start_frame_id, end_frame_id)
  i = start_frame_id
  while i<=end_frame_id:
    # print("Filling ",i)
    input_map[i] = {'biggest_area':0,'potential': True}
    i+=1;
  return input_map

def fill_up_empty_sec (start_sec, end_sec,input_map):
  # print("Fill up secs , ",start_sec, end_sec)
  i = start_sec
  while i<=end_sec:
    input_map[i] = {}
    i+=1;
  return input_map

def cal_potential (in_area,video_dimension,compare_rate):
   ns_potential = False
   if in_area < (video_dimension * compare_rate):
     ns_potential = True
   return ns_potential


def get_final_potential_list(detail_dict, frame_count, frames_per_second,video_duration):
    # Distill info for each sec
    # video_duration = math.floor(frame_count / frames_per_second)
    sec_potential_list = []
    for sec, data in detail_dict.items():
        # print("Sec = ",sec)
        if ('frames' in data.keys()):
            frames = data['frames']
            len_detected = len(frames.keys())
            potential_count = 0
            for frame_id, datas in frames.items():
                if datas['potential'] == True:
                    potential_count += 1
            potential_count = (frames_per_second - len_detected) + potential_count
        else:
            potential_count = frames_per_second

        # print("potential_count =  ",potential_count)
        final_potential = False;
        if potential_count == frames_per_second:
            final_potential = True
        sec_potential_list.append(final_potential)

    # Fill up last secs
    temp_len = len(sec_potential_list)
    sec_potential_list[temp_len:video_duration] = [True] * (video_duration - temp_len)

    return sec_potential_list


def get_sec_potential_ns(video_dimension, compare_rate, in_collection,frame_count, frames_per_second,video_duration):
    format_area_frame = {}

    for eachFrame in in_collection:
        sec = eachFrame['second']
        # Fill up epty secs: begin
        temp_secs = format_area_frame.keys()
        if len(temp_secs) == 0:
            last_sec = 0
        else:
            last_sec = max(temp_secs)
        if (sec != last_sec + 1) and (sec not in temp_secs):
            # print("Fill up sec = ", last_sec, sec)
            format_area_frame = fill_up_empty_sec(last_sec, sec - 1, format_area_frame)

        # New second
        if sec not in format_area_frame.keys():
            format_area_frame[sec] = {}
            print("New Sec ", sec)

        if 'frames' not in format_area_frame[sec].keys():
            # first time, new frame
            # print("New Frame ", eachFrame['frame']);
            ns_potential = cal_potential(eachFrame['area'],video_dimension, compare_rate)
            if eachFrame['frame'] != 0:
                # fill up empty frames: beginning
                temp_map = {}
                format_area_frame[sec]['frames'] = fill_up_empty_spaces(0, eachFrame['frame'] - 1, temp_map)
                format_area_frame[sec]['frames'][eachFrame['frame']] = {'biggest_area': eachFrame['area'],
                                                                        'potential': ns_potential}
            else:
                format_area_frame[sec]['frames'] = {
                    eachFrame['frame']: {'biggest_area': eachFrame['area'], 'potential': ns_potential}}
        else:
            # has frame info stored
            # get last frame
            temp_keys = format_area_frame[sec]['frames'].keys()
            last_frame = max(temp_keys)
            # if frame alraedy exists (case: multi objects per frame)
            if eachFrame['frame'] == last_frame:
                # print('Frame Already Exist')
                prev_biggest = format_area_frame[sec]['frames'][last_frame]['biggest_area']
                now_biggest = max(prev_biggest, eachFrame['area'])
                new_potential = cal_potential(now_biggest,video_dimension, compare_rate)
                # print([prev_biggest, now_biggest])
                format_area_frame[sec]['frames'][last_frame]['biggest_area'] = now_biggest
                format_area_frame[sec]['frames'][last_frame]['potential'] = new_potential

            # fill up empty frames
            elif eachFrame['frame'] != last_frame + 1:
                # print("Noot Connected, ", eachFrame['frame'], last_frame)
                format_area_frame[sec]['frames'] = fill_up_empty_spaces(last_frame + 1, eachFrame['frame'] - 1,
                                                                        format_area_frame[sec]['frames'])
            else:
                # new frame
                ns_potential = cal_potential(eachFrame['area'],video_dimension, compare_rate)
                format_area_frame[sec]['frames'][eachFrame['frame']] = {'biggest_area': eachFrame['area'],
                                                                        'potential': ns_potential}

    final_list = get_final_potential_list(format_area_frame, frame_count, frames_per_second,video_duration)

    return final_list

"""
Core part of Nature Scene detection algorithm
"""

class_list = ['buildings','forest','glacier','mountain','sea','street']
train_class = ['buildings', 'forest', 'glacier', 'mountain', 'others', 'sea', 'street']


def quantify_image(image,bins=(3, 3, 3)):
  # compute a 3D color histogram over the image and normalize it
  hist = cv2.calcHist([image], [0, 1, 2], None, bins,[0, 256, 0, 256, 0, 256])
  hist = cv2.normalize(hist, hist).flatten()
  # return the histogram
  return hist


def get_data_features_frame(frame):
    image = cv2.resize(frame, (224, 224))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    features = quantify_image(image)

    return features

#decision_function returns values in the range of [-0.5, 0.5] where -.5 is the most anomalous
def get_most_possible_cat(nov_detect_result):
  max_ano = -1
  class_index = -1
  for i, each in enumerate(nov_detect_result):
    if each[0] == 1: #found
      if (each[1] > max_ano):
        max_ano = each[1]
        class_index = i

  if max_ano<-0.003:
    max_ano = -1
    class_index = -1

  return max_ano,class_index

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


def novelty_detection(frame):
    match_index = [-1] * 6
    for index, eachModel in enumerate(model_list):

        frame_features = get_data_features_frame(frame)
        temp_list = base_list_list[index] + frame_features
        test_model = eachModel
        preds = test_model.predict(temp_list)
        anomaly_score = test_model.decision_function([frame_features])
        # print("Index = ",index)
        if (preds[-1] == 1):  # inliner
            match_index[index] = [1, anomaly_score]
        else:
            match_index[index] = [-1, -10]

    return match_index


def NS_detection(num_ns_sec, per_video_info, potential_list):
    n = 0
    processed_frame = 0
    curretn_sec = 0;
    per_sec_list = [];
    frame_record_list = [];  # num_ns_sec: number of selected frame per sec that will be used for ns detection. Goal: improve speed
    all_sec_list = [];
    frames_per_second = per_video_info['frames_per_second']
    video_duration = per_video_info['video_duration']
    video_streams = per_video_info['video_streams']

    # video_duration = frame_count / frames_per_second

    while (1):
        ret, current_frame = video_streams.read()
        if ret == True:
            skip = False
            if (potential_list[curretn_sec] == False):  # skip this second
                # print("Skip sec {}, frame{}".format(curretn_sec, processed_frame))
                skip = True

            if (skip == False):
                if processed_frame % (math.floor(frames_per_second / num_ns_sec)) == 0:
                    frame_record_list.append(current_frame.copy())

                if processed_frame % (frames_per_second) == 0:
                    temp = cv2.resize(current_frame, (224, 224))
                    # cv2.imshow(temp)

                match_index_list = novelty_detection(current_frame)
                # print('Novelty Detection Result:',match_index_list)
                max_ano, class_index = get_most_possible_cat(match_index_list)
                if max_ano != -1 and class_index != -1:
                    # print("Found! class_index = ",class_list[class_index])
                    per_sec_list.append(class_index)

            n += 1
            processed_frame += 1
            if (processed_frame == frames_per_second):  # A sec end
                print("One Sec End, Result ======= ", per_sec_list)
                curretn_sec += 1;
                if len(per_sec_list) > 0 and skip == False:  # detected something
                    most_possible_nov = most_frequent(per_sec_list)
                    print("Most possible nov = ", class_list[most_possible_nov])

                    # Run ns model
                    print("Start NS MODEL-------------------------")
                    per_frame_ns_result = []



                    average_confidence = 0
                    print('Len of frame to Process:', len(frame_record_list))





                    for eachFrame in frame_record_list:
                        frame_resized = cv2.resize(eachFrame, (224, 224))
                        # cv2_imshow(frame_resized)
                        # # print(frame_resized.shape)
                        frame_resized = torch.from_numpy(frame_resized)
                        batch_frame = np.transpose(torch.unsqueeze(frame_resized, 0), [0, 3, 1, 2])
                        batch_frame = batch_frame.float()
                        # prediction reuslt & confidence
                        frame_features = alexnet.features(batch_frame)
                        pred = model_final(frame_features)
                        prob = F.softmax(pred, dim=1)
                        confidence, pred_class = prob.topk(1, dim=1)
                        top_prob, top_label = prob.topk(2)



                        average_confidence = average_confidence + confidence.item()



                        print('Confidence = {}%'.format(confidence.item() * 100))
                        print('Prediction = ', pred_class.item())

                        # a very simple confidence filter
                        if (confidence.item() < 0.7):
                            per_frame_ns_result.append(-1)
                        else:
                            per_frame_ns_result.append(pred_class.item())

                    average_confidence = average_confidence / len(frame_record_list)

                    most_possible_ns = most_frequent(per_frame_ns_result)
                    print("Most possible ns = ", train_class[most_possible_ns])




                    if most_possible_ns == -1:  # corner case: all sec confidence <-1
                        all_sec_list.append([class_list[most_possible_nov], [-1, average_confidence]]);
                    else:
                        all_sec_list.append([class_list[most_possible_nov], [train_class[most_possible_ns], average_confidence]]);




                    if most_possible_ns != -1:
                        if (class_list[most_possible_nov] != train_class[most_possible_ns]):
                            print("Two Prediction result does not match!")
                else:
                    print("Detected Nothing")
                    all_sec_list.append([None, None])
                # change sec
                print("Len = ", len(per_sec_list))
                per_sec_list = []
                processed_frame = 0
                frame_record_list = []

            # print("curretn_sec = ", curretn_sec)
            # if (n == frame_count or curretn_sec == math.floor(video_duration)):
            if (curretn_sec == video_duration):
                break;
        else:
            print('Error: Cannot read frame, frame = {}'.format(n))
            break;

    return all_sec_list


# For each sec:
# case 1: estimator and CNN has same result: quality score = 1 * average confidence of cnn
# case 2: estimator and CNN has different result: estimator weight = 0.5, CNN weight = 0.5, quality score = 0.5 * average confidence of cnn
def process_ns_results(ns_all_sec_list, video_duration):
    result = {}  # {sec: [cnn result (category), quality score]}
    for index, eachSec in enumerate(ns_all_sec_list):
        quality_score = 0
        estimator_result = eachSec[0]
        cnn_result = eachSec[1]
        # print(estimator_result)
        # print(cnn_result)
        if estimator_result != None and cnn_result != None:
            if estimator_result == cnn_result[0]:
                quality_score = 1 * cnn_result[1]  # cnn_result[1]: average confidence
            else:
                quality_score = 0.5 * cnn_result[1]

            if cnn_result[0] == -1:
                result[index] = [estimator_result, quality_score]
            else:
                result[index] = [cnn_result[0], quality_score]

    result_map = {}
    # {cateory: times: [[seg1],[seg2]], "quality score"}
    for sec, data in result.items():
        if data[0] not in result_map.keys():  # the category does not exist in map
            result_map[data[0]] = {'timestamps': [[sec, sec]], 'quality_score': 1 * data[1], 'total_length': 1}
        else:
            time_list = result_map[data[0]]['timestamps']
            # total_time_length = 0
            # for each in time_list:
            #   total_time_length = total_time_length + (each[1]-each[0])

            time_last = result_map[data[0]]['timestamps'][-1]
            temp = result_map[data[0]]['quality_score'] / result_map[data[0]]['total_length'] + data[1]
            if time_last[1] <= sec - 2:  # difference is larger than 2 secs
                new_seg = [sec, sec]
                result_map[data[0]]['timestamps'].append(new_seg)
            else:
                result_map[data[0]]['timestamps'][-1][1] = sec

            result_map[data[0]]['total_length'] += 1
            result_map[data[0]]['quality_score'] = temp * result_map[data[0]]['total_length']
        print(result_map)

    return result_map

def ns_result_format(result_map):
  quality_score_result = []
  detection_result = []
  for category, data in result_map.items():
    quality_score_result.append({'keyword':category,'score':round(data['quality_score'],1)})
    for eachSeg in data['timestamps']:
      detection_result.append({'keyword':category,'start':eachSeg[0],'end':eachSeg[1]})
  return quality_score_result,detection_result




