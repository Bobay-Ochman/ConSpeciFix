import os
from config import *

species = getSpecies()

print species


strains={}
for sp in species:
	strains[sp]=[]


h=open('../liste_genomes.txt','w')
for sp in species:
	files = os.listdir(PATH_TO_OUTPUT+sp+'/genomes/')
#	print files
	for truc in files:
		if truc.endswith('.fa'):
			b= truc.split('.')
			if len(b) != 2:
				print sp, ' ',b,' PROBLEM'
			st = b[0]
			h.write(sp + '\t' + st + '\n')
			strains[sp].append(st)

h.close()







	
