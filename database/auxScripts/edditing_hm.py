from config import *
import os

species = getAllSpecies()

edditedSpecies = []


for sp in species:
	fdspec = open(PATH_TO_OUTPUT+sp+'/sample.txt')
	maxsize = len(fdspec.readlines())

	fdhm = open(PATH_TO_OUTPUT+sp+'/rm1.txt','r')
	flag = False
	rmratios = []
	for l in fdhm.readlines():
		parts = l.split('\t')
		size = len(parts[0].split('&&&'))
		if size >= maxsize/10.0 * 9:
			rm = float(parts[3])
			rmratios.append(rm)
	print sp+'\t'+str(sum(rmratios) / len(rmratios))
	fdhm.close()