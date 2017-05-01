from config import *
import os
import sys

# prepare for usearch
os.mkdir(uploadPath()+'/BBH')
os.mkdir(uploadPath()'/results')

remArgs = ' '+sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '

# usearch build
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_build.py'+remArgs)

# usearch multi
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_multi.py'+remArgs)

# parse multiple usearch
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_build.py'+remArgs)

# getcore

# launch mafft

# concat85

# Raxml distance

# sample.py

# calcHM

# graph

