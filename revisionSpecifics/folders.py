import os
from config import *

species=getAllSpecies()

for sp in species:
	os.mkdir(PATH_TO_OUTPUT + sp + '/geneSubsets')
	try:
		for i in range(100):
			os.mkdir(PATH_TO_OUTPUT + sp + '/geneSubsets/geneSubsetNo'+str(i))
	except OSError:
		pass




