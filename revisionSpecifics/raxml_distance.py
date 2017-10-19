import os
from config import *


species = giveMulti(getAllSpecies())	

### Don't multithread because RAxML can do it for us and better

for sp in species:
	print sp
	for i in range(100):
		os.chdir(PATH_TO_OUTPUT+ sp+'/geneSubsets/geneSubsetNo'+str(i)+'/')
		print os.getcwd()
		try:
			os.system('rm RAx*')
		except:
			pass
		os.system(RAXML_PATH+' -f x -T 10 -p 12345 -s ' +  ' concat85.fa  -m GTRGAMMA -n dist')
