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
	os.system('mkdir '+PATH_TO_UPLOAD+'out')
	os.system('mkdir '+PATH_TO_UPLOAD+'align')

except OSError as e:
	print e




remArgs = ' '+sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+sys.argv[4]+' '

print "------ cleaning the names of the genes"
os.system('python '+PATH_TO_SCRIPTS + 'clean_gene_names.py '+remArgs + ' > '+PATH_TO_UPLOAD+'out/clean.txt')
# parse the gff -> Skip since the FA already exists
#print "------ running parse_gff_build"
#os.system('python '+PATH_TO_SCRIPTS + 'parse_gff_build.py'+remArgs)
#print "------ running parse_gff_multi"
#os.system('python '+PATH_TO_SCRIPTS + 'parse_gff_multi.py'+remArgs)

print "------ Expects just to have a .fa file"
# usearch

sendEmail("We've started your analysis and will be emailing you periodically to keep you updated on how it is going.")

print "------ usearch build"
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_build.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/u_build.txt')
print "------ usearch multi"
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_multi.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/u_multi.txt')

print "------ parse usearch"
# parse multiple usearch
os.system('python '+ PATH_TO_SCRIPTS + 'parse_multiple_usearch.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/u_parse.txt')

# MCL
print "------ MCL time"
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mcl.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/mcl.txt')

# getcore
print "------ get core"
os.system('python '+ PATH_TO_SCRIPTS + 'get_core.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/get_core.txt')

# launch mafft
print "------ mafft prep"
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mafft_build.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/mafft_build.txt')

print "------ going on mafft"
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mafft_multi.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/mafft_multi.txt')

# concat85
print "------ concating to the 85"
os.system('python '+ PATH_TO_SCRIPTS + 'concat85_arr.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/concat85.txt')

# Raxml distance
print "------ Raxml TIME!!!"
os.system('python '+ PATH_TO_SCRIPTS + 'raxml_distance.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/raxml.txt')

try:
	f = open(PATH_TO_UPLOAD+'RAxML_distances.dist',"r")
except:
	sendEmail("The genome that you are testing is substantially divergent from "+getSingleSpecies()[0]+", prohibiting recombination analysis and preventing production of h/m graphs. Please select a more closely related sample-set for comparison, if available.")
	quit()


# sample.py
print "------ Sampling time"
os.system('python '+ PATH_TO_SCRIPTS + 'sample.py'+remArgs + ' > '+PATH_TO_UPLOAD+'out/sample.txt')

# calcHM
print "------ going for r/m"
os.system('python '+ PATH_TO_SCRIPTS + 'calcHM_multi.py'+remArgs + ' > '+PATH_TO_UPLOAD+'out/calcHM.txt')

# graph
print "------ Graph time!"
os.system('python '+ PATH_TO_SCRIPTS + 'graph.py'+remArgs + ' > '+PATH_TO_UPLOAD+'out/graph.txt')
os.system('python '+ PATH_TO_SCRIPTS + 'big_graph.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/graph_big.txt')
os.system('Rscript '+ PATH_TO_UPLOAD + 'graph.R'+ ' > '+PATH_TO_UPLOAD+'out/graph_r.txt')

print "------ Email the results!"
os.system('python '+ PATH_TO_SCRIPTS + 'mailGraph.py'+remArgs)
quit()

