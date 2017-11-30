from config import *
import os

species = getAllSpecies()

allDifferences = []
zeroOldCount = 0
zeroNewCount = 0

for sp in species:
	maxDist = -1;
	strains = []
	for l in open(PATH_TO_OUTPUT+sp+'/sample.txt','r').readlines():
		strains.append(l.strip('\n'))

	raxmlFD = open(PATH_TO_OUTPUT+sp+'/RAxML_distances.dist','r')
	lines = raxmlFD.readlines()
	for l in lines:
		parts = l.strip('\n').split('\t')
		dist = float(parts[1])
		strainA = parts[0].split(' ')[0]
		strainB = parts[0].split(' ')[1]
		if strainA in strains and strainB in strains and dist > maxDist:
			maxDist = dist
	print sp+"\t"+str(maxDist)
	raxmlFD.close()
