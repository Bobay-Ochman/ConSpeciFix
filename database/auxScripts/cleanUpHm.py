from config import *
import os



species = getAllSpecies()


edditedSpecies = []


for sp in species:
	fdspec = open(PATH_TO_OUTPUT+sp+'/sample.txt')
	acceptableStrains = [x.strip('\n')for x in fdspec.readlines()]
	maxsize = len(acceptableStrains)

	fdhm = open(PATH_TO_OUTPUT+sp+'/rm1.txt','r')
	for l in fdhm.readlines():
		parts = l.split('\t')
		size = len(parts[0].split('&&&'))
		if size > maxsize:
			print size
	fdhm.close()


	fdhm = open(PATH_TO_OUTPUT+sp+'/rm1.txt','r')
	newLines = []
	print sp
	badStrainNames = []
	for l in fdhm.readlines():
		parts = l.split('\t')
		strainsHere = parts[0].split('&&&')
		for strain in strainsHere:
			if strain not in acceptableStrains:
				badStrainNames.append(str(strain))
		if size <= maxsize and len(badStrainNames)==0:
			newLines.append(l.strip('\n'))
	fdhm.close()
	newhmfd = open(PATH_TO_OUTPUT+sp+'/rmTEST.txt','w')
	newhmfd.write("\n".join(newLines))
	newhmfd.close()
	edditedSpecies.append(sp)

for sp in edditedSpecies:
	# pass
	os.system('mv '+PATH_TO_OUTPUT+sp+'/rm1.txt ' +PATH_TO_OUTPUT+sp+'/rm1_old3.txt ')
	os.system('mv '+PATH_TO_OUTPUT+sp+'/rmTEST.txt ' +PATH_TO_OUTPUT+sp+'/rm1.txt ')
