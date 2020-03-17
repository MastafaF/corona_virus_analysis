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
IMAGES_PATH = DATA_PATH + "images/"
sys.path.append(CORONA + '/data/')

from PIL import Image
import requests
import matplotlib.pyplot as plt
import numpy as np



URL = 'http://83.140.123.184/ImageHarvester/Images/copyright!-stureplan_1_live.jpg?counter=1584452098949'

def get_image(url = URL, save = False):
    """
    :param url: str
    :return: numpy array correspond to the image, time the request is sent

    # @TODO: get country and town
    """
    # SENT GET REQUEST TO SERVER
    response = requests.get(url=URL, stream=True)
    # GET IMAGE IN REQUEST
    img = Image.open(response.raw)
    # SAVE IMAGE IN DIR
    img_arr = np.array(img)  # shape (480, 640, 3)
    time_now_str = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
    if save:
        np.save(arr=img_arr, file=IMAGES_PATH + 'Sweden%Stockholm%' + time_now_str)

    return img_arr, time_now_str