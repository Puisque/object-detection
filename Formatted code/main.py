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
from InfoProcessingFunctions import *
from NatureSceneDetection import *

import Global

COMPARE_RATE = 0.5
PER_SEC_FRAME_DENO = 10
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
# test_list = dataset_1.sample(n = 2000).to_dict('index')
test_list = dataset_1.iloc[[17715]].to_dict('index')
print(test_list)
test_trailer_list = get_youtube_data(test_list,genres)


"""
Get video data from TMDB dataset including VideoCapture results
"""
num_videos= 1 #the number of videos you want to process this time #changed already
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
    video_path_out, elapsed_time,frames_per_second,frame_count,width,height  = detect_objects(detector,video_data = video_data,fileName = f_name,logProgress=logProgress)
    #Process the detection results
    output_Collection_temp = Global.output_Collection.copy()
    #====================Aisling, here is your part====================
    # debugging process start
    print("Here started the information processing processes.")
    # per_sec_object_info = choose_obj(output_Collection_temp)
    output_dic_reformated, reformat_frame_second = reformat_ouput(output_Collection_temp)
    """
    NS Detection
    """
    video_dimension = width * height
    compare_rate = COMPARE_RATE
    video_duration = output_Collection_temp[-1][0]
    final_list = get_sec_potential_ns(video_dimension, compare_rate, output_dic_reformated,frame_count,frames_per_second,video_duration)
    print("final_list = ",final_list)
    per_video_info = {}
    per_video_info['frames_per_second'] = frames_per_second
    per_video_info['video_duration'] = video_duration
    per_video_info['video_streams'] = cv2.VideoCapture(video_data.url)
    all_sec_list = NS_detection(PER_SEC_FRAME_DENO, per_video_info, final_list)
    print("NS Detection Result: ",all_sec_list)
    result_map = process_ns_results(all_sec_list, per_video_info['video_duration'])
    quality_score_result, detection_result = ns_result_format(result_map)
    print(quality_score_result)
    print(detection_result)

    # processed_array = object_occurrence_within_second_frame(output_dic_reformated)
    # final_dic_output = final_intent_reformat(processed_array)
    # updated_arry = final_intent_reformat_update(processed_array)
    # update_arr = quality_score_attempt_version2(updated_arry)

    #grouped_per_sec_object_info = final_result(per_sec_object_info)
    print("Ready to put organized info in json files.")
    # print(update_arr)
    #============================================================
    #v_index = str(i)
    #dict_to_schema(grouped_per_sec_object_info,value,url,v_index)

gc.collect()