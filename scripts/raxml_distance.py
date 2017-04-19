import os
from config import *


species = giveMulti(getSelectedSpecies())

### Don't multithread because RAxML can do it for us and better

for sp in species:
	print sp
	os.chdir(PATH_TO_OUTPUT+ sp+'/')
	print os.getcwd()
	os.system('raxml -f x -T 16 -p 12345 -s ' +  ' concat85.phy  -m GTRGAMMA -n dist')




#'raxml -f x -T 4 -p 12345 -s /Volumes/ITDR/brian/results/Acetobacter_pasteurianus/concat85.phy  -m GTRGAMMA -n dist'

#time caffeinate raxml -f x -T 16 -p 12345 -s /Volumes/ITDR/brian/results/Acetobacter_pasteurianus/concat85.fa  -m GTRGAMMA -n dist

#make multi with selected species
