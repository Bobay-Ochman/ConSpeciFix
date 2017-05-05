import os
import sys
from multiprocessing import Pool
from config import *


for SP in getSingleSpecies():
	

	#strains.remove('Dsim')

	memo_subset={}
	tmp = os.listdir(PATH_TO_UPLOAD)
	for file in tmp:
		if file.startswith("rm"):
			f=open( PATH_TO_UPLOAD + file,"r")
			for l in f:
				a=l.strip("\n").split("\t")
				if len(a) == 5:									
					memo_subset[a[0]] = a[1:]
			f.close()


	f_subset=open(PATH_TO_UPLOAD+'rm1.txt',"w")
	for subset in memo_subset:
		f_subset.write(subset + "\t" + '\t'.join(memo_subset[subset])  + "\n")

	f_subset.close()



	tmp=[]
	f=open(PATH_TO_UPLOAD + 'families_'+SP+'.txt','r')
	for l in f:
		a=l.strip('\n').split('\t')
		if memo_subset.has_key(a[1]):
			pass
		else:
			tmp.append(a[1])


	import random

	subsets=[]
	while len(tmp) > 0:
		truc = random.choice(tmp)
		subsets.append(truc)
		tmp.remove(truc)

	print '*** GO',SP,len(subsets)

	fd = open(PATH_TO_UPLOAD + 'todo/calcHM.txt','a')
	for t in subsets:
		fd.write(SP + '\t' + t + '\n')
	fd.close()


"""
fd = open('todo/calcHM.txt','a')
fd.seek(0)
fd.truncate()
fd.close()
	
for sp in getSelectedSpecies():
	calcHM(sp)

"""


#"""
