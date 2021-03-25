from collections import Counter
import json
import pandas as pd


# assuming box_array being in the format as below
# pass in the info array --> output_Collection_1
# will reformat it with sec and frame number attached
def calc_area(box_point):
    x1, y1, x2, y2 = box_point
    area = (x2 - x1) * (y2 - y1)
    return area


def find_box_middle(box_point):
    x1, y1, x2, y2 = box_point
    x_middle = (x1 + x2) / 2
    y_middle = (y1 + y2) / 2
    middle_point = [x_middle, y_middle]
    return middle_point

#when multiple objects were detected, select the one with the largest area
def select_largest_area_object(multi_objects_array):

    largest_object = multi_objects_array[0]
    num_objects = len(multi_objects_array)

    if(num_objects > 1):
        largest_area = calc_area(multi_objects_array[0]['box_points'])
        # if more than one objects were detected on current frame
        for i in range(num_objects):
            # debug purpose
            print("this number of the object is:", i)
            tem_largest = multi_objects_array[i]
            tem_largest_area = calc_area(tem_largest['box_points'])
            if (tem_largest_area > largest_area):
                largest_object = tem_largest

    return largest_object

def reformat_ouput(output_info_collection):
    output_frame_array = []
    frame_second = []

    for i in range(len(output_info_collection)):  # i number of seconds in total
        print("^^^^^^^^^^^^^^^start^^^^^^^^^^^^^^^^^^")
        print("second number is: ", output_info_collection[i][0])

        for j in range(len(output_info_collection[i][1])):  # number of frames

            print('The number of frames is: {}'.format(len(output_info_collection[i][1])))
            print("============================")
            print('This correspond to the {0} second {1} frame'.format(i, j))
            print(output_info_collection[i][1][j])
            # directly choose the first output object detected within the frame
            #update: always select the object with largest area
            if (len(output_info_collection[i][1][j]) != 0):
                largest_detected_object = select_largest_area_object(output_info_collection[i][1][j])
                print(
                    'This correspond to the {0} second {1} frame, type is: {2}, with accuracy {4}, location: {3}'.format(
                        i, j, largest_detected_object['name'],
                        largest_detected_object['box_points'],
                        largest_detected_object['percentage_probability']))
                object_area = calc_area(largest_detected_object['box_points'])
                box_central = find_box_middle(largest_detected_object['box_points'])
                print('the area of the detected object {0}, the central location of the object {1}'.format(object_area,
                                                                                                           box_central))
                object_type = largest_detected_object['name']
                print("object type is: ", object_type)
                print("****************************")
                frame_info = {'second': i, 'frame': j, 'type': largest_detected_object['name'],
                              'accuracy': largest_detected_object['percentage_probability'],
                              'location': largest_detected_object['box_points'], 'area': object_area,
                              'central location': box_central}

                output_frame_array.append(frame_info)
                frame_second.append([output_info_collection[i][0], frame_info])

    return output_frame_array, frame_second


#
# output_dic_reformated, reformat_frame_second = reformat_ouput(output_Collection_temp)


def object_occurrence_within_second_frame(output_dic_reformated):
    format_output_info_array = []
    count = 1
    for i in range(len(output_dic_reformated) - 1):

        print("===============")
        print("Inside the loop")
        print("Numbers in the range:", i)
        if ((output_dic_reformated[i]['second'] == output_dic_reformated[i + 1]['second']) and (
                output_dic_reformated[i]['type'] == output_dic_reformated[i + 1]['type'])):
            count += 1
        elif ((output_dic_reformated[i]['second'] != output_dic_reformated[i + 1]['second']) or (
                output_dic_reformated[i]['type'] != output_dic_reformated[i + 1]['type'])):
            print("*********************************")
            print("ready for restart!!")
            print("count before restart is: ", count)
            print("continues counting on the object is: ", output_dic_reformated[i]['type'])
            print("we are currently on the {} second".format(output_dic_reformated[i]['second']))
            insert_frame = {'object_type': output_dic_reformated[i]['type'],
                            'current_second': output_dic_reformated[i]['second'], 'frame_count': count}
            format_output_info_array.append(insert_frame)
            count = 1

    print("**************************************")
    print("count after restart is: ", count)
    print("last continuous occurred object is: ", output_dic_reformated[i + 1]['type'])
    print("we are currently on the {} second".format(output_dic_reformated[i + 1]['second']))
    insert_frame = {'object_type': output_dic_reformated[i + 1]['type'],
                    'current_second': output_dic_reformated[i + 1]['second'], 'frame_count': count}
    format_output_info_array.append(insert_frame)

    return format_output_info_array


# processed_array = object_occurrence_within_second_frame(output_dic_reformated)


def final_intent_reformat(pro_arrayInFrames):
    output_info_dictionary = {}

    for i in range(len(pro_arrayInFrames)):
        print("the iteration number we are entering is: ", i)
        # checking if type already exist in the output dictionary
        typeCheck = pro_arrayInFrames[i]['object_type']

        if typeCheck in output_info_dictionary:
            # update second number if already exist in the dictionary
            sec_num = pro_arrayInFrames[i]['current_second']
            value_list = output_info_dictionary[typeCheck]
            if sec_num not in value_list:
                output_info_dictionary[typeCheck].append(sec_num)
        # has not occurred before, create a new position for it
        else:
            d = {}
            d[typeCheck] = []
            sec_num = pro_arrayInFrames[i]['current_second']
            d[typeCheck].append(sec_num)
            output_info_dictionary.update(d)

    return output_info_dictionary


# final_dic_output = final_intent_reformat(processed_array)

def final_intent_reformat_update(pro_arrayInFrames):
    output_info_dictionary = {}

    for i in range(len(pro_arrayInFrames)):
        print("the iteration number we are entering is: ", i)
        # checking if type already exist in the output dictionary
        typeCheck = pro_arrayInFrames[i]['object_type']

        if typeCheck in output_info_dictionary:
            print("this type has occured before, which is: ", typeCheck)
            # update second number if already exist in the dictionary
            sec_num = pro_arrayInFrames[i]['current_second']
            value_list = output_info_dictionary[typeCheck]
            last_sec = value_list[-1][1]
            print("current value list is: ", value_list)
            print("seems like the last sec is: ", last_sec)
            # checking if last element needs to be updated or not
            # value_list[-1][1]
            if (last_sec + 1) == sec_num:  # needs to be updated to the newest
                value_list[-1][1] = sec_num
                print("value list after updating is: ", value_list)
            elif last_sec != sec_num:  # second number is not continuous
                sec_inner_arr = [sec_num, sec_num]
                value_list.append(sec_inner_arr)

        # has not occurred before, create a new position for it
        else:
            print("this type has not occured before, which is: ", typeCheck)
            d = {}
            d[typeCheck] = []
            sec_num = pro_arrayInFrames[i]['current_second']
            sec_inner_arr = [sec_num, sec_num]
            d[typeCheck].append(sec_inner_arr)
            output_info_dictionary.update(d)

    return output_info_dictionary

    # updated_arry = final_intent_reformat_update(processed_array)


def quality_score_attempt_version2(updated_arry):
    score_arry = []
    attempt_score = 10
    for x in updated_arry:
        type_score = 0
        print("current x value is: ", x)
        print("the length of the value is: ", len(updated_arry[x]))
        num_arr = len(updated_arry[x])
        for i in range(num_arr):
            type_score = type_score + updated_arry[x][i][1] - updated_arry[x][i][0] + attempt_score
        print("attemp score is: ", type_score)
        output_dict = {x: updated_arry[x], 'score': type_score}
        score_arry.append(output_dict)
    return score_arry

    #update_arr = quality_score_attempt_version2(updated_arry)

    #print(update_arr)


def object_occurrence_within_second_frame_accuracy_avgArea_avgAcc(output_dic_reformated):
    up_format_output_info_array = []
    count = 1
    area = output_dic_reformated[0]['area']
    acc = output_dic_reformated[0]['accuracy']

    for i in range(len(output_dic_reformated) - 1):

        print("===============")
        print("Inside the loop")
        print("Numbers in the range:", i)
        if ((output_dic_reformated[i]['second'] == output_dic_reformated[i + 1]['second']) and (
                output_dic_reformated[i]['type'] == output_dic_reformated[i + 1]['type'])):
            count += 1
            area += output_dic_reformated[i + 1]['area']
            acc += output_dic_reformated[i + 1]['accuracy']
        elif ((output_dic_reformated[i]['second'] != output_dic_reformated[i + 1]['second']) or (
                output_dic_reformated[i]['type'] != output_dic_reformated[i + 1]['type'])):
            print("*********************************")
            print("ready for restart!!")
            print("count before restart is: ", count)
            print("avgArea before restart is: ", area/count)
            print("avgAccracy before restart is: ", acc/count)
            print("continues counting on the object is: ", output_dic_reformated[i]['type'])
            print("we are currently on the {} second".format(output_dic_reformated[i]['second']))
            insert_frame = {'object_type': output_dic_reformated[i]['type'],
                            'current_second': output_dic_reformated[i]['second'], 'frame_count': count,
                            'avg_area': area/count, 'avg_acc': acc/count}
            up_format_output_info_array.append(insert_frame)
            count = 1
            area = output_dic_reformated[i]['area']
            acc = output_dic_reformated[i]['accuracy']

    print("**************************************")
    print("count after restart is: ", count)
    print("avgArea after restart is: ", area/count)
    print("average accuracy after restart is: ", acc/count)
    print("last continuous occurred object is: ", output_dic_reformated[i + 1]['type'])
    print("we are currently on the {} second".format(output_dic_reformated[i + 1]['second']))
    insert_frame = {'object_type': output_dic_reformated[i + 1]['type'],
                    'current_second': output_dic_reformated[i + 1]['second'], 'frame_count': count,
                    'avg_area':area/count,'avg_acc': acc/count}
    up_format_output_info_array.append(insert_frame)

    return up_format_output_info_array

# update_accuracy_with_area = object_occurrence_within_second_frame_accuracy_avgArea_avgAcc(output_dic_reformated)


def final_intent_reformat_acc(pro_arrayInFrames_acc):
    output_info_dictionary_acc = {}

    for i in range(len(pro_arrayInFrames_acc)):
        print("the iteration number we are entering is: ", i)
        # checking if type already exist in the output dictionary
        typeCheck = pro_arrayInFrames_acc[i]['object_type']

        if typeCheck in output_info_dictionary_acc:
            # update second number if already exist in the dictionary
            acc_num = pro_arrayInFrames_acc[i]['avg_acc']
            value_list = output_info_dictionary_acc[typeCheck]
            if acc_num not in value_list:
                output_info_dictionary_acc[typeCheck].append(acc_num)
        # has not occurred before, create a new position for it
        else:
            d = {}
            d[typeCheck] = []
            acc_num = pro_arrayInFrames_acc[i]['avg_acc']
            d[typeCheck].append(acc_num)
            output_info_dictionary_acc.update(d)

    return output_info_dictionary_acc

#
# final_dic_output_acc = final_intent_reformat_acc(update_accuracy_with_area)

def final_intent_reformat_area(pro_arrayInFrames_acc):
    output_info_dictionary_area = {}

    for i in range(len(pro_arrayInFrames_acc)):
        print("the iteration number we are entering is: ", i)
        # checking if type already exist in the output dictionary
        typeCheck = pro_arrayInFrames_acc[i]['object_type']

        if typeCheck in output_info_dictionary_area:
            # update second number if already exist in the dictionary
            area_num = pro_arrayInFrames_acc[i]['avg_area']
            value_list = output_info_dictionary_area[typeCheck]
            if area_num not in value_list:
                output_info_dictionary_area[typeCheck].append(area_num)
        # has not occurred before, create a new position for it
        else:
            d = {}
            d[typeCheck] = []
            area_num = pro_arrayInFrames_acc[i]['avg_area']
            d[typeCheck].append(area_num)
            output_info_dictionary_area.update(d)

    return output_info_dictionary_area

#
# final_dic_output_area = final_intent_reformat_area(update_accuracy_with_area)


def quality_socre_acc(accuracy_dic_input):
  score_array_acc = []

  for x in accuracy_dic_input:
      #debug purpose
      total_acc = 0
      print("current x value is: ", x)
      print("the length of the corresponding x value is: ", len(accuracy_dic_input[x]))
      num_acc = len(accuracy_dic_input[x])
      for i in range(num_acc):
        total_acc += accuracy_dic_input[x][i]
      print("total accuracy is: ",total_acc)
      avg_Acc = total_acc/num_acc
      out_acc_dic = {x: accuracy_dic_input[x], 'score': avg_Acc}
      score_array_acc.append(out_acc_dic)
  return score_array_acc

# acc_score_dic = quality_socre_acc(final_dic_output_acc)

def quality_socre_area(area_dic_input):
  score_array_area = []

  for x in area_dic_input:
      #debug purpose
      total_area = 0
      print("current x value is: ", x)
      print("the length of the corresponding x value is: ", len(area_dic_input[x]))
      num_area = len(area_dic_input[x])
      for i in range(num_area):
        total_area += area_dic_input[x][i]
      print("total accuracy is: ",total_area)
      avg_Area = total_area/num_area
      out_acc_dic = {x: area_dic_input[x], 'score': avg_Area}
      score_array_area.append(out_acc_dic)
  return score_array_area

# area_score_dic = quality_socre_area(final_dic_output_area)

def final_quaility_score(area_score_dic,acc_score_dic,update_arr):
    len_score = []
    for x in update_arr:
        len_score.append(x['score'])
    acc_score = []
    for i in acc_score_dic:
        acc_score.append(i['score'])
    area_score = []
    for j in area_score_dic:
        area_score.append(j['score'])
    final_score_arr = []
    for i in range(len(update_arr)):
        final_score = area_score[i]*0.2/100 + acc_score[i] * 0.5/100 + len_score[i] * 0.3/100
        update_final_score  = round(final_score,1)# only 1 digit after "."
        final_score_arr.append(final_score)

    for i in range(len(update_arr)):
        update_arr[i]['score'] = final_score_arr[i]

    return update_arr

# score_update_arr = final_quaility_score(area_score_dic,acc_score_dic,update_arr)

def transformArrToJsonFileFormat(score_update_arr):
    json_array = []
    for i in range(len(score_update_arr)):
        print("this is the {} the element in the score array".format(i))
        print(score_update_arr[i])
        for k, v in score_update_arr[i].items():
            print("k value of {0}th element in the score array is:".format(i))
            print(k)
            if (k != 'score'):
                tp = k

                js_out_arr = {'type': tp, 'time': score_update_arr[i][tp], 'score': score_update_arr[i]['score']}
                json_array.append(js_out_arr)

    return json_array

"""
Save Result to json file
"""
def dict_to_schema (score_arr,video_info,url,v_index):
    title = video_info['Video Info']['title']
    js_fileName = 'video '+v_index+'.json'
    anno_list = []
    timeSeg=[]

    for i in range(len(score_arr)):
        print("number of dict is:", i)
        print(score_arr[i])
        anno_dict = {}
        anno_dict['keyword'] = score_arr[i]['type']
        anno_dict['score'] = score_arr[i]['score']
        anno_list.append(anno_dict)

    for i in range(len(score_arr)):
        #print(score_arr[i]['time'])
        num_seg = len(score_arr[i]['time'])

        for j in range(num_seg):
            print(score_arr[i]['type'])
            print(score_arr[i]['time'][j])
            print("start",score_arr[i]['time'][j][0])
            print("end",score_arr[i]['time'][j][-1])
            time_dict = {}
            time_dict['keyword'] = score_arr[i]['type']
            time_dict['start'] = score_arr[i]['time'][j][0]
            time_dict['end'] = score_arr[i]['time'][j][-1]

            timeSeg.append(time_dict)

    pre_string = "https://image.tmdb.org/t/p/original"

    df = pd.DataFrame(
        [[title,
          #video_info['Video Info']['id'],
          #url,
          video_info['Video Info']['runtime'],
          video_info['Video Info']['genres'],#need to be edited maybe manually !!!!
          video_info['Video Info']['overview'],
          pre_string + video_info['Video Info']['poster_path'],
          video_info['Video Info']['release_date'],
          anno_list,
          timeSeg]],
        index= [js_fileName],
        columns = ['title','runtime','genres','overview','posterUrl','releaseDate','annotations','segments']
    )

    df_json = df.to_json(orient="index",indent = 4).replace('\/', "/")
    parsed = json.loads(df_json)
    json.dumps(parsed, indent=4)

    with open(js_fileName, 'w') as f:
        f.write(df_json)

    return
