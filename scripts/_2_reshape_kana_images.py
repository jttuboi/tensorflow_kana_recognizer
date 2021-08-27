from consts import *
from PIL import Image
import PIL.ImageOps
import glob


def get_all_filanames():
    return glob.glob(IMAGES_FOLDER + "*/*." + IMAGE_EXTENSION_FILE)


def resize(image, filename):
    x, y = image.size
    # if the image is greater, needs to resize to INIT_SQUARE_SIZE
    if x > INIT_SQUARE_SIZE+1 or y > INIT_SQUARE_SIZE+1:
        #print("%s (%d, %d)"%(filename,x, y))
        image.thumbnail((INIT_SQUARE_SIZE, INIT_SQUARE_SIZE), Image.ANTIALIAS)
        x, y = image.size
    # create a new image with FINAL_SQUARE_SIZE and add the kana image in the middle of this new image.
    resized_image = Image.new('RGBA', (FINAL_SQUARE_SIZE_X, FINAL_SQUARE_SIZE_Y), BACKGROUND_COLOR)
    resized_image.paste(image, (int((FINAL_SQUARE_SIZE_X - x) / 2), int((FINAL_SQUARE_SIZE_Y - y) / 2)))
    return resized_image


for filename in get_all_filanames():
    print("=== " + filename)
    image = Image.open(filename)
    resized_image = resize(image, filename)
    resized_image.save(filename, format=IMAGE_EXTENSION_FILE)


###############################################################################
# if you want to use background black and strokes white
###############################################################################

#BACKGROUND_COLOR = (0, 0, 0, 255) # black

#def invert_color(image):
#    return PIL.ImageOps.invert(image)

#for filename in get_all_filanames():
#    print("=== " + filename)
#    image = Image.open(filename).convert('RGB')
#    color_inverted_image = invert_color(image)
#    resized_image = resize(color_inverted_image, filename)
#    resized_image.save(filename, format=IMAGE_EXTENSION_FILE)
