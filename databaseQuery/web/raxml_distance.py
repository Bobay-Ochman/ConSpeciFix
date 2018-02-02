import os
from config import *


species = getSingleSpecies()

### Don't multithread because RAxML can do it for us and better

for sp in species:
	print sp
	os.chdir(PATH_TO_UPLOAD)
	os.system(RAXML_PATH)
	os.system(RAXML_PATH + ' -f x -T 2 -p 12345 -s ' +  ' concat85.fa  -m GTRGAMMA -n dist')


#'raxml -f x -T 4 -p 12345 -s /Volumes/ITDR/brian/results/Acetobacter_pasteurianus/concat85.phy  -m GTRGAMMA -n dist'
#/var/app/current/efs/progs/RAxML/raxmlHPC-PTHREADS-SSE3 -f x -T 1 -p 12345 -s concat85.fa  -m GTRGAMMA -n dist
#time caffeinate raxml -f x -T 16 -p 12345 -s /Volumes/ITDR/brian/results/Acetobacter_pasteurianus/concat85.fa  -m GTRGAMMA -n dist