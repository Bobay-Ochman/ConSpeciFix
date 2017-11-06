import os
from config import *

species=getAllSpecies()

for sp in species:
	hmRatios = []
	for i in range(100):
		try:
			f = open(PATH_TO_OUTPUT+sp+'/geneSubsets/geneSubsetNo'+str(i)+'/rm1.txt')
			for l in f:
				hmRatios.append(l.split('\t')[3])
		except:
			pass
	hmRatios = sorted(hmRatios)
	out = open(PATH_TO_OUTPUT + sp +'/geneSubsetHMVals.txt','w')
	out.write("hmRatio\tsize\n")
	for ratio in hmRatios:
		out.write(str(ratio)+'\t'+str(len(hmRatios))+'\n')
	out.close()