import os
from config import *


species = giveMulti(getSpeciesForTest())
print species

### Don't multithread because RAxML can do it for us and better

for sp in species:
	print sp
	os.chdir(PATH_TO_OUTPUT+ sp+'/')
	print os.getcwd()
	os.system('rm RAx*')
	os.system(RAXML_PATH+' -f x -T 16 -p 12345 -s ' +  ' concat85.fa  -m GTRGAMMA -n dist')



#timeout 4 /work/03414/be4833/RAxML/raxmlHPC-PTHREADS -f x -T 4 -p 12345 -s concat85.fa  -m GTRGAMMA -n dist

#time caffeinate raxml -f x -T 16 -p 12345 -s /Volumes/ITDR/brian/results/Acetobacter_pasteurianus/concat85.fa  -m GTRGAMMA -n dist

#make multi with selected species
