import os

from utils import Utils
from read_file import ReadFile
from downloader import Downloader

"""DOWNLOAD_PRENAME = "lav-25"
SAVE_DIR = DOWNLOAD_PRENAME + "/"
FILE_PATH = DOWNLOAD_PRENAME + ".txt"
MODE = "64"
"""

URL_DICT = "url_dict.txt"

util_obj = Utils()  # object for utility functions such as getting names
file_obj = ReadFile()  # object to get urls
download_obj = Downloader()  # object to download images

folder_list = file_obj.create_couples(URL_DICT)

for couple in folder_list:
    prename, mode = couple[0], couple[1]
    util_obj.make_directory(prename)
    save_dir, file_path = file_obj.read_from_couple(prename)

    urls = file_obj.read_txt_lines("urls/" + file_path)

    for line in urls:
        dump_line = util_obj.replace_names(line)
        print(dump_line)
        save_name = save_dir + util_obj.get_names(dump_line, mode=mode)
        download_obj.download_image(dump_line, save_name, mode=mode)

    download_obj.final_info()

del dump_line
del save_name
del util_obj
del file_obj
del download_obj


"""util_obj.make_directory(DOWNLOAD_PRENAME)

urls = file_obj.read_txt_lines()

for line in urls:
    dump_line = util_obj.replace_names(line)
    print(dump_line)
    save_name = SAVE_DIR + util_obj.get_names(dump_line, mode=MODE)
    download_obj.download_image(dump_line, save_name, mode=MODE)

download_obj.final_info()  # get final info on the downloads

# release memory
del dump_line
del save_name
del util_obj
del file_obj
del download_obj
"""
