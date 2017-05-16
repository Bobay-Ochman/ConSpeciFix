from config import *
from mailMessage import *
import os
import sys



remArgs = ['Lactobacillus_crispatus', 'upload_dd21c82a729bdfe702e443b3320504d1', '1494887021656', 'brian.ellis@austin.rr.com']

print "------ parse usearch"
# parse multiple usearch
os.system('python '+ PATH_TO_SCRIPTS + 'distrib.py'+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'kmeans.py'+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'split_kmeans.py'+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'criterion.py'+remArgs)

