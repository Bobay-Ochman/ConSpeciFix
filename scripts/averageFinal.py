from scipy import stats
from config import *


toDelete = open("todo/toDelete.txt",'w')

for specName in getSelectedSpecies():

	fs = open("/Volumes/ITDR/brian/results/"+specName+"/distrib_"+specName+".txt")
	lines = fs.readlines()
	dico = {}
	goodGenomes = []
	allGenomes = []
	maxSize = 0
	allLargeFamilyHMs = []

	#identify the number of genomes
	#get list of all genomes
	for line in lines:
		parts = line.split('\t')
		lables = parts[0].split('&&&')
		hm = float(parts[1])
		size = len(lables)
		if(size > maxSize):
			maxSize = size
		allGenomes += lables

	maxAllowableSize = maxSize - 3;
	allGenomes = list(set(allGenomes))

	#build the "all large sample hms"
	for line in lines:
		parts = line.split('\t')
		lables = parts[0].split('&&&')
		hm = float(parts[1])
		size = len(lables)
		if(size > maxAllowableSize):
			allLargeFamilyHMs.append(hm)
	allLargeFamilyHMs.sort()


	#find the minimum p value (where the lists are most extremly different) from the list of all hm values
	minPValue = 1
	minPValueIndex = -1
	#2 here is arbitrary and should probably be algorithmically produced.
	for i in range(2,len(allLargeFamilyHMs)-2):
		pval = stats.ttest_ind(allLargeFamilyHMs[0:i],allLargeFamilyHMs[i:])[1]
		if(pval < minPValue):
			minPValue = pval
			minPValueIndex = i
	smallHMs = allLargeFamilyHMs[0:minPValueIndex]
	bigHMs = allLargeFamilyHMs[minPValueIndex:] # we assume that the best HM values will always put us over here

	for line in lines:
		parts = line.split('\t')
		lables = parts[0].split('&&&')
		hm = float(parts[1])
		size = len(lables)
		if(size == maxSize-1):
			if hm in bigHMs:
				goodGenomes+=lables

	#remove duplicates
	goodGenomes = list(set(goodGenomes))

	# #no go through and print all the bad genomes
	# if(len(goodGenomes) == len(allGenomes) or  len(goodGenomes) == 0):
	# 	print 'No issues! Everything is a member of the species' 
	# 	exit()

	oneSegment = []
	for lable in allGenomes:
		if lable in goodGenomes:
			oneSegment.append(lable)

	secondSegment = []
	for lable in allGenomes:
		if lable not in goodGenomes:
			secondSegment.append(lable)

	if(len(oneSegment) == 0 or len(secondSegment) == 0):
		print "no issue with " +specName
	else:
		segment = []
		if(len(oneSegment) < len(secondSegment)):
			segment = oneSegment
		else:
			segment = secondSegment
		print specName
		print minPValue
		print len(allGenomes)
		print allLargeFamilyHMs
		for label in segment:
			print "\t" + label
			toDelete.write(specName+"\t"+label+"\n")
toDelete.close()








