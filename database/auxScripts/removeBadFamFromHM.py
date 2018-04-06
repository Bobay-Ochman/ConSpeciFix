from config import *
import os

species = getAllSpecies()

edditedSpecies = []


for sp in species:
	fdspec = open(PATH_TO_OUTPUT+sp+'/sample.txt')
	acceptableStrains = [x.strip('\n')for x in fdspec.readlines()]
	print acceptableStrains
	print len(acceptableStrains)
	maxsize = len(acceptableStrains)


	badStrainNames = []

	fdFam = open(PATH_TO_OUTPUT+sp+'/families_'+sp+'.txt')
	for l in fdFam.readlines():
		strains = l.split('\t')[1].split('&&&')
		for st in strains:
			if not st.strip('\n') in acceptableStrains:
				badStrainNames.append(st)
	print set(badStrainNames)



	fdhm = open(PATH_TO_OUTPUT+sp+'/rm1.txt','r')
	flag = True
	for l in fdhm.readlines():
		parts = l.split('\t')
		size = len(parts[0].split('&&&'))
		if size > maxsize:
			print size
			flag = True
	fdhm.close()

	i = 0

	if(flag):
		fdhm = open(PATH_TO_OUTPUT+sp+'/rm1.txt','r')
		newLines = []
		print sp
		for l in fdhm.readlines():
			badStrainNames = []
			parts = l.split('\t')
			strainsHere = parts[0].split('&&&')
			for strain in strainsHere:
				if strain not in acceptableStrains:
					badStrainNames.append(strain)
			print badStrainNames
			i+=1
			if i > 50:
				pass
			if size <= maxsize and len(badStrainNames)==0:
				newLines.append(l.strip('\n'))
		fdhm.close()
		newhmfd = open(PATH_TO_OUTPUT+sp+'/rmTEST.txt','w')
		newhmfd.write("\n".join(newLines))
		newhmfd.close()
		edditedSpecies.append(sp)

for sp in edditedSpecies:
	# os.system('mv '+PATH_TO_OUTPUT+sp+'/rm1.txt ' +PATH_TO_OUTPUT+sp+'/rm1_old.txt ')
	# os.system('mv '+PATH_TO_OUTPUT+sp+'/rmTEST.txt ' +PATH_TO_OUTPUT+sp+'/rm1.txt ')
	pass