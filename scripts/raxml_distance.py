from config import *
import os

species = getSelectedSpecies()

for sp in species:
	os.system('time caffeinate raxml -f x -T 16 -p 12345 -s' + PATH_TO_OUTPUT+ sp + '/concat85.phy  -m GTRGAMMA -n dist')
	os.system('mv RAxML_distances.dist   '+PATH_TO_OUTPUT+ sp +'/distances.dist')
	os.system('rm RA*')





#'raxml -f x -T 4 -p 12345 -s /Volumes/ITDR/brian/results/Acetobacter_pasteurianus/concat85.phy  -m GTRGAMMA -n dist'

#time caffeinate raxml -f x -T 16 -p 12345 -s /Volumes/ITDR/brian/results/Acetobacter_pasteurianus/concat85.fa  -m GTRGAMMA -n dist

#make multi with selected species
