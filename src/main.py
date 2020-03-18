import sys
import os
import json
from datetime import datetime, timedelta

# export CORONA='/Users/foufamastafa/Documents/micro_projects/corona_virus'
assert os.environ.get('CORONA'), 'Please set the environment variable CORONA'
CORONA = os.environ['CORONA']
DATA_PATH = CORONA + "/data/"
IMAGES_PATH = DATA_PATH + "images/"
DATAFRAME_PATH = DATA_PATH + "dataframe/"
CONFIG_PATH = CORONA + "/config/"
sys.path.append(CORONA + '/data/')
sys.path.append(CORONA + '/utils/')

from update_dashboard import update_dashboard
import time

delay = 0
max_nb_files = 1

print('Run something..')
dt = datetime.now() + timedelta(hours=12)

while datetime.now() < dt:
    with open(CONFIG_PATH + 'config.json') as json_file:
        config = json.load(json_file)
        for webcam in config['webcams']:

            #print(webcam['url'],webcam['city'],webcam['country'],webcam['id'],delay,max_nb_files)

            update_dashboard(url = webcam['url'], city = webcam['city'], country = webcam['country'], zone_id = webcam['id'], delay = delay, max_nb_files = max_nb_files)

    time.sleep(120)
        
