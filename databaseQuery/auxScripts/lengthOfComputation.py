import os

myPath = '/Users/ochmanlab/Desktop/ConSpeciFix/env/work/Ochman/brian/databaseQuerySpecies/'

#target='/Volumes/APE_MacPro_External_2/brian/databaseComp/'

interesting = {}
alldirs = []
i = 0
for trial in os.listdir(myPath):
	if trial == '.DS_Store':
		continue
	i+=1
	if os.path.isfile(myPath+trial+'/criterion.txt'):
		allFiles = os.listdir(myPath+trial+'/out')
		minTimeStamp = 1920575909.0
		maxTimeStamp = 0
		for f in allFiles:
			thisTS = os.path.getmtime(myPath+trial+'/out/'+f)
			if thisTS > maxTimeStamp:
				maxTimeStamp = thisTS
			if thisTS < minTimeStamp:
				minTimeStamp = thisTS
		duration = maxTimeStamp - minTimeStamp
		alldirs.append(duration)
		alldirs = sorted(alldirs)
		if i %100 == 15:
			print '-------'
			print 'avg', str(sum(alldirs)/((len(alldirs)*60.0)))
			print 'max',max(alldirs)/60.0
			print 'min',min(alldirs)/60.0
			print 'Q1 ', alldirs[int(len(alldirs)/4)]/60.0
			print 'Q2 ', alldirs[int(len(alldirs)/2)]/60.0
			print 'Q3 ', alldirs[int(len(alldirs)*3.0/4)]/60.0