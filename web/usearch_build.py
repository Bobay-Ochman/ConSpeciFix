import os
from config import *


species=getSingleSpecies()
specialStrain = getCompStrain()


strains=getStrains()


liste={}
for sp in species:
	liste[sp]=[]
	for st in strains[sp]:
		truc = st 
		liste[sp].append(truc)


parent,dico={},{}

todoList = open(uploadPath()+'/usearch.txt','w')

globalDone = 0
globalLeftToDo = 0

for sp in species:
	#if 'Mycobacterium' in sp or 'Pseudomonas_syringae' in sp or 'Ralstonia_solanacearum' in sp or 'Rhodococcus' in sp or 'Streptomyces_griseus' in sp:
	#	continue
	nb = len(liste[sp])
	if nb >= 15:
		print sp,' ',nb,' strains'
		done = 0
		leftToDo = 0
		for prot1 in liste[sp]:
			prot2 = specialStrain
			todoList.write(PATH_TO_OUTPUT + '\t' + sp + '\t' + prot1 + '\t' + prot2+'\n');
			leftToDo+=1
			globalLeftToDo+=1
		print 'done already: ',done, ' left to do: ',leftToDo
	else:
		print sp, ' <15'
todoList.close()

print 'done already: ',globalDone, ' left to do: ',globalLeftToDo


