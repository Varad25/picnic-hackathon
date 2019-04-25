import Augmentor


# Helper libraries
import numpy as np
import os, os.path



train_data = np.genfromtxt('train.tsv', dtype=(str, str),delimiter='\t', skip_header=1)
path_to_data = "augmented_data/Fish"
labels = list(set(map(lambda x: x[1].replace(' ', '_'), train_data)))


for label in labels:
    path_to_data = "augmented_data/{}".format(label)
    p = Augmentor.Pipeline(path_to_data, output_directory="")

    p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
    p.rotate_random_90(probability=0.3)
    p.crop_random(probability=0.5, percentage_area=0.10)
    # simple version for working with CWD
   
    no_of_files = len([name for name in os.listdir(path_to_data)])
    print("{}: {}".format(label, no_of_files))
    p.sample(no_of_files * 3)

