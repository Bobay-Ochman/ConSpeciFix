import os
from config import *


species=getSingleSpecies()
specialStrain = getCompStrain()

liste={}
for sp in species:
	liste[sp]=[]
	for st in open(PATH_TO_OUTPUT + sp + '/tenForUsearch.txt','r').readlines():
		truc = st.strip('\n')
		liste[sp].append(truc)

parent,dico={},{}

todoList = open(PATH_TO_UPLOAD+'todo/usearch.txt','w')

globalDone = 0
globalLeftToDo = 0

for sp in species:
	#if 'Mycobacterium' in sp or 'Pseudomonas_syringae' in sp or 'Ralstonia_solanacearum' in sp or 'Rhodococcus' in sp or 'Streptomyces_griseus' in sp:
	#	continue
	print sp
	done = 0
	leftToDo = 0
	for prot1 in liste[sp]:
		prot2 = specialStrain+'.fa'
		todoList.write(PATH_TO_OUTPUT + '\t' + sp + '\t' + prot1 + '\t' + prot2+'\n');
		leftToDo+=1
		globalLeftToDo+=1
	print 'done already: ',done, ' left to do: ',leftToDo

todoList.close()

print 'done already: ',globalDone, ' left to do: ',globalLeftToDo