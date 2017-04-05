from config import *

print getSpecies()
species = getSpecies()
	
#make sure we don't do work that has already been done
todoSpec = []
for sp in species:
	try:
		k=open(PATH_TO_OUTPUT + sp + '/input.txt','r')
		todoSpec.append(sp)
	except:
		pass
species = todoSpec
print len(species)