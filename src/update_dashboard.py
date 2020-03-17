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

MAX_NB_FILES = 10

def get_nb_files_in_dir(dir_name = IMAGES_PATH):
    arr_files = os.listdir(dir_name)
    nb_files = len(arr_files)
    return nb_files

counter = 0
# Get image every 5 minutes
# For each URL, we have the correponding city, town in config
URL = 'http://83.140.123.184/ImageHarvester/Images/copyright!-stureplan_1_live.jpg?counter=1584452098949'
while get_nb_files_in_dir() < MAX_NB_FILES:
    _, _ = get_image(url = URL, save = True)
    counter += 1
    time.sleep(5)

# And then when counter is a multiple of 12 ie after every hour, add that information to dataframe
# By updating data with utils/update_data.py
# @TODO: launch exec update_data.py instead of redoing it here ...
# if we get data every 5 mins and we want to update our dataframe every 60 mins,
# then FACTOR_HOURS = 60/5 = 12
FACTOR_HOURS = 5
csv_file = DATAFRAME_PATH + "df_data.tsv"
if counter % FACTOR_HOURS == 0:
    df = update_data(dir_name = IMAGES_PATH)

    if Path(csv_file).exists():
        # concatenate old df with new df
        old_df = pd.read_csv(csv_file, parse_dates=True, sep='\t')
        df = pd.concat([old_df, df], sort=True)
        # empty directory
        shutil.rmtree(IMAGES_PATH)
        # create directory again
        os.makedirs(IMAGES_PATH)


    df = df.set_index('datetime').fillna(0)

    df.sort_values(by=['datetime'], inplace=True)
    df.to_csv(csv_file, sep='\t')

    print(df)