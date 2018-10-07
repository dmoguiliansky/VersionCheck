# import deepDiff
# from pprint import pprint

original_dict_path = 'C:\\Users\Dor Moguiliansky\PycharmProjects\VersionCheckDogma\AAPL_W_stt3_backup_1.ini'
test_dict_path = 'C:\\Users\Dor Moguiliansky\PycharmProjects\VersionCheckDogma\AAPL_W_stt4_backup_1.ini'

original_dictionary = {}
test_dictionary = {}

def compare_dictionaries(original_dictionary, test_dictionary):
    global original_values, test_values
    original_dictionary = open(original_dictionary, 'r')
    original_dictionary_lines = original_dictionary.readlines()
    test_dictionary = open(test_dictionary, 'r')
    test_dictionary_lines = test_dictionary.readlines()
    original_dictionary.close()
    test_dictionary.close()
    for original_line in original_dictionary_lines[1:]:
        split_line = original_line.split('=')
        original_values = split_line[1]
        for test_line in test_dictionary_lines[1:]:
            split_line = test_line.split('=')
            test_values = split_line[1]

        # for test_line in test_dictionary_lines[1:]:
        #     test_values = test_line.split()
        #     for original_line in original_values:
        #             for test_line in test_values:
        #                 if original_line != test_line:
        #                     print('value has changed from', original_line, 'to', test_line)
        #                 else:
        #                     print('all good')

    # for test_line in test_dictionary_lines[1:]:
    #     splitLine = test_line.split("=")
    #     test_values = splitLine[1]
    #     # print(test_values)
    # for original_value in original_values:
    #     for test_value in test_values:
    #         if original_value != test_value:
    #             print('value has changed from', original_value, 'to', test_value)
    #         else:
    #             print('all good')

    # for test_line in test_dictionary_lines[1:]:
    #     splitLine = test_line.split("=")
    #     test_values = splitLine[1]
    #     return test_values
    #  if test_values != original_values:
    #      print('the value has changed from', original_values,'to',test_values)
    #  else:
    #      print('all good')
# for test_line in test_dictionary_lines[1:]:
    #     splitLine = test_line.split("=")
    #     test_values = splitLine[1]
    # print(original_values)
    # if original_values != test_values:
    #     print('the value has changed from', original_values,'to',test_values)
    # else:
    #     print('all good!')

compare_dictionaries(original_dict_path, test_dict_path)

    # for original_line in original_dictionary_lines:
    #     for test_line in test_dictionary_lines:
    #         if original_line != test_line:
    #             print(original_line,'has changed to', test_line)


    # print(test_dictionary_lines,original_dictionary_lines)
    # for line in original_dictionary_lines, test_dictionary_lines:
    #         split_line = line.(":")
    #         split_line[0] = split_line[1]
    #         original_values = original_dictionary_lines[split_line[1]]
    #         test_values = test_dictionary_lines[split_line[1]]
    #         if original_values != test_values:
    #             print('We have a problem')
    #         else:
    #             print('We have a match')

#
#
#
# file1 = open(file1path, 'r')
# file1Lines = file1.readlines()
# file1.close
#
#
# file1Dict = {}
#
# for line in dict1[1:]:
#     splitLine = dict1.split("=")
#     dict1[splitLine[0]] = splitLine[1]
#
# file2Dict = {}
#
# differenceDict = {}
# for key in file1Dict.keys():
#     if file2Dict.keys():
#         if file1Dict[key] == file2Dict[key]:
#             Do
#             something
#         else:
#             differenceDict[filePath][key] = "change from x to y"
# # compare_dictionaries(get_dict_from_ini(a),dict2)
#
#
# dict1 = {
#     "DetailedLog:2",
#     "RunStatus:1",
#     "StatusPort:7000",
#     "Archive:1",
#     "Version:0.9",
#     "RunFTP:1",
#     "FTPPort:21",
#     "FTPDataPort:30",
# }
#
# dict2 = {
#     "DetailedLog:2",
#     "RunStatus:1",
#     "StatusPort:6090",
#     "Archive:1",
#     "Version:0.9",
#     "RunFTP:1",
#     "FTPPort:21",
#     "FTPDataPort:20",
# }
#
# for key in dict1:
#     print()
#     print(dict1)