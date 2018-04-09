import os

myPath = '/Users/ochmanlab/Desktop/ConSpeciFix/env/work/Ochman/brian/databaseQuerySpecies/'

#target='/Volumes/APE_MacPro_External_2/brian/databaseComp/'
target='/Volumes/APE_MacPro_External_2/brian/databaseQuerySnapshot/'

interesting = {}

for trial in os.listdir(myPath):
	if trial == '.DS_Store':
		continue
	print trial
	allFiles = os.listdir(myPath+trial)
	going = False
	for f in allFiles:
		if 'testGraph' in f:
			going = True
	if going:
		os.mkdir(target+trial)
		for f in allFiles:
			os.system('cp '+myPath+trial+'/'+f+' ' + target+trial+'/'+f)