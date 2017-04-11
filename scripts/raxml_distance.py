from config import *
import os

species = ['Acetobacter_pasteurianus']

for sp in species:
	os.system('raxml -f x -T 4 -p 12345 -s' + PATH_TO_OUTPUT+ sp + '/concat85.fa  -m GTRGAMMA -n dist')
	os.system('mv RAxML_distances.dist   '+PATH_TO_OUTPUT+ sp +'/distances.dist')
	os.system('rm RA*')




#make multi with selected species

