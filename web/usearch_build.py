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

todoList = open('todo/usearch.txt','w')
largeSpecList = open('todo/LargeSpec.txt','w')

globalDone = 0
globalLeftToDo = 0

for sp in species:
	#if 'Mycobacterium' in sp or 'Pseudomonas_syringae' in sp or 'Ralstonia_solanacearum' in sp or 'Rhodococcus' in sp or 'Streptomyces_griseus' in sp:
	#	continue
	nb = len(liste[sp])
	if nb >= 15:
		if nb > 500:
			largeSpecList.write(sp + '\n')
			continue
		print sp,' ',nb,' strains'
		i=0
		done = 0
		leftToDo = 0
		for prot1 in liste[sp]:
			i+=1
			prot2 = specialStrain
			try:
				completed = open(PATH_TO_OUTPUT +  sp + '/BBH/' + prot1 + '-' + prot2, 'r')
				done+=1
				globalDone +=1
				continue
			except:
				todoList.write(PATH_TO_OUTPUT + '\t' + sp + '\t' + prot1 + '\t' + prot2+'\n');
				leftToDo+=1
				globalLeftToDo+=1
		print 'done already: ',done, ' left to do: ',leftToDo
	else:
		print sp, ' <15'
todoList.close()
largeSpecList.close()

print 'done already: ',globalDone, ' left to do: ',globalLeftToDo


