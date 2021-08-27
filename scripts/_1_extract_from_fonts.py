from consts import *
import fontforge
import os


def get_font_folder_url(font_name):
    return IMAGES_FOLDER + font_name + "/"


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def extract_images_from_font(font_name):
    font = fontforge.open(FONTS_FOLDER + font_name)

    for font_key in font:
        if not font_key in unicode_map.keys():
            #print("-- font_key " + font_key + " don't exist on map. if is an hiragana/katakana, needs to set it")
            continue

        #print(font_key, " ", unicode_map[font_key])
        full_path = get_font_folder_url(font_name) + unicode_map[font_key] + "." + IMAGE_EXTENSION_FILE
        if os.path.exists(full_path):
            #print("-- file " + full_path + " exist")
            continue

        glyph = font[font_key]
        glyph.export(full_path)
        glyph.export(full_path, INIT_SQUARE_SIZE)
    font.close()


create_folder(IMAGES_FOLDER)

for font_name in fonts_names:
    print("\n\n=== " + font_name)
    try:
        create_folder(get_font_folder_url(font_name))
        extract_images_from_font(font_name)
    except Exception as e:
        print("++ error ocurred in file " + font_name)
        print(e)
