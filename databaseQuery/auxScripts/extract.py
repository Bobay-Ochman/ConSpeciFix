import os

myPath = '/Users/ochmanlab/Desktop/ConSpeciFix/env/work/Ochman/brian/databaseQuerySpecies/'

#target='/Volumes/APE_MacPro_External_2/brian/databaseComp/'
target='/Volumes/APE_MacPro_External_2/brian/databaseCompExport/'

interesting = {}

for trial in os.listdir(myPath):
	if trial == '.DS_Store':
		continue
	print trial
	allFiles = os.listdir(myPath+trial)
	os.mkdir(target+trial)
	for f in allFiles:
		if 'testGraph' in f or 'params' in f or ('genomic' in f and not 'genomic.fa' in f) or 'crit_stats' in f:
			print f
			os.system('cp '+myPath+trial+'/'+f+' ' + target+trial+'/'+f)
