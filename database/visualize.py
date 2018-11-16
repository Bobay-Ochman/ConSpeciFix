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

def makeImages(sp):
	fromSave = False
	makeSave = True
	pat = PATH_TO_OUTPUT + sp+'/'

	print(pat)
	print("starting")
	allStrains = []
	for l in open(pat+'sample.txt','r').readlines():
		allStrains.append(l.strip())
	print("have all strains")


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
	#		if lineNumber == 50: #this says only take the first 25 lines. This isn't really enough.
	#			break
			print("on new line " + str(lineNumber))
			for i in range(genomeLength):
				for sac in whatHappened[i]:
					for s1 in sac:
						for s2 in sac:
							if s1 == s2:
								continue
							name = "&&&".join([s1,s2])
							if len(strainMap[name]) == 0:
								strainMap[name] = [0]*genomeLength
							strainMap[name][i] = 1
						# strainMap[s1][i] = 1

	strainGroups = {}
	for strain in allStrains:
		strainGroup = strain.split('-')[0] #split on Dengue1, Dengue2, etc.
		if strainGroup not in strainGroups.keys():
			strainGroups[strainGroup] = []
		strainGroups[strainGroup].append(strain)

	largestStrainGroup = strainGroups.keys()[0]
	for name in strainGroups:
		if len(strainGroups[name]) > len(strainGroups[largestStrainGroup]):
			largestStrainGroup = name

	# largestStrainGroup = 'All_Dengue'
	specialStrains = []
	for strainGroup in strainGroups.keys():
		specialStrains.append(random.sample(strainGroups[strainGroup],1)[0])

	# specialStrains = ['Dengue1-AF180817','Dengue2-KY937188','Dengue2-KY937189','Dengue2-FM210227']

	if not fromSave:
		if makeSave:
			save = open(pat+'mapOfRecombination.txt','w')
			save.write(str(strainMap))
			save.close()

	if fromSave:
		fd = open(pat+'mapOfRecombination.txt','r')
		strainMap = []
		for l in fd.readlines():
			jsonReadable = l.strip().replace("'",'"')
		 	strainMap = json.loads(jsonReadable)

	print("consolidate")
	maxLen = 0
	for spStrain in specialStrains:
		mapToPrint = []
		orderOfStrains = []
		for strainPair in sorted(strainMap.keys()):
			if not strainPair.startswith(spStrain):
				continue
			compStrainName = strainPair.split('&&&')[1]
			if compStrainName == unicode(spStrain):
				continue
			orderOfStrains.append(compStrainName)
			genomeMap = []
			maxLen = int(len(strainMap[strainPair])/100)
			for i in range(maxLen):
				value = sum(strainMap[strainPair][i*100:(i+1)*100])
				genomeMap.append(value)
			mapToPrint.append(genomeMap)
		print orderOfStrains
		print unicode(spStrain)
		print("image")
		# data = np.array(mapToPrint)
		print(len(mapToPrint[0]))
		print(len(mapToPrint))
		w, h = len(mapToPrint[0]), len(mapToPrint)
		data = np.zeros((h, w), dtype=np.uint8)
		for i in range(len(mapToPrint)):
			for j in range(len(mapToPrint[i])):
				data[i, j] = mapToPrint[i][j]+1
		#img = Image.fromarray(data, 'RGB')
		#img.save('zimage_'+spStrain+'_against_population_of_'+largestStrainGroup+'.png')
		print("max data point: " + str(data.max()))
		fig, (ax0) = plt.subplots(1,1)
		plt.xticks(np.arange(0,maxLen,step = 20), np.arange(0,maxLen*100,step = 20*100))
		plt.yticks(np.arange(0,len(mapToPrint),step=1), orderOfStrains)
		c = ax0.pcolor(data,norm=LogNorm(vmin=1, vmax=data.max()),cmap='GnBu')
		plt.tick_params(axis='y', which='major', labelsize=3)
		spStrain = spStrain.split('.fa')[0]
		ax0.set_title(spStrain+' against population of '+largestStrainGroup)
		cbar = fig.colorbar(c, ax=ax0,ticks=[1,int((data.max()+1) / 2), data.max()])
		cbar.ax.set_yticklabels([0,int((data.max()) / 2), data.max()])  
		plt.savefig(pat+'image_'+spStrain+'_v_pop_'+largestStrainGroup+'.pdf')

def wrapper(f):
	try:
		makeImages(f)
	except:
		print('ERROR WITH !!!!!!! ' + str(f))

if __name__ == '__main__':
    args = getAllSpecies()
    args = giveMulti(args)
    p = Pool(MAX_THREADS)
    p.map(makeImages, args)





