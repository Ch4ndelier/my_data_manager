import json
import os
import cv2
import numpy as np


def load_config():
    with open("config/process.json") as f:
        config = json.load(f)
    return config


def get_img_list(path):
    img_path_list = []
    img_name_list = []
    for filename in os.listdir(path):
        print(os.path.join(path, filename))
        img_name_list.append(filename)
        img_path_list.append(os.path.join(path, filename))
    return list(zip(img_path_list, img_name_list))
