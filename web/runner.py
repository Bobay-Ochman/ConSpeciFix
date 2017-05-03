from config import *
import os
import sys

# prepare for usearch
os.mkdir(uploadPath()+'/genes')
	#Need to also probably fill this folder with the genes we find here???
os.mkdir(uploadPath()+'/BBH')
os.mkdir(uploadPath()'/results')

remArgs = ' '+sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '

# usearch
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_build.py'+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_multi.py'+remArgs)

# parse multiple usearch
os.system('python '+ PATH_TO_SCRIPTS + 'parse_multiple_usearch.py'+remArgs)

# MCL
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mcl.py'+remArgs)

# getcore
os.system('python '+ PATH_TO_SCRIPTS + 'get_core.py'+remArgs)

# launch mafft
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mafft_build.py'+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mafft_multi.py'+remArgs)

# concat85
os.system('python '+ PATH_TO_SCRIPTS + 'concat85.py'+remArgs)

# Raxml distance
os.system('python '+ PATH_TO_SCRIPTS + 'raxml_distance.py'+remArgs)

# sample.py
os.system('python '+ PATH_TO_SCRIPTS + 'sample.py'+remArgs)

# calcHM
os.system('python '+ PATH_TO_SCRIPTS + 'calcHM.py'+remArgs)

# graph
os.system('python '+ PATH_TO_SCRIPTS + 'graph.py'+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'big_graph.py'+remArgs)
os.system('Rscript '+ uploadPath() + 'big_graph.R'+remArgs)

