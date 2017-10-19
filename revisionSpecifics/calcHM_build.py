import os
import sys
from multiprocessing import Pool
from config import *


def calcHM(SP):
	# Load distances
	print SP
	strains=[]
	try:
		f=open(PATH_TO_OUTPUT + SP + '/revisedStrains.txt','r')
		
		for l in f:
			a=l.strip("\n").split("\t")
			strains.append(a[0])
		f.close()
	except IOError as e:
		print SP, e
		return

	subsets = []
	subsets.append('&&&'.join(strains))

	print '*** GO',SP,len(subsets)

	fd = open('todo/calcHM.txt','a')
	for t in subsets:
		for i in range(100):
			fd.write(SP + '\t' + str(i) +'\t' + t + '\n')
	fd.close()

"""
fd = open('todo/calcHM.txt','a')
fd.seek(0)
fd.truncate()
fd.close()
	
for sp in getSelectedSpecies('sample.txt'):
	calcHM(sp)

"""


if __name__ == '__main__':
	fd = open('todo/calcHM.txt','a')
	fd.seek(0)
	fd.truncate()
	fd.close()
	species = giveMulti(getSelectedSpecies('revisedStrains.txt'))	
	print len(species)
	p = Pool(MAX_THREADS)
	p.map(calcHM,species)


#"""
