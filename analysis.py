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

output_Collection_temp = [(1, [[{'name': 'person', 'percentage_probability': 96.82927131652832, 'box_points': [295, 44, 637, 398]}], [{'name': 'person', 'percentage_probability': 96.8692421913147, 'box_points': [294, 45, 637, 397]}], [{'name': 'person', 'percentage_probability': 96.50949239730835, 'box_points': [293, 44, 637, 398]}], [{'name': 'person', 'percentage_probability': 96.55259251594543, 'box_points': [294, 44, 637, 398]}], [{'name': 'person', 'percentage_probability': 95.8750307559967, 'box_points': [293, 47, 638, 395]}], [{'name': 'person', 'percentage_probability': 95.5468475818634, 'box_points': [292, 45, 639, 396]}], [{'name': 'person', 'percentage_probability': 96.17335200309753, 'box_points': [291, 48, 639, 394]}], [{'name': 'person', 'percentage_probability': 95.76746821403503, 'box_points': [291, 48, 639, 392]}], [{'name': 'person', 'percentage_probability': 96.13617658615112, 'box_points': [291, 50, 637, 392]}], [{'name': 'person', 'percentage_probability': 95.05749940872192, 'box_points': [289, 49, 636, 393]}], [{'name': 'person', 'percentage_probability': 94.12708282470703, 'box_points': [290, 50, 638, 389]}], [{'name': 'person', 'percentage_probability': 94.38591599464417, 'box_points': [289, 50, 637, 389]}], [{'name': 'person', 'percentage_probability': 94.4780707359314, 'box_points': [292, 48, 635, 391]}], [{'name': 'person', 'percentage_probability': 96.0079550743103, 'box_points': [289, 49, 636, 390]}], [{'name': 'person', 'percentage_probability': 96.16316556930542, 'box_points': [289, 48, 637, 393]}], [{'name': 'person', 'percentage_probability': 95.24122476577759, 'box_points': [286, 50, 637, 392]}], [{'name': 'person', 'percentage_probability': 93.66161823272705, 'box_points': [286, 51, 638, 391]}], [{'name': 'person', 'percentage_probability': 93.81410479545593, 'box_points': [287, 49, 639, 394]}], [{'name': 'person', 'percentage_probability': 92.83763766288757, 'box_points': [288, 50, 638, 392]}], [{'name': 'person', 'percentage_probability': 92.96866655349731, 'box_points': [286, 49, 638, 392]}], [{'name': 'person', 'percentage_probability': 91.3057029247284, 'box_points': [284, 53, 637, 379]}], [{'name': 'person', 'percentage_probability': 91.3088321685791, 'box_points': [288, 50, 637, 388]}], [{'name': 'person', 'percentage_probability': 93.4547483921051, 'box_points': [283, 52, 638, 383]}]], [{'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}], {'person': 1}),
                          (2, [[{'name': 'person', 'percentage_probability': 91.61617755889893, 'box_points': [283, 51, 637, 386]}], [{'name': 'person', 'percentage_probability': 92.22461581230164, 'box_points': [283, 52, 637, 380]}], [{'name': 'person', 'percentage_probability': 91.40949249267578, 'box_points': [283, 53, 636, 376]}], [{'name': 'person', 'percentage_probability': 89.22054171562195, 'box_points': [284, 54, 634, 381]}], [{'name': 'person', 'percentage_probability': 88.38596940040588, 'box_points': [283, 54, 633, 379]}], [{'name': 'person', 'percentage_probability': 82.45054483413696, 'box_points': [284, 56, 631, 380]}], [{'name': 'person', 'percentage_probability': 75.48195719718933, 'box_points': [282, 54, 632, 377]}], [{'name': 'person', 'percentage_probability': 70.56198120117188, 'box_points': [282, 53, 631, 373]}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], [{'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}], {'person': 0}),
                          (3, [[], [], [], [], [{'name': 'person', 'percentage_probability': 99.32337999343872, 'box_points': [297, 72, 623, 415]}], [{'name': 'person', 'percentage_probability': 99.06272292137146, 'box_points': [291, 76, 626, 413]}], [{'name': 'person', 'percentage_probability': 99.2439329624176, 'box_points': [294, 75, 624, 415]}], [{'name': 'person', 'percentage_probability': 99.19794201850891, 'box_points': [289, 76, 621, 414]}], [{'name': 'person', 'percentage_probability': 99.15759563446045, 'box_points': [288, 75, 620, 415]}], [{'name': 'person', 'percentage_probability': 99.24275279045105, 'box_points': [289, 74, 621, 415]}], [{'name': 'person', 'percentage_probability': 99.2910623550415, 'box_points': [288, 72, 620, 417]}], [{'name': 'person', 'percentage_probability': 99.32926893234253, 'box_points': [289, 72, 621, 418]}], [{'name': 'person', 'percentage_probability': 99.30818676948547, 'box_points': [289, 72, 621, 418]}], [{'name': 'person', 'percentage_probability': 99.27644729614258, 'box_points': [288, 72, 622, 417]}], [{'name': 'person', 'percentage_probability': 99.28801655769348, 'box_points': [290, 72, 621, 418]}], [{'name': 'person', 'percentage_probability': 99.2851734161377, 'box_points': [289, 71, 622, 419]}], [{'name': 'person', 'percentage_probability': 99.26844239234924, 'box_points': [285, 72, 623, 419]}], [{'name': 'person', 'percentage_probability': 99.26973581314087, 'box_points': [286, 72, 622, 419]}], [{'name': 'person', 'percentage_probability': 99.18662905693054, 'box_points': [286, 72, 618, 417]}], [{'name': 'person', 'percentage_probability': 99.25442337989807, 'box_points': [286, 72, 618, 418]}], [{'name': 'person', 'percentage_probability': 99.37023520469666, 'box_points': [285, 72, 619, 417]}], [{'name': 'person', 'percentage_probability': 99.37298893928528, 'box_points': [291, 71, 618, 416]}], [{'name': 'person', 'percentage_probability': 99.35727715492249, 'box_points': [296, 71, 618, 417]}]], [{}, {}, {}, {}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}], {'person': 0}),
                          (4, [[{'name': 'person', 'percentage_probability': 99.2735505104065, 'box_points': [292, 71, 617, 417]}], [{'name': 'person', 'percentage_probability': 99.10821914672852, 'box_points': [295, 72, 617, 418]}], [{'name': 'person', 'percentage_probability': 99.12167191505432, 'box_points': [288, 75, 620, 415]}], [{'name': 'person', 'percentage_probability': 98.8122284412384, 'box_points': [290, 73, 617, 413]}], [{'name': 'person', 'percentage_probability': 98.64466190338135, 'box_points': [284, 70, 612, 415]}], [{'name': 'person', 'percentage_probability': 98.52356314659119, 'box_points': [285, 71, 610, 414]}], [{'name': 'person', 'percentage_probability': 98.34051728248596, 'box_points': [286, 74, 612, 414]}], [{'name': 'person', 'percentage_probability': 98.08198809623718, 'box_points': [286, 76, 613, 412]}], [{'name': 'person', 'percentage_probability': 98.57721328735352, 'box_points': [291, 73, 617, 412]}], [{'name': 'person', 'percentage_probability': 98.67697358131409, 'box_points': [292, 71, 616, 413]}], [{'name': 'person', 'percentage_probability': 98.7047016620636, 'box_points': [291, 71, 615, 413]}], [{'name': 'person', 'percentage_probability': 98.6397922039032, 'box_points': [289, 71, 614, 413]}], [{'name': 'person', 'percentage_probability': 98.70670437812805, 'box_points': [288, 71, 613, 414]}], [{'name': 'person', 'percentage_probability': 98.71838688850403, 'box_points': [288, 70, 612, 416]}], [{'name': 'person', 'percentage_probability': 83.24831128120422, 'box_points': [164, 118, 424, 391]}], [], [{'name': 'person', 'percentage_probability': 70.88921070098877, 'box_points': [135, 141, 411, 406]}], [{'name': 'person', 'percentage_probability': 83.47342610359192, 'box_points': [127, 191, 384, 409]}], [{'name': 'person', 'percentage_probability': 63.19856643676758, 'box_points': [72, 202, 360, 391]}], [], [{'name': 'person', 'percentage_probability': 75.72823762893677, 'box_points': [46, 199, 217, 369]}], [], [{'name': 'person', 'percentage_probability': 61.749619245529175, 'box_points': [19, 200, 174, 363]}]], [{'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {}, {'person': 1}, {'person': 1}, {'person': 1}, {}, {'person': 1}, {}, {'person': 1}], {'person': 0}),
                          (5, [[{'name': 'person', 'percentage_probability': 71.42916321754456, 'box_points': [212, 153, 368, 391]}, {'name': 'person', 'percentage_probability': 69.01410222053528, 'box_points': [19, 196, 175, 363]}], [{'name': 'person', 'percentage_probability': 74.93714094161987, 'box_points': [223, 143, 376, 394]}, {'name': 'person', 'percentage_probability': 72.99303412437439, 'box_points': [19, 194, 176, 363]}], [{'name': 'person', 'percentage_probability': 92.9118812084198, 'box_points': [214, 121, 375, 396]}, {'name': 'person', 'percentage_probability': 55.97980618476868, 'box_points': [474, 187, 535, 341]}, {'name': 'person', 'percentage_probability': 72.54340648651123, 'box_points': [18, 193, 175, 362]}], [{'name': 'person', 'percentage_probability': 91.79216623306274, 'box_points': [206, 121, 375, 386]}, {'name': 'person', 'percentage_probability': 54.78193163871765, 'box_points': [472, 188, 536, 342]}, {'name': 'person', 'percentage_probability': 74.05514717102051, 'box_points': [16, 196, 173, 364]}], [{'name': 'person', 'percentage_probability': 92.43969917297363, 'box_points': [192, 115, 375, 388]}, {'name': 'person', 'percentage_probability': 50.279515981674194, 'box_points': [473, 185, 538, 343]}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], [{'person': 2}, {'person': 2}, {'person': 3}, {'person': 3}, {'person': 2}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}], {'person': 0}),
                          (6, [[{'name': 'person', 'percentage_probability': 77.65394449234009, 'box_points': [57, 41, 541, 366]}], [{'name': 'person', 'percentage_probability': 75.2770483493805, 'box_points': [58, 41, 541, 366]}], [{'name': 'person', 'percentage_probability': 77.0573616027832, 'box_points': [61, 41, 540, 367]}], [{'name': 'person', 'percentage_probability': 76.39549970626831, 'box_points': [60, 40, 539, 367]}], [{'name': 'person', 'percentage_probability': 83.85465145111084, 'box_points': [61, 41, 543, 369]}], [{'name': 'person', 'percentage_probability': 76.83209180831909, 'box_points': [64, 34, 538, 371]}], [{'name': 'person', 'percentage_probability': 57.255733013153076, 'box_points': [53, 13, 540, 372]}], [], [], [], [], [], [], [], [{'name': 'person', 'percentage_probability': 55.93287944793701, 'box_points': [260, 106, 615, 396]}], [{'name': 'couch', 'percentage_probability': 56.31125569343567, 'box_points': [116, 150, 638, 439]}, {'name': 'person', 'percentage_probability': 71.22646570205688, 'box_points': [235, 119, 606, 401]}], [{'name': 'couch', 'percentage_probability': 55.073535442352295, 'box_points': [131, 149, 630, 448]}, {'name': 'person', 'percentage_probability': 87.44322061538696, 'box_points': [241, 103, 593, 403]}], [{'name': 'couch', 'percentage_probability': 58.61566662788391, 'box_points': [124, 145, 630, 452]}, {'name': 'person', 'percentage_probability': 91.58228635787964, 'box_points': [242, 100, 593, 405]}], [{'name': 'couch', 'percentage_probability': 66.69763922691345, 'box_points': [130, 141, 626, 453]}, {'name': 'person', 'percentage_probability': 93.56296062469482, 'box_points': [233, 99, 600, 403]}], [{'name': 'couch', 'percentage_probability': 63.963937759399414, 'box_points': [131, 140, 627, 451]}, {'name': 'person', 'percentage_probability': 94.10867691040039, 'box_points': [235, 99, 598, 403]}], [{'name': 'couch', 'percentage_probability': 63.64133358001709, 'box_points': [132, 140, 627, 452]}, {'name': 'person', 'percentage_probability': 93.95342469215393, 'box_points': [235, 98, 597, 403]}], [{'name': 'couch', 'percentage_probability': 64.4484281539917, 'box_points': [133, 139, 626, 452]}, {'name': 'person', 'percentage_probability': 93.89503002166748, 'box_points': [233, 98, 599, 403]}], [{'name': 'couch', 'percentage_probability': 64.21086192131042, 'box_points': [135, 140, 626, 452]}, {'name': 'person', 'percentage_probability': 94.12632584571838, 'box_points': [232, 98, 600, 404]}]], [{'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {}, {}, {}, {}, {}, {}, {}, {'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}], {'person': 0, 'couch': 0}),
                          (7, [[{'name': 'couch', 'percentage_probability': 64.89205956459045, 'box_points': [136, 140, 625, 451]}, {'name': 'person', 'percentage_probability': 94.60631012916565, 'box_points': [231, 97, 600, 404]}], [{'name': 'couch', 'percentage_probability': 64.21177387237549, 'box_points': [137, 139, 625, 452]}, {'name': 'person', 'percentage_probability': 94.6535050868988, 'box_points': [231, 97, 600, 404]}], [{'name': 'couch', 'percentage_probability': 65.03366827964783, 'box_points': [137, 138, 624, 451]}, {'name': 'person', 'percentage_probability': 94.9234127998352, 'box_points': [230, 97, 601, 404]}], [{'name': 'couch', 'percentage_probability': 65.68722128868103, 'box_points': [137, 138, 624, 450]}, {'name': 'person', 'percentage_probability': 94.94314193725586, 'box_points': [229, 97, 602, 403]}], [{'name': 'couch', 'percentage_probability': 63.47220540046692, 'box_points': [137, 138, 625, 450]}, {'name': 'person', 'percentage_probability': 94.85585689544678, 'box_points': [229, 96, 602, 403]}], [{'name': 'couch', 'percentage_probability': 62.98450827598572, 'box_points': [136, 138, 626, 451]}, {'name': 'person', 'percentage_probability': 94.84168291091919, 'box_points': [231, 97, 601, 404]}], [{'name': 'couch', 'percentage_probability': 62.56442070007324, 'box_points': [135, 138, 626, 452]}, {'name': 'person', 'percentage_probability': 94.62029933929443, 'box_points': [233, 97, 599, 404]}], [{'name': 'couch', 'percentage_probability': 63.235777616500854, 'box_points': [136, 139, 625, 452]}, {'name': 'person', 'percentage_probability': 94.50832605361938, 'box_points': [233, 97, 599, 404]}], [{'name': 'couch', 'percentage_probability': 62.836599349975586, 'box_points': [135, 139, 625, 453]}, {'name': 'person', 'percentage_probability': 94.75063681602478, 'box_points': [233, 97, 599, 404]}], [{'name': 'couch', 'percentage_probability': 63.853633403778076, 'box_points': [134, 139, 625, 453]}, {'name': 'person', 'percentage_probability': 94.73913908004761, 'box_points': [232, 97, 600, 404]}], [{'name': 'couch', 'percentage_probability': 63.508230447769165, 'box_points': [133, 140, 625, 453]}, {'name': 'person', 'percentage_probability': 94.54130530357361, 'box_points': [233, 97, 600, 404]}], [{'name': 'couch', 'percentage_probability': 64.27590250968933, 'box_points': [132, 139, 625, 452]}, {'name': 'person', 'percentage_probability': 94.43091750144958, 'box_points': [233, 98, 600, 404]}], [{'name': 'couch', 'percentage_probability': 63.61395716667175, 'box_points': [133, 139, 625, 452]}, {'name': 'person', 'percentage_probability': 94.29464936256409, 'box_points': [233, 98, 600, 404]}], [{'name': 'couch', 'percentage_probability': 63.245487213134766, 'box_points': [134, 138, 625, 451]}, {'name': 'person', 'percentage_probability': 94.72246170043945, 'box_points': [234, 98, 600, 404]}], [{'name': 'couch', 'percentage_probability': 63.084572553634644, 'box_points': [133, 138, 626, 451]}, {'name': 'person', 'percentage_probability': 94.67672109603882, 'box_points': [235, 98, 600, 404]}], [{'name': 'couch', 'percentage_probability': 63.21825981140137, 'box_points': [134, 138, 626, 451]}, {'name': 'person', 'percentage_probability': 94.70435976982117, 'box_points': [234, 98, 601, 404]}], [{'name': 'couch', 'percentage_probability': 61.78666353225708, 'box_points': [133, 138, 627, 451]}, {'name': 'person', 'percentage_probability': 94.78362202644348, 'box_points': [236, 99, 600, 403]}], [{'name': 'couch', 'percentage_probability': 62.410157918930054, 'box_points': [131, 140, 628, 451]}, {'name': 'person', 'percentage_probability': 94.60143446922302, 'box_points': [236, 99, 600, 403]}], [{'name': 'couch', 'percentage_probability': 61.81066036224365, 'box_points': [128, 140, 628, 451]}, {'name': 'person', 'percentage_probability': 94.64399218559265, 'box_points': [237, 99, 600, 403]}], [{'name': 'person', 'percentage_probability': 98.99426102638245, 'box_points': [242, 80, 616, 412]}], [{'name': 'person', 'percentage_probability': 98.97672533988953, 'box_points': [241, 80, 616, 412]}], [{'name': 'person', 'percentage_probability': 98.97985458374023, 'box_points': [241, 80, 616, 413]}], [{'name': 'person', 'percentage_probability': 98.9917516708374, 'box_points': [241, 80, 617, 413]}]], [{'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}], {'couch': 0, 'person': 1}),
                          (8, [[{'name': 'person', 'percentage_probability': 99.01639223098755, 'box_points': [241, 80, 617, 413]}], [{'name': 'person', 'percentage_probability': 98.98568391799927, 'box_points': [240, 80, 616, 413]}], [{'name': 'person', 'percentage_probability': 98.99671077728271, 'box_points': [240, 80, 617, 413]}], [{'name': 'person', 'percentage_probability': 98.94515872001648, 'box_points': [238, 80, 617, 413]}], [{'name': 'person', 'percentage_probability': 98.9778459072113, 'box_points': [238, 80, 617, 413]}], [{'name': 'person', 'percentage_probability': 98.99974465370178, 'box_points': [239, 80, 617, 413]}], [{'name': 'person', 'percentage_probability': 98.98527264595032, 'box_points': [239, 80, 617, 413]}], [{'name': 'person', 'percentage_probability': 99.01180863380432, 'box_points': [240, 80, 617, 413]}], [{'name': 'person', 'percentage_probability': 98.97738099098206, 'box_points': [240, 80, 617, 413]}], [{'name': 'person', 'percentage_probability': 99.00175333023071, 'box_points': [241, 80, 617, 413]}], [{'name': 'person', 'percentage_probability': 98.96407127380371, 'box_points': [239, 79, 616, 414]}], [{'name': 'person', 'percentage_probability': 98.97714853286743, 'box_points': [239, 79, 617, 414]}], [{'name': 'person', 'percentage_probability': 99.04852509498596, 'box_points': [240, 79, 616, 413]}], [{'name': 'person', 'percentage_probability': 99.03004765510559, 'box_points': [240, 79, 616, 412]}], [{'name': 'couch', 'percentage_probability': 65.1408314704895, 'box_points': [121, 142, 627, 451]}, {'name': 'person', 'percentage_probability': 94.95673775672913, 'box_points': [240, 99, 593, 405]}], [{'name': 'couch', 'percentage_probability': 65.15615582466125, 'box_points': [121, 142, 627, 452]}, {'name': 'person', 'percentage_probability': 95.03103494644165, 'box_points': [239, 98, 593, 405]}], [{'name': 'couch', 'percentage_probability': 64.50654864311218, 'box_points': [122, 142, 627, 452]}, {'name': 'person', 'percentage_probability': 95.28525471687317, 'box_points': [239, 98, 594, 405]}], [{'name': 'couch', 'percentage_probability': 65.50527811050415, 'box_points': [125, 142, 627, 452]}, {'name': 'person', 'percentage_probability': 95.57399153709412, 'box_points': [236, 97, 596, 407]}], [{'name': 'couch', 'percentage_probability': 65.55337309837341, 'box_points': [125, 142, 627, 452]}, {'name': 'person', 'percentage_probability': 95.60738205909729, 'box_points': [235, 97, 596, 407]}], [{'name': 'couch', 'percentage_probability': 65.68571329116821, 'box_points': [126, 142, 625, 451]}, {'name': 'person', 'percentage_probability': 95.66906094551086, 'box_points': [235, 97, 596, 407]}], [{'name': 'couch', 'percentage_probability': 65.35571813583374, 'box_points': [124, 143, 626, 451]}, {'name': 'person', 'percentage_probability': 95.54954171180725, 'box_points': [236, 97, 595, 407]}], [{'name': 'couch', 'percentage_probability': 65.62490463256836, 'box_points': [124, 142, 626, 450]}, {'name': 'person', 'percentage_probability': 95.61995267868042, 'box_points': [236, 98, 595, 407]}], [{'name': 'couch', 'percentage_probability': 64.91658687591553, 'box_points': [124, 142, 626, 450]}, {'name': 'person', 'percentage_probability': 95.60878872871399, 'box_points': [236, 98, 595, 406]}]], [{'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}], {'person': 1, 'couch': 0}),
                          (9, [[{'name': 'couch', 'percentage_probability': 59.999412298202515, 'box_points': [119, 140, 628, 448]}, {'name': 'person', 'percentage_probability': 94.49270367622375, 'box_points': [239, 98, 592, 405]}], [{'name': 'couch', 'percentage_probability': 59.282177686691284, 'box_points': [119, 141, 628, 449]}, {'name': 'person', 'percentage_probability': 94.73745226860046, 'box_points': [239, 98, 591, 406]}], [{'name': 'couch', 'percentage_probability': 60.83126664161682, 'box_points': [119, 140, 628, 449]}, {'name': 'person', 'percentage_probability': 94.93099451065063, 'box_points': [241, 99, 590, 405]}], [], [], [], [], [], [], [{'name': 'person', 'percentage_probability': 59.54936146736145, 'box_points': [181, 105, 334, 399]}], [], [{'name': 'person', 'percentage_probability': 68.04463863372803, 'box_points': [202, 145, 372, 394]}], [{'name': 'person', 'percentage_probability': 75.96994638442993, 'box_points': [207, 148, 371, 394]}], [{'name': 'person', 'percentage_probability': 96.12146615982056, 'box_points': [138, 103, 449, 389]}], [{'name': 'person', 'percentage_probability': 92.90900230407715, 'box_points': [143, 89, 463, 383]}], [{'name': 'person', 'percentage_probability': 91.29589200019836, 'box_points': [175, 102, 494, 393]}], [{'name': 'person', 'percentage_probability': 95.09658217430115, 'box_points': [189, 98, 484, 395]}], [{'name': 'person', 'percentage_probability': 97.97598719596863, 'box_points': [182, 95, 492, 401]}], [{'name': 'person', 'percentage_probability': 98.48287105560303, 'box_points': [190, 105, 495, 400]}], [{'name': 'person', 'percentage_probability': 98.8987684249878, 'box_points': [193, 105, 504, 403]}], [{'name': 'person', 'percentage_probability': 94.89428997039795, 'box_points': [190, 106, 510, 398]}], [{'name': 'person', 'percentage_probability': 76.40334367752075, 'box_points': [220, 73, 398, 384]}], [{'name': 'person', 'percentage_probability': 76.15976333618164, 'box_points': [213, 76, 403, 386]}]], [{'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {'couch': 1, 'person': 1}, {}, {}, {}, {}, {}, {}, {'person': 1}, {}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}], {'couch': 0, 'person': 0}),
                          (10, [[{'name': 'person', 'percentage_probability': 75.65928101539612, 'box_points': [209, 87, 403, 390]}], [{'name': 'person', 'percentage_probability': 71.19921445846558, 'box_points': [206, 84, 401, 385]}], [], [], [], [{'name': 'person', 'percentage_probability': 72.52044081687927, 'box_points': [189, 109, 354, 390]}], [{'name': 'person', 'percentage_probability': 84.95193123817444, 'box_points': [185, 110, 353, 392]}], [{'name': 'person', 'percentage_probability': 82.85227417945862, 'box_points': [191, 137, 300, 381]}], [{'name': 'person', 'percentage_probability': 61.33061647415161, 'box_points': [189, 138, 303, 381]}], [{'name': 'person', 'percentage_probability': 67.42435693740845, 'box_points': [138, 123, 302, 365]}], [{'name': 'person', 'percentage_probability': 61.96507215499878, 'box_points': [143, 123, 302, 364]}], [{'name': 'person', 'percentage_probability': 77.73433923721313, 'box_points': [142, 121, 304, 365]}], [{'name': 'person', 'percentage_probability': 65.88979363441467, 'box_points': [189, 131, 303, 375]}], [{'name': 'person', 'percentage_probability': 75.7569968700409, 'box_points': [190, 126, 304, 379]}], [{'name': 'person', 'percentage_probability': 70.19199728965759, 'box_points': [190, 126, 303, 379]}], [{'name': 'person', 'percentage_probability': 72.84826040267944, 'box_points': [190, 123, 303, 378]}], [{'name': 'person', 'percentage_probability': 71.2151288986206, 'box_points': [138, 115, 299, 369]}], [{'name': 'person', 'percentage_probability': 70.46579122543335, 'box_points': [139, 117, 296, 367]}], [{'name': 'person', 'percentage_probability': 99.85567331314087, 'box_points': [133, 95, 314, 376]}, {'name': 'chair', 'percentage_probability': 67.48857498168945, 'box_points': [388, 251, 630, 416]}, {'name': 'couch', 'percentage_probability': 63.84124755859375, 'box_points': [388, 251, 630, 416]}], [{'name': 'person', 'percentage_probability': 99.86842274665833, 'box_points': [139, 94, 304, 377]}, {'name': 'chair', 'percentage_probability': 64.6019458770752, 'box_points': [387, 249, 633, 419]}, {'name': 'couch', 'percentage_probability': 67.90146231651306, 'box_points': [387, 249, 633, 419]}, {'name': 'chair', 'percentage_probability': 64.095139503479, 'box_points': [19, 228, 172, 366]}], [{'name': 'person', 'percentage_probability': 99.83199834823608, 'box_points': [151, 90, 304, 373]}, {'name': 'chair', 'percentage_probability': 62.02691197395325, 'box_points': [394, 246, 635, 420]}, {'name': 'couch', 'percentage_probability': 70.4049825668335, 'box_points': [394, 246, 635, 420]}, {'name': 'chair', 'percentage_probability': 50.884515047073364, 'box_points': [18, 226, 175, 364]}], [{'name': 'person', 'percentage_probability': 99.6580719947815, 'box_points': [147, 90, 315, 378]}, {'name': 'couch', 'percentage_probability': 67.37791895866394, 'box_points': [395, 246, 634, 418]}, {'name': 'chair', 'percentage_probability': 59.39796566963196, 'box_points': [18, 226, 178, 364]}], [{'name': 'person', 'percentage_probability': 99.8578429222107, 'box_points': [143, 93, 315, 381]}, {'name': 'couch', 'percentage_probability': 64.71104025840759, 'box_points': [393, 245, 636, 419]}, {'name': 'chair', 'percentage_probability': 57.46159553527832, 'box_points': [15, 224, 186, 366]}]], [{'person': 1}, {'person': 1}, {}, {}, {}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1, 'chair': 1, 'couch': 1}, {'person': 1, 'chair': 2, 'couch': 1}, {'person': 1, 'chair': 2, 'couch': 1}, {'person': 1, 'couch': 1, 'chair': 1}, {'person': 1, 'couch': 1, 'chair': 1}], {'person': 0, 'chair': 0, 'couch': 0}),
                          (11, [[{'name': 'person', 'percentage_probability': 78.28536629676819, 'box_points': [213, 89, 464, 401]}], [{'name': 'person', 'percentage_probability': 78.17673087120056, 'box_points': [215, 88, 467, 400]}], [{'name': 'person', 'percentage_probability': 72.13614583015442, 'box_points': [216, 87, 461, 402]}], [{'name': 'person', 'percentage_probability': 60.821813344955444, 'box_points': [3, 43, 195, 345]}, {'name': 'person', 'percentage_probability': 69.99295353889465, 'box_points': [218, 86, 461, 402]}, {'name': 'tie', 'percentage_probability': 52.74421572685242, 'box_points': [85, 143, 119, 209]}], [{'name': 'person', 'percentage_probability': 58.22204947471619, 'box_points': [1, 42, 195, 348]}, {'name': 'person', 'percentage_probability': 66.67481660842896, 'box_points': [211, 84, 461, 404]}], [{'name': 'person', 'percentage_probability': 83.40834975242615, 'box_points': [2, 43, 197, 348]}, {'name': 'person', 'percentage_probability': 64.01469111442566, 'box_points': [209, 84, 460, 404]}], [{'name': 'person', 'percentage_probability': 89.46884274482727, 'box_points': [3, 45, 199, 348]}, {'name': 'person', 'percentage_probability': 62.367433309555054, 'box_points': [205, 84, 463, 405]}], [{'name': 'person', 'percentage_probability': 87.84010410308838, 'box_points': [1, 45, 197, 348]}, {'name': 'person', 'percentage_probability': 69.75840330123901, 'box_points': [206, 85, 465, 405]}], [{'name': 'person', 'percentage_probability': 96.22094631195068, 'box_points': [6, 47, 214, 368]}, {'name': 'person', 'percentage_probability': 98.7641453742981, 'box_points': [216, 101, 447, 406]}, {'name': 'tie', 'percentage_probability': 83.86446237564087, 'box_points': [297, 244, 329, 296]}], [{'name': 'person', 'percentage_probability': 96.24910950660706, 'box_points': [6, 46, 214, 368]}, {'name': 'person', 'percentage_probability': 98.76150488853455, 'box_points': [217, 99, 446, 406]}, {'name': 'tie', 'percentage_probability': 83.68709087371826, 'box_points': [297, 243, 330, 296]}], [{'name': 'person', 'percentage_probability': 96.92749977111816, 'box_points': [5, 45, 216, 367]}, {'name': 'person', 'percentage_probability': 98.91579747200012, 'box_points': [217, 100, 450, 405]}, {'name': 'tie', 'percentage_probability': 81.06551170349121, 'box_points': [297, 243, 329, 296]}], [{'name': 'person', 'percentage_probability': 97.23974466323853, 'box_points': [5, 46, 215, 366]}, {'name': 'person', 'percentage_probability': 98.88810515403748, 'box_points': [215, 101, 450, 405]}, {'name': 'tie', 'percentage_probability': 81.90773129463196, 'box_points': [297, 242, 329, 296]}], [{'name': 'person', 'percentage_probability': 97.02737927436829, 'box_points': [5, 43, 217, 367]}, {'name': 'person', 'percentage_probability': 98.58806729316711, 'box_points': [213, 100, 448, 405]}, {'name': 'tie', 'percentage_probability': 81.07225298881531, 'box_points': [297, 242, 329, 296]}], [{'name': 'person', 'percentage_probability': 96.88299298286438, 'box_points': [4, 39, 219, 367]}, {'name': 'person', 'percentage_probability': 98.69376420974731, 'box_points': [210, 100, 448, 406]}, {'name': 'tie', 'percentage_probability': 81.23417496681213, 'box_points': [296, 243, 329, 296]}]], [{'person': 1}, {'person': 1}, {'person': 1}, {'person': 2, 'tie': 1}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}], {'person': 1, 'tie': 0}),
                          (12, [[{'name': 'person', 'percentage_probability': 97.29366898536682, 'box_points': [4, 37, 221, 366]}, {'name': 'person', 'percentage_probability': 98.60242009162903, 'box_points': [205, 100, 448, 406]}, {'name': 'tie', 'percentage_probability': 78.32034826278687, 'box_points': [296, 243, 328, 295]}], [{'name': 'person', 'percentage_probability': 97.56016731262207, 'box_points': [3, 36, 223, 366]}, {'name': 'person', 'percentage_probability': 98.6354649066925, 'box_points': [204, 102, 447, 406]}, {'name': 'tie', 'percentage_probability': 77.07198858261108, 'box_points': [297, 244, 328, 295]}], [{'name': 'person', 'percentage_probability': 97.18708395957947, 'box_points': [3, 36, 223, 366]}, {'name': 'person', 'percentage_probability': 98.61301779747009, 'box_points': [203, 102, 446, 406]}, {'name': 'tie', 'percentage_probability': 76.44110918045044, 'box_points': [296, 243, 328, 295]}], [{'name': 'person', 'percentage_probability': 96.56349420547485, 'box_points': [4, 39, 221, 364]}, {'name': 'person', 'percentage_probability': 98.49416613578796, 'box_points': [202, 103, 446, 406]}, {'name': 'tie', 'percentage_probability': 77.19920873641968, 'box_points': [297, 244, 328, 295]}], [{'name': 'person', 'percentage_probability': 96.37547135353088, 'box_points': [3, 39, 221, 363]}, {'name': 'person', 'percentage_probability': 98.43558073043823, 'box_points': [201, 103, 445, 406]}, {'name': 'tie', 'percentage_probability': 77.16944217681885, 'box_points': [296, 244, 328, 295]}], [{'name': 'person', 'percentage_probability': 95.7293689250946, 'box_points': [4, 41, 219, 364]}, {'name': 'person', 'percentage_probability': 98.51089119911194, 'box_points': [201, 104, 445, 405]}, {'name': 'tie', 'percentage_probability': 74.46305751800537, 'box_points': [296, 244, 328, 295]}], [{'name': 'person', 'percentage_probability': 96.39967083930969, 'box_points': [96, 81, 419, 413]}], [{'name': 'person', 'percentage_probability': 96.23736143112183, 'box_points': [93, 81, 420, 414]}], [{'name': 'person', 'percentage_probability': 95.61851024627686, 'box_points': [93, 81, 420, 414]}], [{'name': 'person', 'percentage_probability': 95.42033672332764, 'box_points': [93, 81, 419, 413]}], [], [], [], [{'name': 'person', 'percentage_probability': 80.5647611618042, 'box_points': [34, 53, 384, 349]}]], [{'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}, {'person': 2, 'tie': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {}, {}, {}, {'person': 1}], {'person': 1, 'tie': 0}),
                          (13, [[], [{'name': 'person', 'percentage_probability': 76.7524003982544, 'box_points': [145, 57, 255, 248]}, {'name': 'person', 'percentage_probability': 92.95424818992615, 'box_points': [227, 72, 341, 261]}], [{'name': 'person', 'percentage_probability': 88.52049112319946, 'box_points': [223, 69, 343, 264]}], [{'name': 'person', 'percentage_probability': 69.36225891113281, 'box_points': [142, 56, 256, 252]}, {'name': 'person', 'percentage_probability': 92.98699498176575, 'box_points': [228, 71, 343, 260]}], [{'name': 'person', 'percentage_probability': 89.52484130859375, 'box_points': [142, 59, 259, 252]}, {'name': 'person', 'percentage_probability': 95.03880739212036, 'box_points': [229, 73, 339, 260]}], [{'name': 'person', 'percentage_probability': 87.70829439163208, 'box_points': [141, 58, 260, 253]}, {'name': 'person', 'percentage_probability': 94.359290599823, 'box_points': [228, 71, 341, 261]}], [{'name': 'person', 'percentage_probability': 88.14775943756104, 'box_points': [146, 60, 258, 247]}, {'name': 'person', 'percentage_probability': 95.3434944152832, 'box_points': [227, 72, 339, 260]}], [{'name': 'person', 'percentage_probability': 90.04506468772888, 'box_points': [145, 60, 259, 246]}, {'name': 'person', 'percentage_probability': 95.78232169151306, 'box_points': [227, 71, 339, 260]}], [{'name': 'person', 'percentage_probability': 89.62427377700806, 'box_points': [144, 61, 260, 246]}, {'name': 'person', 'percentage_probability': 95.1492965221405, 'box_points': [226, 71, 339, 260]}], [{'name': 'person', 'percentage_probability': 88.362717628479, 'box_points': [147, 60, 261, 247]}, {'name': 'person', 'percentage_probability': 94.98403668403625, 'box_points': [225, 70, 340, 260]}], [{'name': 'person', 'percentage_probability': 88.33380937576294, 'box_points': [147, 60, 260, 247]}, {'name': 'person', 'percentage_probability': 95.38645148277283, 'box_points': [224, 69, 340, 261]}], [{'name': 'person', 'percentage_probability': 84.94828939437866, 'box_points': [145, 61, 261, 244]}, {'name': 'person', 'percentage_probability': 96.22145295143127, 'box_points': [223, 69, 341, 260]}], [{'name': 'person', 'percentage_probability': 81.15270733833313, 'box_points': [147, 61, 261, 244]}, {'name': 'person', 'percentage_probability': 96.62929773330688, 'box_points': [222, 69, 341, 260]}], [{'name': 'person', 'percentage_probability': 81.37046098709106, 'box_points': [148, 61, 260, 243]}, {'name': 'person', 'percentage_probability': 96.78886532783508, 'box_points': [222, 69, 340, 259]}]], [{}, {'person': 2}, {'person': 1}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}], {'person': 1}),
                          (14, [[{'name': 'person', 'percentage_probability': 82.38322734832764, 'box_points': [149, 61, 260, 244]}, {'name': 'person', 'percentage_probability': 95.84000706672668, 'box_points': [223, 70, 340, 259]}], [{'name': 'person', 'percentage_probability': 83.98786187171936, 'box_points': [147, 61, 261, 243]}, {'name': 'person', 'percentage_probability': 95.62036991119385, 'box_points': [223, 69, 340, 258]}], [{'name': 'person', 'percentage_probability': 83.25215578079224, 'box_points': [146, 62, 261, 243]}, {'name': 'person', 'percentage_probability': 95.91836333274841, 'box_points': [223, 69, 341, 259]}], [{'name': 'person', 'percentage_probability': 83.32857489585876, 'box_points': [145, 62, 261, 242]}, {'name': 'person', 'percentage_probability': 96.1076021194458, 'box_points': [223, 70, 341, 258]}], [{'name': 'person', 'percentage_probability': 97.26542234420776, 'box_points': [141, 60, 412, 391]}], [{'name': 'person', 'percentage_probability': 97.3709762096405, 'box_points': [141, 61, 414, 391]}], [{'name': 'person', 'percentage_probability': 97.39221334457397, 'box_points': [141, 60, 415, 392]}], [{'name': 'person', 'percentage_probability': 97.0413327217102, 'box_points': [140, 61, 412, 391]}], [{'name': 'person', 'percentage_probability': 96.72560691833496, 'box_points': [141, 61, 413, 390]}], [{'name': 'person', 'percentage_probability': 95.35410404205322, 'box_points': [138, 66, 410, 389]}], [{'name': 'person', 'percentage_probability': 96.50759696960449, 'box_points': [117, 97, 434, 410]}], [{'name': 'person', 'percentage_probability': 96.7717170715332, 'box_points': [114, 96, 433, 413]}], [{'name': 'person', 'percentage_probability': 95.40123343467712, 'box_points': [113, 99, 432, 410]}], [{'name': 'tv', 'percentage_probability': 98.07203412055969, 'box_points': [28, 69, 387, 332]}]], [{'person': 2}, {'person': 2}, {'person': 2}, {'person': 2}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'tv': 1}], {'person': 1, 'tv': 0}),
                          (15, [[{'name': 'tv', 'percentage_probability': 98.32988977432251, 'box_points': [27, 68, 384, 333]}], [{'name': 'tv', 'percentage_probability': 98.44536185264587, 'box_points': [26, 67, 383, 334]}], [{'name': 'tv', 'percentage_probability': 97.14498519897461, 'box_points': [26, 70, 385, 331]}], [{'name': 'tv', 'percentage_probability': 97.68345952033997, 'box_points': [26, 70, 384, 331]}], [{'name': 'tv', 'percentage_probability': 97.96280264854431, 'box_points': [26, 68, 384, 333]}], [{'name': 'tv', 'percentage_probability': 97.71825075149536, 'box_points': [28, 68, 383, 332]}], [{'name': 'tv', 'percentage_probability': 98.04017543792725, 'box_points': [28, 69, 385, 331]}], [{'name': 'tv', 'percentage_probability': 98.15681576728821, 'box_points': [29, 68, 382, 333]}], [{'name': 'tv', 'percentage_probability': 98.00386428833008, 'box_points': [29, 68, 379, 332]}], [{'name': 'tv', 'percentage_probability': 97.39431142807007, 'box_points': [28, 68, 380, 332]}], [{'name': 'tv', 'percentage_probability': 97.76583909988403, 'box_points': [28, 69, 380, 332]}], [{'name': 'tv', 'percentage_probability': 97.28885889053345, 'box_points': [26, 69, 379, 331]}], [{'name': 'person', 'percentage_probability': 89.08666968345642, 'box_points': [103, 57, 342, 254]}], [{'name': 'person', 'percentage_probability': 89.99555110931396, 'box_points': [104, 59, 342, 254]}]], [{'tv': 1}, {'tv': 1}, {'tv': 1}, {'tv': 1}, {'tv': 1}, {'tv': 1}, {'tv': 1}, {'tv': 1}, {'tv': 1}, {'tv': 1}, {'tv': 1}, {'tv': 1}, {'person': 1}, {'person': 1}], {'tv': 0, 'person': 0}),
                          (16, [[{'name': 'person', 'percentage_probability': 91.16752743721008, 'box_points': [106, 58, 342, 256]}], [{'name': 'person', 'percentage_probability': 91.03465676307678, 'box_points': [104, 58, 342, 255]}], [{'name': 'person', 'percentage_probability': 91.3987398147583, 'box_points': [109, 60, 340, 259]}], [{'name': 'person', 'percentage_probability': 90.50254225730896, 'box_points': [109, 60, 340, 259]}], [{'name': 'person', 'percentage_probability': 86.52979135513306, 'box_points': [107, 60, 341, 257]}], [{'name': 'person', 'percentage_probability': 85.43699383735657, 'box_points': [109, 60, 340, 256]}], [{'name': 'person', 'percentage_probability': 86.89377307891846, 'box_points': [111, 61, 337, 255]}], [{'name': 'person', 'percentage_probability': 95.10414004325867, 'box_points': [18, 55, 426, 386]}], [{'name': 'person', 'percentage_probability': 94.16747689247131, 'box_points': [16, 55, 431, 387]}], [{'name': 'person', 'percentage_probability': 93.99626851081848, 'box_points': [17, 57, 428, 385]}], [{'name': 'person', 'percentage_probability': 94.18757557868958, 'box_points': [20, 58, 427, 384]}], [{'name': 'person', 'percentage_probability': 94.26366090774536, 'box_points': [20, 56, 427, 385]}], [{'name': 'person', 'percentage_probability': 93.4090256690979, 'box_points': [17, 54, 433, 391]}], [{'name': 'person', 'percentage_probability': 94.66513395309448, 'box_points': [16, 53, 433, 391]}, {'name': 'tie', 'percentage_probability': 54.82523441314697, 'box_points': [157, 291, 293, 365]}]], [{'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1}, {'person': 1, 'tie': 1}], {'person': 1, 'tie': 0})]

print(output_Collection_temp)


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



output_dic_reformated, reformat_frame_second = reformat_ouput(output_Collection_temp)


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

processed_array = object_occurrence_within_second_frame(output_dic_reformated)


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


final_dic_output = final_intent_reformat(processed_array)

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

update_accuracy_with_area = object_occurrence_within_second_frame_accuracy_avgArea_avgAcc(output_dic_reformated)


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


final_dic_output_acc = final_intent_reformat_acc(update_accuracy_with_area)

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


final_dic_output_area = final_intent_reformat_area(update_accuracy_with_area)

def quality_score_attempt_version2(updated_arry):
    score_arry = []
    attempt_score = 10 #could be changeds
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
