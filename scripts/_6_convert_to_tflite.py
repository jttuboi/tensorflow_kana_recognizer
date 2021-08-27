import tensorflow as tf
from consts import *


def convert_to_tlite(kana):
    print("--- "+kana)
    
    converter = tf.lite.TFLiteConverter.from_saved_model(kana + MODEL_FOLDER)
    tflite_model = converter.convert()

    with open(kana + TFLITE_EXTENSION, "wb") as f:
        f.write(tflite_model)



print("=== convert to tflite started")
convert_to_tlite(HIRAGANA)
#convert_to_tlite(KATAKANA)
print("=== convert to tflite ended")
