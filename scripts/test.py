from config import *
import os


species = giveMulti(getSelectedSpecies())
print species
complete = []
for sp in species:
	try:
		k=open(PATH_TO_OUTPUT + sp + '/out.input_'+sp+'.txt.I12','r')
		complete.append(sp)
		k.close()
	except:
		pass

todoSpec = []
for sp in species:
	if sp in complete:
		continue
	try:
		k=open(PATH_TO_OUTPUT + sp + '/input_'+sp+'.txt','r')
		todoSpec.append(sp)
		k.close()
	except:
		pass
species = todoSpec

print species