from config import *
import numpy as np
import json
import random
import os
from multiprocessing import Pool
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import unicodedata
import copy

def makeImages(sp):
	fromSave = False
	pat = PATH_TO_OUTPUT + sp+'/'

	#automatically pull from save file if it exists
	if os.path.isfile(pat+'mapOfRecombination.txt'):
		fromSave = True

	#start by loading all of the strain names from samples.txt
	print(pat)
	print("starting")
	allStrains = []
	for l in open(pat+'sample.txt','r').readlines():
		allStrains.append(l.strip())
	print("have all strains")


	#build a map of the whole genome for every strain A&&&B, and if the index at that point
	#was a 'n', 'm', 'r' for no change, mutation, or recombination.
	#This is built from the visual.txt file and will be print to mapOfRecombination.txt

	if not fromSave:
		strainMap = {}
		for s1 in allStrains:
			print(s1)
			for s2 in allStrains:
				if s1 == s2:
					continue
				name = "&&&".join([s1,s2])
			#strainMap[s1] = []
				strainMap[name] = []
		print("built strain map")

		print(len(strainMap))

		fd = open(pat+'visual.txt','r')
		lineNumber = 0
		for l in fd.readlines():
			jsonReadable = l.strip().replace("'",'"')
			whatHappened = json.loads(jsonReadable)
			genomeLength = len(whatHappened)
			print(genomeLength)
			lineNumber += 1
			# go through every line, which is a H/m comparison of N genomes
			# and for each location containing the genomes, look if the sites
			# contain n,m,or r.
			print("on new line " + str(lineNumber))
			for i in range(genomeLength):
				for testResult in whatHappened[i]:
					RorM = testResult[0]
					sac = testResult[1]
					for s1 in sac:
						for s2 in sac:
							if s1 == s2:
								continue
							name = "&&&".join([s1,s2])
							if len(strainMap[name]) == 0:
								strainMap[name] = ['n']*genomeLength
							if RorM == 'r':
								strainMap[name][i] = 'r'
							else:
								if strainMap[name][i] != 'r':
									strainMap[name][i] = 'm'

	
	specialStrains = allStrains
	largestStrainGroup = sp
	
	#save the work, becauase it takes forevery to make this map
	if not fromSave:
		save = open(pat+'mapOfRecombination.txt','w')
		save.write(str(strainMap))
		save.close()

	# load it from save if we already made it
	if fromSave:
		fd = open(pat+'mapOfRecombination.txt','r')
		strainMap = []
		for l in fd.readlines():
			jsonReadable = l.strip().replace("'",'"')
		 	strainMap = json.loads(jsonReadable)

	# make a seperate 'totals' list. Can be used in combination with MCL to
	# make subgroups of the given strains and split them into bits.
	# not super duper related to making maps, but useful to produce here
	# while we have the full map loaded into memory
	strainTotals = {}
	for i in strainMap:
		print i
		strainTotals[i] = sum( [1 for z in strainMap[i] if z== 'r'] )
	out = open(pat+'totalsOfRecombination.txt','w')
	for i in strainTotals:
		put = '\t'.join(str(i).split('&&&')) +'\t'+str(strainTotals[i])
		print put 
		out.write(put+'\n')
	out.close()
	

	#get the ordering from RAxML so we can sort via philogony
	raxmlFile = open(pat+'RAxML_parsimonyTree.dist','r')
	totalSortedOrder = []
	for l in raxmlFile.readlines():
		totalSortedOrder = l.replace('(',"").replace(')','').replace(';',"").strip().split(',')
	print totalSortedOrder

	trimmedSortedOrder = []
	for strain in totalSortedOrder:
		if strain in allStrains:
			trimmedSortedOrder.append(strain)

	print("consolidate")
	maxLen = 0
	totalTally = []
	
	#actually start making the maps
	for spStrain in specialStrains:
		sortedOrder = copy.copy(trimmedSortedOrder)
		sortedOrder.remove(spStrain)		
		mapToPrint = [[]]*len(sortedOrder)
		orderOfStrains = []
		for strainPair in sorted(strainMap.keys()):
			if not strainPair.startswith(spStrain):
				continue
			compStrainName = strainPair.split('&&&')[1]
			if compStrainName == unicode(spStrain):
				continue
			orderOfStrains.append(compStrainName)
			genomeMap = []
			maxLen = int(len(strainMap[strainPair])/BUCKET_SIZE)
			
			if len(totalTally) < maxLen:
				totalTally = [[]] * maxLen

			for i in range(maxLen):
				recombs = [(z=='r') for z in strainMap[strainPair][i*BUCKET_SIZE:(i+1)*BUCKET_SIZE]]
				mutations = [(z=='m') for z in strainMap[strainPair][i*BUCKET_SIZE:(i+1)*BUCKET_SIZE]]
				hmRate = 0
				if (sum(mutations)) != 0:
					hmRate = (sum(recombs)+0.0)/sum(mutations)
				genomeMap.append(hmRate)
				totalTally[i].append(hmRate)
			try:
				compName = unicodedata.normalize('NFKD', compStrainName).encode('ascii','ignore')
			except TypeError:
				compName = compStrainName

			insertIndex = sortedOrder.index(compName)
			mapToPrint[insertIndex] = genomeMap
		# data = np.array(mapToPrint)
		for i in range(len(mapToPrint)):
			if len(mapToPrint[i]) == 0:
				mapToPrint[i] = [0] * maxLen
		print(maxLen)
		print(len(mapToPrint))
		w, h = maxLen, len(mapToPrint)
		data = np.zeros((h, w), dtype=np.float64)
		for i in range(len(mapToPrint)):
			for j in range(len(mapToPrint[i])):
				data[i, j] = mapToPrint[i][j]+1
		#img = Image.fromarray(data, 'RGB')
		#img.save('zimage_'+spStrain+'_against_population_of_'+largestStrainGroup+'.png')
		print("max data point: " + str(data.max()))
		fig, (ax0) = plt.subplots(1,1)
		tickNames = [str(s) for s in np.arange(0,maxLen*BUCKET_SIZE,step = max(int(maxLen/10)/10,1))]  
		plt.xticks(np.arange(0,maxLen,step = int(maxLen/10)),tickNames )
		plt.yticks(np.arange(0,len(mapToPrint),step=1), sortedOrder)
		c = ax0.pcolor(data,norm=LogNorm(vmin=1, vmax=data.max()),cmap='GnBu')
		plt.tick_params(axis='y', which='major', labelsize=3)
		spStrain = spStrain.split('.fa')[0]
		plt.xlabel("kbp")
		ax0.set_title(spStrain+' against population of '+largestStrainGroup)
		tickLabels = []
		for i in range(9):
			tickLabels.append(int((data.max()-1)*(i/8.0)*BUCKET_SIZE)/float(BUCKET_SIZE))
		labelThings = [mark+1 for mark in tickLabels]
		print tickLabels
		print data.max(),data.min()
		print labelThings
		cbar = fig.colorbar(c, ax=ax0, ticks = labelThings)
		#cbar.formatter = LogFormatterExponent(base=10) # 10 is the default
		cbar.ax.set_yticklabels(tickLabels)  
		plt.savefig(pat+'maps/image_'+spStrain+'_v_pop_'+largestStrainGroup+'.pdf')
		plt.close()
	tallyToPrint = []
	for arr in totalTally:
		tallyToPrint.append(sum(arr)/(len(arr)+0.0))
	print tallyToPrint
	plt.plot(tallyToPrint)
	plt.title('recombination instances found across entire genome')
	plt.ylabel('count totals')
	plt.xticks(np.arange(0,maxLen,step = int(maxLen/10)),tickNames)
	plt.savefig(pat+'maps/overall.pdf')

def wrapper(f):
	try:
		makeImages(f)
	except Exception as e:
		print('ERROR WITH !!!!!!! ' + str(f)+"\n"+str(e))

if __name__ == '__main__':
    args = getAllSpecies()
    args = giveMulti(args)
    p = Pool(MAX_THREADS)
    p.map(wrapper, args)





