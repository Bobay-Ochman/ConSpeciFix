import os
from config import *


species=getSpecies()
#species = ['Mycobacterium_abscessus']
strains={}
for sp in species:
	strains[sp]=[]


for sp in species:
	files = os.listdir( PATH_TO_OUTPUT + sp + '/genes/')
	for truc in files:
		if truc.endswith('.fa'):
			strains[sp].append(truc)



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

listOfTodos = []

for sp in species:
	#if 'Mycobacterium' in sp or 'Pseudomonas_syringae' in sp or 'Ralstonia_solanacearum' in sp or 'Rhodococcus' in sp or 'Streptomyces_griseus' in sp:
	#	continue
	nb = len(liste[sp])
	if nb >= MIN_SPECIES_SIZE:
		print sp,' ',nb,' strains'
		i=0
		done = 0
		leftToDo = 0
		for prot1 in liste[sp]:
			i+=1
			for prot2 in liste[sp][i:]:
				if prot1 != prot2:
					if os.path.isfile(PATH_TO_OUTPUT +  sp + '/'+USEARCH_FOLDER+'/' + prot1 + '-' + prot2):
						done+=1
						globalDone +=1
					else:
						listOfTodos.append(PATH_TO_OUTPUT + '\t' + sp + '\t' + prot1 + '\t' + prot2);
						leftToDo+=1
						globalLeftToDo+=1
		print 'done already: ',done, ' left to do: ',leftToDo
	else:
		print sp, ' <'+str(MIN_SPECIES_SIZE)

todoList.write('\n'.join(listOfTodos))
todoList.truncate()
todoList.close()
largeSpecList.close()

print 'done already: ',globalDone, ' left to do: ',globalLeftToDo





















	
