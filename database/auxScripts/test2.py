from config import *
import os

species = getAllSpecies()
edditedSpecies = []



for sp in species:
	rmVals = []
	fdspec = open(PATH_TO_OUTPUT+sp+'/sample.txt')
	maxsize = len(fdspec.readlines())
	if maxsize > 99:
		maxsize = 99
	maxsize = 22
	fdhm = open(PATH_TO_OUTPUT+sp+'/distrib.txt','r')
	flag = False
	for l in fdhm.readlines():
		parts = l.split('\t')
		size = len(parts[0].split('&&&'))
		if size > maxsize:
			flag = True
		rmVals.append(float(parts[1]))
		print parts[1]
	fdhm.close()
print sum(rmVals) / len(rmVals)
print max(rmVals)

