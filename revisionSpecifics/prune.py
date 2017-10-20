import os
from config import *

species=getAllSpecies()

for sp in species:
	removalFile = open(PATH_TO_OUTPUT + sp + '/for_removal.txt','r')
	strainsFile = open(PATH_TO_OUTPUT + sp + '/sample.txt','r')
	removal = []
	strains = []
	for s in removalFile:
		removal.append(s.strip('\n'))
	for s in strainsFile:
		strain = s.strip('\n')
		if strain not in removal:
			strains.append(strain)
	strainsFile.close()
	removalFile.close()
	f = open(PATH_TO_OUTPUT + sp + '/revisedStrains.txt','w')
	f.write('\n'.join(strains))
	f.close()




