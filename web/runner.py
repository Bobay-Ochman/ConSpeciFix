from config import *
import os
import sys

# make folders
try:
	os.mkdir(PATH_TO_UPLOAD+'todo')
except OSError as e:
	print e
	#Need to also probably fill this folder with the genes we find here???
try:
	os.mkdir(PATH_TO_UPLOAD+'BBH')
except OSError as e:
	print e
try:
	os.mkdir(PATH_TO_UPLOAD+'results')
except OSError as e:
	print e
try:
	os.mkdir(PATH_TO_UPLOAD+'align')
except OSError as e:
	print e

print "------ made folders"

remArgs = ' '+sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '

# parse the gff
print "------ running parse_gff_build"
os.system('python '+PATH_TO_SCRIPTS + 'parse_gff_build.py'+remArgs)
print "------ running parse_gff_multi"
os.system('python '+PATH_TO_SCRIPTS + 'parse_gff_multi.py'+remArgs)

# usearch
print "------ usearch build"
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_build.py'+remArgs)
print "------ usearch multi"
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_multi.py'+remArgs)

print "------ parse usearch"
# parse multiple usearch
os.system('python '+ PATH_TO_SCRIPTS + 'parse_multiple_usearch.py'+remArgs)

# MCL
print "------ MCL time"
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mcl.py'+remArgs)

# getcore
print "------ get core"
os.system('python '+ PATH_TO_SCRIPTS + 'get_core.py'+remArgs)

# launch mafft
print "------ mafft prep"
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mafft_build.py'+remArgs)

print "------ going on mafft"
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mafft_multi.py'+remArgs)

# concat85
print "------ concating to the 85"
os.system('python '+ PATH_TO_SCRIPTS + 'concat85_arr.py'+remArgs)

# Raxml distance
print "------ Raxml TIME!!!"
os.system('python '+ PATH_TO_SCRIPTS + 'raxml_distance.py'+remArgs)

# sample.py
print "------ Sampling time"
os.system('python '+ PATH_TO_SCRIPTS + 'sample.py'+remArgs)

# calcHM
print "------ going for r/m"
os.system('python '+ PATH_TO_SCRIPTS + 'calcHM_multi.py'+remArgs)

print "------ Email the results!"
os.system('python '+ PATH_TO_SCRIPTS + 'mail.py'+remArgs)

# graph
print "------ Graph time!"
os.system('python '+ PATH_TO_SCRIPTS + 'graph.py'+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'big_graph.py'+remArgs)
os.system('Rscript '+ PATH_TO_UPLOAD + 'graph.R')
quit()

