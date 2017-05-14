from config import *
from mailMessage import *
import os
import sys


print "------ making folders"

# make folders
try:
	os.system('mkdir '+PATH_TO_UPLOAD+'todo')
	os.system('mkdir '+PATH_TO_UPLOAD+'BBH')
	os.system('mkdir '+PATH_TO_UPLOAD+'results')
	os.system('mkdir '+PATH_TO_UPLOAD+'align')

except OSError as e:
	print e


remArgs = ' '+sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+sys.argv[4]+' '

# parse the gff -> Skip since the FA already exists
#print "------ running parse_gff_build"
#os.system('python '+PATH_TO_SCRIPTS + 'parse_gff_build.py'+remArgs)
#print "------ running parse_gff_multi"
#os.system('python '+PATH_TO_SCRIPTS + 'parse_gff_multi.py'+remArgs)

print "------ Expects just to have a .fa file"
# usearch

sendEmail("We've started your analysis and will be emailing you periodically to keep you updated on how it is going.")

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

try:
	f = open(PATH_TO_UPLOAD+'RAxML_distances.dist',"r")
except:
	sendEmail("It seems the genome you are testing against is completly divergent from "+getSingleSpecies()[0]+". Because of this, we were unable to produce H/M graphs to illustrate how simmilar they are.")
	quit()


# sample.py
print "------ Sampling time"
os.system('python '+ PATH_TO_SCRIPTS + 'sample.py'+remArgs)

# calcHM
print "------ going for r/m"
os.system('python '+ PATH_TO_SCRIPTS + 'calcHM_multi.py'+remArgs)

# graph
print "------ Graph time!"
os.system('python '+ PATH_TO_SCRIPTS + 'graph.py'+remArgs)
os.system('python '+ PATH_TO_SCRIPTS + 'big_graph.py'+remArgs)
os.system('Rscript '+ PATH_TO_UPLOAD + 'graph.R')

print "------ Email the results!"
os.system('python '+ PATH_TO_SCRIPTS + 'mailGraph.py'+remArgs)
quit()

