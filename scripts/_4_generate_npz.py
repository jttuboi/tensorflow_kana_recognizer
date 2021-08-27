from consts import *
from PIL import Image
import PIL.ImageOps
from tensorflow.keras.preprocessing import image as keras_image
import os
import glob
import numpy as np


def kana_prefix(kana):
    HIRAGANA_PREFIX = "1" # folder is 1XX
    KATAKANA_PREFIX = "2" # folder is 2XX
    return HIRAGANA_PREFIX if (kana == HIRAGANA) else KATAKANA_PREFIX


def get_folder_names(kana):
    folder_names = os.listdir(IMAGES_READY_FOLDER)
    folder_names.sort()
    
    folder_names_filtered = []
    for folder_name in folder_names:
    	if folder_name.startswith(kana_prefix(kana)):
    	    folder_names_filtered.append(folder_name)
    return folder_names_filtered


# the quantity of sample images MUST be equals for all kanas
# so you can use the first folder to find the quantity of samples
def calculate_samples_quantity(folder_path):
    return len(glob.glob(folder_path + "/*."+IMAGE_EXTENSION_FILE))


def convert_to_npz(kana):
    print("--- "+kana)
    
    folder_names = get_folder_names(kana)

    kana_quantity = len(folder_names)
    samples_quantity = calculate_samples_quantity(IMAGES_READY_FOLDER + folder_names[0]) # only look the first folder
    print("%d %d"%(kana_quantity, samples_quantity))

    final_image_array = np.zeros([kana_quantity, samples_quantity, FINAL_SQUARE_SIZE_Y, FINAL_SQUARE_SIZE_X], dtype=np.uint8)

    kana_idx = 0
    for folder_name in folder_names:
        folder_path = IMAGES_READY_FOLDER + folder_name
        #print("%s | %s"%(folder_name, folder_path))
        image_names = os.listdir(folder_path)

        sample_idx = 0
        for image_name in image_names:
            image_path = folder_path + "/" + image_name
            #print("%s | %s"%(image_name, image_path))

            # read image and convert to image array
            image = Image.open(image_path).convert('RGB')
            image = PIL.ImageOps.invert(image)
            image = image.convert("L")
            
            # other way to read image
            #image = keras_image.load_img(image_path, color_mode="grayscale")
            #image_array = keras_image.img_to_array(image, data_format="channels_first")#, dtype=np.uint8)
            
            #print(image)
            final_image_array[kana_idx, sample_idx] = np.array(image)
            image.close()
            #print("%s k(%d/%d) s(%d/%d) (%d %d %d)"%(image_path, kana_idx, kana_quantity, sample_idx, samples_quantity, len(image_array), len(image_array[0]), len(image_array[0][0])))
            
            sample_idx += 1
        kana_idx += 1

    #print(final_image_array)
    np.savez_compressed(kana + ".npz", final_image_array)



print("=== generate npz started")
convert_to_npz(HIRAGANA)
#convert_to_npz(KATAKANA)
print("=== generate npz ended")
