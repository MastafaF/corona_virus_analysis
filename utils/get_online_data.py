"""

This file aims to get the data every n-period from
 http://83.140.123.184/ImageHarvester/Images/copyright!-stureplan_1_live.jpg?counter=1584452098949

 The goal is to add images from this website every t seconds as long as Number_Files < MAX_NB_FILES
"""



import os
import sys
from datetime import datetime
import time



# export CORONA='/Users/foufamastafa/Documents/micro_projects/corona_virus'
assert os.environ.get('CORONA'), 'Please set the environment variable CORONA'
CORONA = os.environ['CORONA']
DATA_PATH = CORONA + "/data/"
sys.path.append(CORONA + '/data/')

from PIL import Image
import requests
import matplotlib.pyplot as plt
import numpy as np

#
# list = os.listdir(dir) # dir is your directory path
# number_files = len(list)
# print number_files

MAX_NB_FILES = 10

def get_nb_files_in_dir(dir_name = DATA_PATH):
    arr_files = os.listdir(dir_name)
    nb_files = len(arr_files)
    return nb_files

URL = 'http://83.140.123.184/ImageHarvester/Images/copyright!-stureplan_1_live.jpg?counter=1584452098949'
while get_nb_files_in_dir() < MAX_NB_FILES:
    # SENT GET REQUEST TO SERVER
    response = requests.get(url=URL, stream=True)

    # GET IMAGE IN REQUEST
    img = Image.open(response.raw)
    # SAVE IMAGE IN DIR
    img_arr = np.array(img) # shape (480, 640, 3)
    time_now_str = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
    np.save(arr=img_arr, file=DATA_PATH+'img-'+time_now_str)
    # process should sleep during 1 sec
    time.sleep(1)
