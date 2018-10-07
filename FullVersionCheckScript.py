import rarfile
import configparser
import os

rarfile.UNRAR_TOOL = 'C:\Program Files\WinRAR\\UnRAR.exe'  # A default code for rar file module
rarfile.PATH_SEP = '\\'

b = 'AAPL_Backup_20.02.12_Ini.rar'
# Open a .rar file


def get_files_from_rar_file(rar_path):
    original_rar = rarfile.RarFile(rar_path)
    for file in original_rar.infolist():
        print(file.filename)

# get_files_from_rar_file(b)


directory = "C:\\Users\Dor Moguiliansky\PycharmProjects\VersionCheckDogma"
extention = 'ini'


# Search in folder for all the files with same extension
def get_all_files_with_same_extension(files_path, ext):
    result = []
    for root, dirs, files in os.walk(files_path):
        for f in files:
            if f.endswith("."+ext):
                result.append(os.path.join(root, f))
    # return result
    print(result)



# get_all_files_with_same_extension(directory, extention)
a = 'C:\\Users\Dor Moguiliansky\PycharmProjects\VersionCheckDogma\AAPL_W_stt1_backup_1.ini'


# Take an ini file and return a dictionary
def get_dict_from_ini(ini_path):
    config = configparser.ConfigParser()
    config.optionxform = str                # preserve case
    config.read(ini_path)                    # read ini file
    out_dict = dict(config._sections)        # create dictionary
    for iniKey in out_dict:
        out_dict[iniKey] = dict(config._defaults, **out_dict[iniKey])
        out_dict[iniKey].pop('__name__', None)
    return out_dict

get_dict_from_ini(a)

#
# def compare_dictionaries(original_dictionary, test_dictionary):
#     dict_original_values = []
#     dict_test_values = []
#     for line in test_dictionary:
#         for line in original_dictionary:
#             split_line = line.split(":")
#             split_line[0] = split_line[1]
#             dict_test_values = split_line[1]
#             if dict_original_values != dict_test_values:
#                 print('We have a problem')
#             else:
#                 print('We have a match')
#
#             # print(dict_test_values)
#         return dict_test_values


def compare_dictionaries(dict1, dict2):
    if dict1 is None or dict2 is None:
        print('Nones')
        return False

    if (not isinstance(dict1, dict)) or (not isinstance(dict2, dict)):
        print('Not dict')
        return False

    shared_keys = set(dict2.keys()) & set(dict2.keys())

    if not (len(shared_keys) == len(dict1.keys()) and len(shared_keys) == len(dict2.keys())):
        print('Not all keys are shared')
        return False

    dicts_are_equal = True
    for key in dict1.keys():
        if isinstance(dict1[key], dict) or isinstance(dict2[key], dict):
            dicts_are_equal = dicts_are_equal and compare_dictionaries(dict1[key], dict2[key])
        else:
            dicts_are_equal = dicts_are_equal and all(atleast_1d(dict1[key] == dict2[key]))

    return dicts_are_equal


# compare_dictionaries(dict1,dict2)