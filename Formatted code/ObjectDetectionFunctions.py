import Global
import os
import time
import cv2


def forSeconds(second_number, output_arrays, count_arrays, average_output_count):
    print("SECOND : ", second_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last second: ", average_output_count)
    Global.output_Collection.append((second_number,output_arrays,count_arrays,average_output_count))
    print("------------END OF A SECOND --------------")


def detect_objects(input_detector, video_data, fileName, logProgress=True):
    execution_path = os.getcwd()
    fileName = fileName+"_detected"
    file_path_out = os.path.join(execution_path,"OD Out Videos",fileName)

    video_streams = cv2.VideoCapture(video_data.url)

    frames_per_second = int(video_streams.get(cv2.CAP_PROP_FPS))
    print('frames_per_second = ', frames_per_second)
    frame_count = int(video_streams.get(cv2.CAP_PROP_FRAME_COUNT))
    width = video_streams.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video_streams.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # start: object detection
    start_time = time.time()
    video_path = input_detector.detectObjectsFromVideo(
        camera_input=video_streams,
        output_file_path=file_path_out,  # save output video
        frames_per_second=frames_per_second,
        per_second_function=forSeconds,
        log_progress=logProgress,
        minimum_percentage_probability=70)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Elapsed time = ',elapsed_time)

    return video_path, elapsed_time,frames_per_second,frame_count,width,height