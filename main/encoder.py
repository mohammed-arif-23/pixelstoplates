import os
import tensorflow as tf
import numpy as np
import pickle
import re
from scipy.spatial.distance import cosine

model = tf.keras.applications.DenseNet201(include_top=False, weights='imagenet',
                                          input_shape=(256, 256, 3), pooling='avg', classes=1000)

current_dir = os.path.dirname(__file__)

encodings_path = os.path.join(current_dir, '..', 'encodings.txt')
enc_names_path = os.path.join(current_dir, '..', 'enc_names.txt')

with open(encodings_path, 'rb') as fp:
    enc_list = pickle.load(fp)
    enc_list = np.array(enc_list) 
with open(enc_names_path, 'rb') as fp:
    names_list = pickle.load(fp)
def get_encodings(img):
   
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.keras.preprocessing.image.smart_resize(
    img_array, size=(256, 256))
    img_array = np.expand_dims(img_array, axis=0)
    img_preprocessed = tf.keras.applications.densenet.preprocess_input(
        img_array)

    encoding = model.predict(img_preprocessed)
    encoding = encoding.flatten()
    return encoding
def get_recipes(img):
    enc = get_encodings(img)
    similarity_list = []
    recipe_names_list = []
    print("Shape of enc_list:", enc_list.shape) 
    print("Shape of enc:", enc.shape)  
    for i in range(len(enc_list)):
        similarity = cosine(enc_list[i].flatten(), enc.flatten())
        similarity_list.append(1 - similarity)
    sorted_list = sorted(zip(similarity_list, names_list), reverse=True)

    for i in range(len(sorted_list)):
        name_in_list = sorted_list[i][1]
        s = re.sub(r'[0-9]+.jpg', "", name_in_list)
        if s not in recipe_names_list:
            recipe_names_list.append(s) 
            if len(recipe_names_list) >= 11:
                break

    return recipe_names_list
