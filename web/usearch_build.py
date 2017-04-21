import os
from config import *

########################################################################
import math
 
def mean( echantillon ) :
    size = len( echantillon )
    moyenne = float(sum( echantillon )) / float(size)
    return moyenne


def stat_variance( echantillon ) :
    n = float(len( echantillon )) # taille
    mq = mean( echantillon )**2
    s = sum( [ x**2 for x in echantillon ] )
    variance = s / n - mq
    return variance


def stat_ecart_type( echantillon ) :
    variance = stat_variance( echantillon )
    ecart_type = math.sqrt( variance )
    return ecart_type

def median( echantillon) :
	echantillon.sort()
	size = len( echantillon )
	if len( echantillon ) % 2 == 0:
		M= float(echantillon[size / 2 - 1] + echantillon[size / 2]) / 2
	else:
		M= echantillon[size / 2]
	return M

def ninetyfive( echantillon) :
	echantillon.sort()
	size = len( echantillon )
	i95 = int( float(size) * 95/100 ) - 1
	return echantillon[i95]




species=getSpecies()
#print species
#species = ['Acetobacter_pasteurianus']



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
			for prot2 in liste[sp][i:]:
				if prot1 != prot2:
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





















	
