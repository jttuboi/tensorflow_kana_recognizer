from PIL.Image import EXTENSION
from consts import *
import glob
import os
import shutil


def get_old_folders():
    return glob.glob(IMAGES_FOLDER + "*")


def get_old_files_path(folder):
    return glob.glob(folder + "/*."+IMAGE_EXTENSION_FILE)


def get_new_folder_path(full_path):
    return IMAGES_READY_FOLDER + os.path.basename(full_path)[:-len("." + IMAGE_EXTENSION_FILE)]


def get_new_full_path(new_folder_path, new_filename):
    return new_folder_path + "/" + new_filename + "." + IMAGE_EXTENSION_FILE


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def clean_images_folder():
    shutil.rmtree(IMAGES_FOLDER)



print("=== organize started")
create_folder(IMAGES_READY_FOLDER)

counter_folder = 0
for folder in get_old_folders():
    for old_full_path in get_old_files_path(folder):
        new_folder_path = get_new_folder_path(old_full_path)
        create_folder(new_folder_path)
        new_full_path = get_new_full_path(new_folder_path, str(counter_folder))
        #print("%d/%d"%(old_full_path, new_full_path))
        shutil.move(old_full_path, new_full_path)
    counter_folder += 1

clean_images_folder()
print("=== organize finished")