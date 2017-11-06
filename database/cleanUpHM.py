from config import *
import os

species = ['Staphylococcus_argenteus']

for sp in species:
	fdhm = open(PATH_TO_OUTPUT+sp+'/rm1.txt','r')
	flag = False
	for l in fdhm.readlines():
		parts = l.split('\t')
		size = len(parts[0].split('&&&'))
		if size > 80:
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
			if size <= 82:
				newLines.append(l.strip('\n'))
		fdhm.close()
		newhmfd = open(PATH_TO_OUTPUT+sp+'/rmTEST.txt','w')
		newhmfd.write("\n".join(newLines))
		newhmfd.close()
