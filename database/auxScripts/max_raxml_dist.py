from shutil import copyfile
from config import *
from multiprocessing import Pool
import os



def testDist(fileName):
	maxRAxMLDist = 0
	total = 0.0
	count = 0
	for l in open(fileName,'r').readlines():
		parts = l.strip('\n').split('\t')
		strainA = parts[0].split(' ')[0]
		strainB = parts[0].split(' ')[1]
		if strainA in strains and strainB in strains:
			total+=float(parts[1])
			count+=1
			if float(parts[1]) > maxRAxMLDist:
				maxRAxMLDist = float(parts[1])
	if count == 0:
		count = 1
	return maxRAxMLDist,(total/count)

fd = open('raxmlDistance.csv','w')
fd.write('species,strain count,maxDist,avgDist\n')
for sp in getAllSpecies():
	sampleFD = open(PATH_TO_OUTPUT+sp+'/sample.txt','r')
	strains = []
	for l in sampleFD.readlines():
		strains.append(l.strip('\n'))
	file = PATH_TO_OUTPUT+sp+'/RAxML_distances.dist'
	maxRAxMLDist,avg = testDist(file)
	if(maxRAxMLDist == 0):
		maxRAxMLDist,avg = testDist(PATH_TO_OUTPUT+sp+'/old_RAxML_distances.dist')
	printArr = [sp,str(len(strains)),str(maxRAxMLDist),str(avg)]
	print '\t'.join(printArr)
	fd.write(','.join(printArr)+'\n')

fd.truncate()
fd.close()