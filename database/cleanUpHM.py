from config import *
import os

species = getAllSpecies()

edditedSpecies = []


for sp in species:
	fdspec = open(PATH_TO_OUTPUT+sp+'/sample.txt')
	maxsize = len(fdspec.readlines())
	if maxsize > 99:
		maxsize = 99

	fdhm = open(PATH_TO_OUTPUT+sp+'/rm1.txt','r')
	flag = False
	for l in fdhm.readlines():
		parts = l.split('\t')
		size = len(parts[0].split('&&&'))
		if size > maxsize:
			print size
			flag = True
	fdhm.close()

	if(flag):
		fdhm = open(PATH_TO_OUTPUT+sp+'/rm1.txt','r')
		newLines = []
		print sp
		for l in fdhm.readlines():
			parts = l.split('\t')
			size = len(parts[0].split('&&&'))
			if size <= maxsize:
				newLines.append(l.strip('\n'))
		fdhm.close()
		newhmfd = open(PATH_TO_OUTPUT+sp+'/rmTEST.txt','w')
		newhmfd.write("\n".join(newLines))
		newhmfd.close()
		edditedSpecies.append(sp)

for sp in edditedSpecies:
	os.system('mv '+PATH_TO_OUTPUT+sp+'/rm1.txt ' +PATH_TO_OUTPUT+sp+'/rm1_old.txt ')
	os.system('mv '+PATH_TO_OUTPUT+sp+'/rmTEST.txt ' +PATH_TO_OUTPUT+sp+'/rm1.txt ')
