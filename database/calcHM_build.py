import os
import sys
from multiprocessing import Pool
from config import *


def calcHM(SP):
	# Load distances
	print SP
	strains=[]
	try:
		f=open(PATH_TO_OUTPUT + SP + '/sample.txt','r')
		
		for l in f:
			a=l.strip("\n").split("\t")
			strains.append(a[0])
		f.close()
	except IOError as e:
		print SP, e
		return

	dist={}
	f=open(PATH_TO_OUTPUT + SP + '/RAxML_distances.dist',"r")
	for l in f:
		a=l.strip("\n").split("\t")
		st1,st2 = a[0].strip(" ").split(" ")[0], a[0].strip(" ").split(" ")[1]
		if dist.has_key(st1):
			pass
		else:
			dist[st1] = {}
		if dist.has_key(st2):
			pass
		else:
			dist[st2] = {}
		dist[st1][st2] = float(a[1])
		dist[st2][st1] = float(a[1])
	f.close()




	tmp={}
	f=open(PATH_TO_OUTPUT + SP + '/concat85.fa',"r")
	for l in f:
		if l[0] == '>':
			nb=0
			tag=0
			sp = l.strip('>').strip('\n') 
			tmp[sp] = []
		else:
			try:
				nb += len(l.strip('\n'))
				tmp[sp].append(l.strip('\n'))
			except (KeyError,UnboundLocalError) as e:
				print SP, e
				return
	f.close()


	seq = {}
	for sp in strains:
		seq[sp] = ''.join(tmp[sp])


	#strains.remove('Dsim')

	memo_subset={}
	tmp = os.listdir(PATH_TO_OUTPUT + SP + '/')
	for file in tmp:
		if file.startswith("rm"):
			f=open( PATH_TO_OUTPUT + SP + '/' + file,"r")
			for l in f:
				a=l.strip("\n").split("\t")
				if len(a) == 5:									
					memo_subset[a[0]] = a[1:]
			f.close()


	tmp=[]
	f=open(PATH_TO_OUTPUT + SP + '/families_'+SP+'.txt','r')
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

	fd = open('todo/calcHM.txt','a')
	for t in subsets:
		fd.write(SP + '\t' + t + '\n')
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
	species = giveMulti(getSelectedSpecies('sample.txt'))	
	print len(species)
	p = Pool(MAX_THREADS)
	p.map(calcHM,species)


#"""
