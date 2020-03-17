"""
Given country, place, time, file_path, nb_people_detected

We add that to our curent dataframe and save it

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

csv_file = DATAFRAME_PATH + "df_data.tsv"

def get_features_from_filename(filename):
    arr_features = filename.split("%")
    country, city, time = arr_features[0], arr_features[1], arr_features[2]
    return country, city, time


def get_nb_people(filename):
    pass


def update_data(dir_name = IMAGES_PATH):
    # iterate over the directory and get all filenames
    arr_filenames = os.listdir(dir_name)
    arr_country = [get_features_from_filename(filename)[0] for filename in arr_filenames]
    arr_city = [get_features_from_filename(filename)[1] for filename in arr_filenames]
    arr_time = [get_features_from_filename(filename)[2] for filename in arr_filenames]

    # for each filenames get number of people detected by Yolov
    arr_nb_detected = [get_nb_people(filename) for filename in arr_filenames]

    df = pd.DataFrame( )
    df['country'] = arr_country
    df['city'] = arr_city
    df['time'] = arr_time
    return df

df = update_data(dir_name = IMAGES_PATH)

if Path(csv_file).exists():
    # concatenate old df with new df
    old_df = pd.read_csv(csv_file, parse_dates=True)
    df = pd.concat([old_df, df], sort=True)
    # empty directory
    shutil.rmtree(IMAGES_PATH)

df = df.set_index('datetime').fillna(0)

df.sort_values(by=['datetime'], inplace=True)




