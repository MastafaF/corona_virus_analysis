"""
This file aims to count person in a image given its path.
It uses OpenCV implementation of YOLO
"""

import numpy as np
import cv2
import os
import sys

#  $Env:CORONA = "C:\Users\Quentin\Desktop\corona_virus_analysis"
assert os.environ.get('CORONA'), 'Please set the environment variable CORONA'
CORONA = os.environ['CORONA']
CONFIG_PATH = CORONA + "/config/"
WEIGHTS_PATH = CORONA + "/weights/"
sys.path.append(CORONA + '/data/')


def count_person(path):
    """
    arg: path is the path of an image jpg file
    return: the number of identified person in the image
    """
    
    #init counter
    count_person = 0
    
    # Loading image
    img = cv2.imread(path)

    # desired size
    dsize = (640, 480)
    img = cv2.resize(img, dsize)
    height, width, channels = img.shape

    # Load Yolo
    net = cv2.dnn.readNet(WEIGHTS_PATH + "yolov3.weights",WEIGHTS_PATH + "yolov3.cfg")
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    
    
    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, dsize, (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    #extract person detected
    for out in outs:
        for detection in out:
            # the score associated to person object is at index 5
            score_person = detection[5]
            if score_person > 0.5:
                # Object detected
                count_person += 1
    
    return count_person

