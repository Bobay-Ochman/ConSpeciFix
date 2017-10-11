import os
import sys
from multiprocessing import Pool
from config import *


strains=[]
try:
	f=open(PATH_TO_MAT+'sample.txt','r')		
	for l in f:
		a=l.strip("\n").split("\t")
		strains.append(a[0])
	f.close()
except IOError as e:
	print e
	exit()

dist={}
f=open(PATH_TO_MAT + 'RAxML_distances.dist',"r")
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
f=open(PATH_TO_MAT + 'concat85.fa',"r")
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
			print e
			exit()
f.close()


seq = {}
for sp in strains:
	seq[sp] = ''.join(tmp[sp])


memo_subset={}
tmp = os.listdir(PATH_TO_MAT)
for file in tmp:
	if file.startswith("rm"):
		f=open( PATH_TO_MAT + file,"r")
		for l in f:
			a=l.strip("\n").split("\t")
			if len(a) == 5:									
				memo_subset[a[0]] = a[1:]
		f.close()



f_subset=open(PATH_TO_MAT + 'rm1.txt',"w")
for subset in memo_subset:
	f_subset.write(subset + "\t" + '\t'.join(memo_subset[subset])  + "\n")
f_subset.close()



tmp=[]
f=open(PATH_TO_MAT + 'families.txt','r')
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

print '*** GO',len(subsets)

fd = open(PATH_TO_TODO + 'calcHM.txt','a')
for t in subsets:
	fd.write( t + '\n')
fd.close()