"""

Just for testing the scheduler in Github

"""
import os, sys
assert os.environ.get('CORONA'), 'Please set the environment variable CORONA'
CORONA = os.environ['CORONA']
DATA_PATH = CORONA + "/data/"
with open(DATA_PATH+"test.txt", 'w') as f:
    txt = "hey toto, we are testing Github scheduler"
    txt_bis = "hey tata, we are testing Github scheduler"
    f.write(txt + "\n")
    f.write(txt_bis + "\n")
