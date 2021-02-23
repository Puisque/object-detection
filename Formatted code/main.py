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
num_videos=6 #the number of videos you want to process this time
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
    per_sec_object_info = choose_obj(output_Collection_temp)
    grouped_per_sec_object_info = final_result(per_sec_object_info)
    v_index = str(i)
    dict_to_schema(grouped_per_sec_object_info,value,url,v_index)

gc.collect()
