import os

myPath = '/Volumes/APE_MacPro_External_2/brian/databaseCompExport/'

#target='/Volumes/APE_MacPro_External_2/brian/databaseComp/'
target = '/Volumes/APE_MacPro_External_2/brian/databaseCompExport2/'


for trial in os.listdir(myPath):
	if trial == '.DS_Store':
		continue
	print trial
	allFiles = os.listdir(myPath+trial)
	os.mkdir(target+trial)
	for f in allFiles:
		if not ('genomic' in f and not 'genomic.fa' in f):
			os.system('cp '+myPath+trial+'/'+f+' ' + target+trial+'/'+f)
