from config import *
from mailMessage import *
import os
import sys



remArgs = 'Lactobacillus_crispatus upload_26be13b7688a4e52730c30de41f6bb77 1494943962497 brian.ellis@austin.rr.com'
remArgs = str(remArgs)

print "------ parse usearch"
# parse multiple usearch
os.system('python '+ PATH_TO_SCRIPTS + 'distrib.py '+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'kmean.py '+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'split_kmean.py '+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'criterion.py '+remArgs)

