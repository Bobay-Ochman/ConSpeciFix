from config import *
from mailMessage import *
import os
import sys



def goHome():
	print "------ Going Home"
	quit()




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
os.system('python '+PATH_TO_SCRIPTS + 'clean_gene_names.py '+remArgs + ' > '+PATH_TO_UPLOAD+'out/01_clean.txt')

print "------ usearch build"
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_build.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/02_u_build.txt')
print "------ usearch multi"
os.system('python '+ PATH_TO_SCRIPTS + 'usearch_multi.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/03_u_multi.txt')

#write all the ortholog files
print "------ add to core"
os.system('python '+ PATH_TO_SCRIPTS + 'add_to_core.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/04_add_to_core.txt')

print "------ write core"
os.system('python '+ PATH_TO_SCRIPTS + 'write_core.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/05_write_core.txt')


# launch mafft
print "------ mafft prep"
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mafft_build.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/07_mafft_build.txt')

print "------ going on mafft"
os.system('python '+ PATH_TO_SCRIPTS + 'launch_mafft_multi.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/08_mafft_multi.txt')

# concat85
print "------ concating to the 85"
os.system('python '+ PATH_TO_SCRIPTS + 'concat85_arr.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/09_concat85.txt')

# Raxml distance
print "------ Raxml TIME!!!"
os.system('python '+ PATH_TO_SCRIPTS + 'raxml_distance.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/10_raxml.txt')

try:
	f = open(PATH_TO_UPLOAD+'RAxML_distances.dist',"r")
except:
	#sendEmail("The genome that you are testing is substantially divergent from "+getSingleSpecies()[0]+", prohibiting recombination analysis and preventing production of h/m graphs. Please select a more closely related sample-set for comparison, if available.")
	os.system('echo quitting, going home > '+PATH_TO_UPLOAD+'out/11_stopping.txt')
	goHome()

# sample.py
print "------ Sampling time"
os.system('python '+ PATH_TO_SCRIPTS + 'sample.py'+remArgs + ' > '+PATH_TO_UPLOAD+'out/11_sample.txt')

# calcHM
print "------ going for r/m"
os.system('python '+ PATH_TO_SCRIPTS + 'calcHM_multi.py'+remArgs + ' > '+PATH_TO_UPLOAD+'out/12_calcHM.txt')

# graph
print "------ Graph time!"
os.system('python '+ PATH_TO_SCRIPTS + 'graph.py'+remArgs + ' > '+PATH_TO_UPLOAD+'out/13_graph.txt')
os.system('python '+ PATH_TO_SCRIPTS + 'big_graph.py'+remArgs+ ' > '+PATH_TO_UPLOAD+'out/14_graph_big.txt')
os.system('Rscript '+ PATH_TO_UPLOAD + 'graph.R'+ ' > '+PATH_TO_UPLOAD+'out/15_graph_r.txt')

print "------ Analysis time!"
os.system('python '+ PATH_TO_SCRIPTS + 'distrib.py '+remArgs+ ' > '+PATH_TO_UPLOAD+'out/16_distrib.txt')
os.system('python '+ PATH_TO_SCRIPTS + 'kmean.py '+remArgs+ ' > '+PATH_TO_UPLOAD+'out/17_kmean.txt')
os.system('python '+ PATH_TO_SCRIPTS + 'split_kmean.py '+remArgs+ ' > '+PATH_TO_UPLOAD+'out/18_split_kmean.txt')
os.system('python '+ PATH_TO_SCRIPTS + 'criterion.py '+remArgs+ ' > '+PATH_TO_UPLOAD+'out/19_criterion.txt')
os.system('python '+ PATH_TO_SCRIPTS + 'draw_box_plot.py '+remArgs+ ' > '+PATH_TO_UPLOAD+'out/20_draw.txt')

goHome()
