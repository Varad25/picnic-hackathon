from __future__ import absolute_import, division, print_function
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import os
from shutil import copyfile

# Helper libraries
import numpy as np


train_data = np.genfromtxt('train.tsv', dtype=(str, str),delimiter='\t', skip_header=1)

labels = list(set(map(lambda x: x[1], train_data)))
labels.sort()
images = list(map(lambda x:x[0], train_data))

all_image_labels = [[image[0], image[1].replace(' ', '_')]
                    for image in train_data]

for images in all_image_labels:
    dest_fpath = "data/{}/{}".format(images[1], images[0])
    os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)
    copyfile("train/{}".format(images[0]),dest_fpath)

print("copied")

# def get_size_statistics(DIR):
#   heights = []
#   widths = []
#   for img in os.listdir(DIR): 
#     path = os.path.join(DIR, img)
#     data = np.array(Image.open(path)) #PIL Image library
#     heights.append(data.shape[0])
#     widths.append(data.shape[1])
#   avg_height = sum(heights) / len(heights)
#   avg_width = sum(widths) / len(widths)
#   print("Average Height: " + str(avg_height))
#   print("Max Height: " + str(max(heights)))
#   print("Min Height: " + str(min(heights)))
#   print('\n')
#   print("Average Width: " + str(avg_width))
#   print("Max Width: " + str(max(widths)))
#   print("Min Width: " + str(min(widths)))

# get_size_statistics("train")