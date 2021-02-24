from collections import Counter
import json
import pandas as pd

# assuming box_array being in the format as below
# pass in the info array --> output_Collection_1
# will reformat it with sec and frame number attached
def reformat_ouput(output_info_collection):
  output_frame_array = []
  frame_second = []
  
  for i in range(len(output_info_collection)): # i number of seconds in total
    print("^^^^^^^^^^^^^^^start^^^^^^^^^^^^^^^^^^")
    print("second number is: ", output_info_collection[i][0])
    
    for j in range(len(output_info_collection[i][1])): # number of frames 
      
      print('The number of frames is: {}'.format(len(output_info_collection[i][1])))
      print("============================")
      print('This correspond to the {0} second {1} frame'.format(i,j))
      print(output_info_collection[i][1][j])
      #directly choose the first output object detected within the frame
      
      if(len(output_info_collection[i][1][j])!=0):
        print('This correspond to the {0} second {1} frame, type is: {2}, with accuracy {4}, location: {3}'.format(i,j,output_info_collection[i][1][j][0]['name'],output_info_collection[i][1][j][0]['box_points'],output_info_collection[i][1][j][0]['percentage_probability']))
        object_area = calc_area(output_info_collection[i][1][j][0]['box_points'])
        box_central = find_box_middle(output_info_collection[i][1][j][0]['box_points'])      
        print('the area of the detected object {0}, the central location of the object {1}'.format(object_area, box_central))
        object_type = output_info_collection[i][1][j][0]['name'] 
        print("object type is: ", object_type)
        print("****************************")
        frame_info = {'second': i, 'frame': j, 'type':output_info_collection[i][1][j][0]['name'], 'accuracy':output_info_collection[i][1][j][0]['percentage_probability'], 'location': output_info_collection[i][1][j][0]['box_points'], 'area': object_area, 'central location': box_central}

        output_frame_array.append(frame_info)
      frame_second.append([output_info_collection[i][0],frame_info])
      
  return output_frame_array, frame_second


output_dic_reformated, reformat_frame_second = reformat_ouput(output_Collection_1)



def object_occurrence_within_second_frame(output_dic_reformated):
  format_output_info_array = []
  count = 1
  for i in range(len(output_dic_reformated)-1):
    
    print("===============")
    print("Inside the loop")
    print("Numbers in the range:", i)
    if ((output_dic_reformated[i]['second'] == output_dic_reformated[i+1]['second']) and (output_dic_reformated[i]['type'] == output_dic_reformated[i+1]['type'])):
      count += 1
    elif ((output_dic_reformated[i]['second'] != output_dic_reformated[i+1]['second']) or (output_dic_reformated[i]['type'] != output_dic_reformated[i+1]['type'])):
      print("*********************************")
      print("ready for restart!!")
      print("count before restart is: ", count)
      print("continues counting on the object is: ", output_dic_reformated[i]['type'])
      print("we are currently on the {} second".format(output_dic_reformated[i]['second']))
      insert_frame = {'object_type': output_dic_reformated[i]['type'], 'current_second': output_dic_reformated[i]['second'], 'frame_count': count}
      format_output_info_array.append(insert_frame)
      count = 1

  print("**************************************")    
  print("count after restart is: ", count)
  print("last continuous occurred object is: ", output_dic_reformated[i+1]['type'])
  print("we are currently on the {} second".format(output_dic_reformated[i+1]['second']))
  insert_frame = {'object_type': output_dic_reformated[i+1]['type'], 'current_second': output_dic_reformated[i+1]['second'], 'frame_count': count}
  format_output_info_array.append(insert_frame)

  return format_output_info_array
  
  
  
  processed_array = object_occurrence_within_second_frame(output_dic_reformated)
  
  
  
  def final_intent_reformat(pro_arrayInFrames):
  output_info_dictionary = {}

  for i in range(len(pro_arrayInFrames)):
    print("the iteration number we are entering is: ", i)
    #checking if type already exist in the output dictionary
    typeCheck = pro_arrayInFrames[i]['object_type']
    
    if typeCheck in output_info_dictionary :
      #update second number if already exist in the dictionary 
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
  
  
  
  final_dic_output = final_intent_reformat(processed_array)
  
  
  def final_intent_reformat_update(pro_arrayInFrames):
  output_info_dictionary = {}

  for i in range(len(pro_arrayInFrames)):
    print("the iteration number we are entering is: ", i)
    #checking if type already exist in the output dictionary
    typeCheck = pro_arrayInFrames[i]['object_type']
    
    if typeCheck in output_info_dictionary :
      print("this type has occured before, which is: ", typeCheck)
      #update second number if already exist in the dictionary 
      sec_num = pro_arrayInFrames[i]['current_second']
      value_list = output_info_dictionary[typeCheck]
      last_sec = value_list[-1][1]
      print("current value list is: ", value_list)
      print("seems like the last sec is: ", last_sec)
      #checking if last element needs to be updated or not 
      #value_list[-1][1]
      if ((last_sec+1) == sec_num) :#needs to be updated to the newest
        value_list[-1][1] = sec_num
        print("value list after updating is: ",value_list )
      elif (last_sec != sec_num): #second number is not continuous 
        sec_inner_arr = [sec_num,sec_num]
        value_list.append(sec_inner_arr)

    # has not occurred before, create a new position for it
    else:
      print("this type has not occured before, which is: ", typeCheck)
      d = {}
      d[typeCheck] = []
      sec_num = pro_arrayInFrames[i]['current_second']
      sec_inner_arr = [sec_num,sec_num]
      d[typeCheck].append(sec_inner_arr)
      output_info_dictionary.update(d)

  return output_info_dictionary
  
  
  
  updated_arry = final_intent_reformat_update(processed_array)
  
  
  
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
  
  
  update_arr = quality_score_attempt_version2(updated_arry)
  
  
