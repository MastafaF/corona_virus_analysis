"""
Updating a plot live
"""
import sys
import os
import pandas as pd
from pathlib import Path
import shutil

# export CORONA='/Users/foufamastafa/Documents/micro_projects/corona_virus'
assert os.environ.get('CORONA'), 'Please set the environment variable CORONA'
CORONA = os.environ['CORONA']
DATA_PATH = CORONA + "/data/"
IMAGES_PATH = DATA_PATH + "images/"
DATAFRAME_PATH = DATA_PATH + "dataframe/"
sys.path.append(CORONA + '/data/')
sys.path.append(CORONA + '/utils/')

from get_online_data import get_image
from update_data import update_data
import time


def get_nb_files_in_dir(dir_name = IMAGES_PATH):
    arr_files = os.listdir(dir_name)
    nb_files = len(arr_files)
    return nb_files

# Number of images to gather before converting images into data
MAX_NB_FILES = 10



# For each URL, we have the correponding city, town in config
URL = 'http://83.140.123.184/ImageHarvester/Images/copyright!-overtornea_1_live.jpg'

def update_dashboard(url = URL, city = 'stockolm', country = 'sweden', zone_id = 0, delay = 0, max_nb_files = MAX_NB_FILES):
    counter = 0
    #Check if directory exist
    if not Path(IMAGES_PATH).exists():
        os.makedirs(IMAGES_PATH)

    while get_nb_files_in_dir() < max_nb_files:
        _, _ = get_image(url, city, country, zone_id, True)
        counter += 1
        time.sleep(delay)

    # And then when counter is a multiple of 12 ie after every hour, add that information to dataframe
    # By updating data with utils/update_data.py
    # @TODO: launch exec update_data.py instead of redoing it here ...
    # if we get data every 5 mins and we want to update our dataframe every 60 mins,
    # then FACTOR_HOURS = 60/5 = 12
    csv_file = DATAFRAME_PATH + "df_data.tsv"

    df = update_data(dir_name = IMAGES_PATH)

    if Path(csv_file).exists():
        # concatenate old df with new df
        old_df = pd.read_csv(csv_file, parse_dates=True, sep='\t')
        df = pd.concat([old_df, df], sort=True)
        # empty directory

        #shutil.rmtree(IMAGES_PATH)
        ## create directory again
        #os.makedirs(IMAGES_PATH)

        filelist = [ f for f in os.listdir(IMAGES_PATH) if f.endswith(str(zone_id) + ".jpeg") ]
        for f in filelist:
            os.remove(os.path.join(IMAGES_PATH, f))



    df = df.set_index('datetime').fillna(0)

    df.sort_values(by=['datetime'], inplace=True)
    df.to_csv(csv_file, sep='\t')

        