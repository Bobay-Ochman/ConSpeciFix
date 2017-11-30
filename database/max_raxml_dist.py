from shutil import copyfile
from config import *
from multiprocessing import Pool
import os

for sp in getAllSpecies():
	sampleFD = open(PATH_TO_OUTPUT+sp+'/sample.txt','r')
	strains = []
	maxRAxMLDist = 0
	for l in sampleFD.readlines():
		strains.append(l.strip('\n'))
	for l in open(PATH_TO_OUTPUT+sp+'/RAxML_distances.dist','r').readlines():
		parts = l.strip('\n').split('\t')
		strainA = parts[0].split(' ')[0]
		strainB = parts[0].split(' ')[1]
		if strainA in strains and strainB in strains:
			if float(parts[1]) > maxRAxMLDist:
				maxRAxMLDist = float(parts[1])
	print sp+'\t'+str(maxRAxMLDist)