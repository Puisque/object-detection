from imageai.Detection import VideoObjectDetection
import gc
gc.collect()

from MovieAPIFunctions import *
from ObjectDetectionFunctions import *
from InfoProcessingFunctions import *
from NatureSceneDetection import *
import Global

print("Main!");

"""
const variables 
"""
# fileName = 'tmdb_movies_metadata.csv' # can be found in the Code -> TMDB folder
fileName = 'tmdb_movies_metadata_after2010.csv'
# fileName = 'tmdb_movies_metadata_after2010_docum.csv'
# fileName = 'tmdb_movies_metadata_after2010_Mountain.csv'

header = ['genres','id','overview', 'poster_path','release_date', 'runtime', 'title',]#7 columns
genres = ['Comedy','Romance','Family','Drama','Documentary'] #for test&demo: use video in Romance, Family,Drama,Comedy, Documentary
COMPARE_RATE = 0.4
PER_SEC_FRAME_DENO = 10

"""
load dataset
Note: If a movie has more than one video, onnly keep the first one
"""
dataset_1 = read_dataset_csv(fileName,header);
print(dataset_1.shape)

#For test: use the first 200 videos
test_list = dataset_1.sample(n = 100,random_state =3).to_dict('index')
test_trailer_list = get_youtube_data(test_list,genres)

#For NS: use hardcoded id
# test_list = dataset_1.iloc[[20680]].to_dict('index')
# print(test_list)
# test_trailer_list = get_youtube_data(test_list,genres)

"""
Get video data from TMDB dataset including VideoCapture results
"""
num_videos=10 #the number of videos you want to process this time #changed already
length = 120 #max length , sec
movie_raw_data = get_video_data(num_videos,length,genres,test_trailer_list)
print('Found {} Videos'.format(len(movie_raw_data)))

#save the capctured video for future use
# save_videos(movie_raw_data)

"""
Object Detection Initialization
For now, use YOLOv3 as the detector
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
    #debugging process start
    print("Here started the information processing processes.")
    """
    Info Processing for Object Detection
    """
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
    """
    Info Processing for Nature Scene Detection
    """
    video_dimension = width * height
    video_duration = output_Collection_temp[-1][0]
    #Get a list of secs that can be used for ns detection
    ns_potential_list = get_sec_potential_ns(video_dimension, COMPARE_RATE, output_dic_reformated, frames_per_second, video_duration)
    print("ns_potential_list = ", ns_potential_list)

    per_video_info = {}
    per_video_info['frames_per_second'] = frames_per_second
    per_video_info['video_duration'] = video_duration
    per_video_info['video_streams'] = cv2.VideoCapture(video_data.url)
    all_sec_list = NS_detection(PER_SEC_FRAME_DENO, per_video_info, ns_potential_list)
    print("NS Detection Result: ", all_sec_list)
    result_map = process_ns_results(all_sec_list, per_video_info['video_duration'])
    ns_quality_score_result, ns_detection_result = ns_result_format(result_map)
    print(ns_quality_score_result)
    print(ns_detection_result)

    #============================================================
    v_index = str(i)
    print("v index for the following input: ",v_index)
    dict_to_schema(arr_for_json,value,url,v_index,ns_quality_score_result, ns_detection_result)

gc.collect()