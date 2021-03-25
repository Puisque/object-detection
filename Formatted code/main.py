from imageai.Detection import VideoObjectDetection
import matplotlib as plt
import numpy as np
import os
import time
import cv2
import pafy
import gc
gc.collect()

from MovieAPIFunctions import *
from ObjectDetectionFunctions import *
# from InfoProcessingFunctions import *
# from infoUpdateProcessing import *
from finalQualityScore_infoProcessing import *
import Global

print("Main!");

"""
const variables 
"""
fileName = 'tmdb_movies_metadata.csv' # can be found in the Code -> TMDB folder
header = ['genres','id','overview', 'poster_path','release_date', 'runtime', 'title',]#7 columns
genres = ['Comedy','Romance','Family','Drama','Documentary'] #for test&demo: use video in Romance, Family,Drama,Comedy, Documentary


"""
load dataset
"""
dataset_1 = read_dataset_csv(fileName,header);
print(dataset_1.shape)

#For test: use the first 200 videos
test_list = dataset_1.sample(n = 200).to_dict('index')
test_trailer_list = get_youtube_data(test_list,genres)

"""
Get video data from TMDB dataset including VideoCapture results
"""
num_videos=1 #the number of videos you want to process this time #changed already
length = 100 #max length , sec
movie_raw_data = get_video_data(num_videos,length,genres,test_trailer_list)
print('Found {} Videos'.format(len(movie_raw_data)))

#save the capctured video for future use
# save_videos(movie_raw_data)

"""
---------------Object Detection Part---------------
Note:
1. If a movie has more than one video, onnly keep the first one
2. For now, use YOLOv3 as the detector 
"""
#Initialize detector
execution_path = os.getcwd()
model_path = os.path.join(execution_path , "yolo.h5")
print(model_path)
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel(detection_speed='fastest')

#Run detector
for i, (key, value) in enumerate(movie_raw_data.items()):
    eachVideo = value['Youtube Info'][0]
    #Get video
    video_data = eachVideo[2]
    url = eachVideo[1]
    #Start Object detection
    Global.init()
    f_name = eachVideo[0].replace(' ', '').replace('-','_')
    logProgress=False
    print('Processing Video: ',f_name)
    video_path_1,elapsed_time_1  = detect_objects(detector,video_data = video_data,fileName = f_name,logProgress=logProgress)
    #Process the detection results
    output_Collection_temp = Global.output_Collection.copy()
    #====================Aisling, here is your part====================
    #debugging process start
    print("Here started the information processing processes.")
    output_dic_reformated, reformat_frame_second = reformat_ouput(output_Collection_temp)
    processed_array = object_occurrence_within_second_frame(output_dic_reformated)
    final_dic_output = final_intent_reformat(processed_array)
    updated_arry = final_intent_reformat_update(processed_array)
    update_arr = quality_score_attempt_version2(updated_arry)
    update_accuracy_with_area = object_occurrence_within_second_frame_accuracy_avgArea_avgAcc(output_dic_reformated)
    final_dic_output_acc = final_intent_reformat_acc(update_accuracy_with_area)
    final_dic_output_area = final_intent_reformat_area(update_accuracy_with_area)
    acc_score_dic = quality_socre_acc(final_dic_output_acc)
    area_score_dic = quality_socre_area(final_dic_output_area)
    score_update_arr = final_quaility_score(area_score_dic, acc_score_dic, update_arr)
    arr_for_json = transformArrToJsonFileFormat(score_update_arr)

    # print("Here started the claire information processing processes.")
    # per_sec_object_info = choose_obj(output_Collection_temp)
    # grouped_per_sec_object_info = final_result(per_sec_object_info)
    #
    # print("Ready to put organized info in json files.")
    # print("grouped per second object info are as follows")
    # print(grouped_per_sec_object_info)
    # print("video value array that might need to be used:")
    # print(value)
    # print("url of the input:")
    # print(url)

    #============================================================
    v_index = str(i)
    print("v index for the following input: ")
    print(v_index)
    dict_to_schema(arr_for_json,value,url,v_index)

gc.collect()
