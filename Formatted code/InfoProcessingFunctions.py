from collections import Counter
import json
import pandas as pd

def calc_area(box_point):
  x1,y1,x2,y2 = box_point
  area = (x2-x1) * (y2-y1)
  return area


def area_find_largest(new_box, c_largest=None, c_2nd_largest=None):
    new_a = calc_area(new_box['box_points'])
    largest, sec_largest = None, None

    if c_largest == None:
        largest = new_box
    else:
        a_largest = calc_area(c_largest['box_points'])

        if c_2nd_largest == None:
            temp = [new_box, c_largest]
            temp2 = [new_a, a_largest]
        else:
            a_2nd_largest = calc_area(c_2nd_largest['box_points'])
            temp = [new_box, c_largest, c_2nd_largest]
            temp2 = [new_a, a_largest, a_2nd_largest]

        sort_temp = sorted(temp2)
        largest = temp[temp2.index(sort_temp[-1])]
        sec_largest = temp[temp2.index(sort_temp[-2])]

    return largest, sec_largest



# temp logic here:
# 1. If a object is much larger than other objects (e.g. 2 times), pick it
# 2. If not, find the object with largest occurrences count
def select_object_frame(count_type, largest_box=None, second_largest_box=None):
    result = None

    # case 1: only has one type
    if len(count_type) == 1:
        result = list(count_type.keys())[0]
    else:
        # case 2: more than one type
        if (largest_box != None and second_largest_box != None) and (
                calc_area(largest_box['box_points']) > 2 * calc_area(second_largest_box['box_points'])):
            result = largest_box['name']
        else:
            sorted_count = sorted(count_type.items(), key=lambda kv: kv[1])
            result = sorted_count[-1][0]

    return result


def choose_obj(result):
    total_seconds = len(result)
    output_dict = {}
    result_all_secs = []

    print('Length of the video =  ', len(result), 'sec')
    for (i, eachSec) in enumerate(result):
        print('Second ', i + 1)

        chosen_object_frames = []  # selected object for each frame
        secFrameList = eachSec[1]# the output_arrays

        for eachFrame in secFrameList:
            largest_box = None
            second_largest_box = None
            count_type = {}

            if len(eachFrame) != 0:  # object detected:
                for eachBox in eachFrame:
                    # update occurrences of each object type
                    if len(count_type) != 0 and count_type.__contains__(eachBox['name']):
                        count_type[eachBox['name']] += 1
                    else:
                        count_type[eachBox['name']] = 1

                    # update largest box
                    largest_box, second_largest_box = area_find_largest(eachBox, largest_box, second_largest_box)

                # select object for each frame
                the_chosen_one_frame = select_object_frame(count_type, largest_box, second_largest_box)
                chosen_object_frames.append(the_chosen_one_frame)
            # else:
            #   chosen_object_frames.append(None)

        # select object for each second
        if len(chosen_object_frames) == 0:
            result_all_secs.append(None)
        else:
            count_sec = Counter(chosen_object_frames)  # result is in ordered
            the_chosen_one_sec = list(count_sec.keys())[0]  # largest count

            # Special Case: most of the frames has no detected box, so the largest count is None
            if the_chosen_one_sec == None and len(count_sec) > 1:
                the_chosen_one_sec = list(count_sec.keys())[1]

            result_all_secs.append(the_chosen_one_sec)

        print('Chosen objects from the 1st second =  ', result_all_secs)

    return result_all_secs


"""
Prepare  data that will be saved to json file
"""
def final_result(result_all_secs):
    result = {}
    head = (0, result_all_secs[0])  # time,content
    prev = (0, result_all_secs[0], 0)  # time,content,count
    for index, eachSec in enumerate(result_all_secs):
        if index == 0:
            pass

        if eachSec == head[1]:
            temp = prev[2] + 1
            prev = (index, eachSec, temp)
        else:
            ##Temp logic here: only need to keep a shot that last more than 2 sec
            if (prev[0] - head[0]) >= 1:  # note: 6th sec - 5th sec = 2 sec !
                time_span = str(head[0]) + ' - ' + str(prev[0])
                result[time_span] = head[1]
            print('result = ', result)
            head = (index, eachSec)
            prev = (index, eachSec, 0)

    return result


"""
Save Result to json file
"""
def dict_to_schema (per_sec_object_info,video_info,url,v_index):
    title = video_info['Video Info']['title']
    js_fileName = 'video '+v_index+'.json'
    temp_list=[]

    for key,each in per_sec_object_info.items():
        if (each == None): #Do not pass None, use None for debugging
            continue
        temp_dict={}
        temp_dict['timestamp'] = key
        temp_dict['detection_result'] = each
        temp_list.append(temp_dict)

    df = pd.DataFrame(
        [[title,
          video_info['Video Info']['id'],
          url,
          video_info['Video Info']['genres'],
          video_info['Video Info']['overview'],
          video_info['Video Info']['poster_path'],
          video_info['Video Info']['release_date'],
          video_info['Video Info']['runtime'],
          temp_list]],
        index= [js_fileName],
        columns = ['title','id','url','genres','overview','poster_path','release_date','runtime','detection_info']
    )

    df_json = df.to_json(orient="index",indent = 4).replace('\/', "/")
    parsed = json.loads(df_json)
    json.dumps(parsed, indent=4)

    with open(js_fileName, 'w') as f:
        f.write(df_json)

    return
