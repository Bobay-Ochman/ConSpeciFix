import os
from config import *


strains = []

files = os.listdir( PATH_TO_FOLDER)
for truc in files:
	if truc.endswith('.fa'):
		strains.append(truc)

liste = []
for st in strains:
	truc = st 
	liste.append(truc)


parent,dico={},{}

todoList = open(PATH_TO_TODO + 'usearch.txt','w')

globalDone = 0
globalLeftToDo = 0

nb = len(liste)
if nb >= 2:
	i=0
	done = 0
	leftToDo = 0
	for prot1 in liste:
		i+=1
		for prot2 in liste[i:]:
			if prot1 != prot2:
				try:
					completed = open(PATH_TO_MAT + 'BBH/' + prot1 + '-' + prot2, 'r')
					done+=1
					globalDone +=1
				except:
					todoList.write(prot1 + '\t' + prot2+'\n');
					leftToDo+=1
					globalLeftToDo+=1
else:
	print ' <2'
todoList.truncate()
todoList.close()

print 'done already: ',globalDone, ' left to do: ',globalLeftToDo
















	
