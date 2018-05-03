import os
from multiprocessing import Pool
import multiprocessing


myPath = '/Volumes/APE_MacPro_External_2/brian/databaseComp/'

target='/Volumes/APE_MacPro_External_2/brian/databaseToDo/'

interesting = {}


def procTrial(trial):
	if '.DS_Store' in trial:
		return
	print trial
	allFiles = os.listdir(myPath+trial)
	print allFiles
	if len(allFiles) < 4:
		os.mkdir(target+trial)
		for f in allFiles:
			os.system('cp '+myPath+trial+'/'+f+' ' + target+trial+'/'+f)


if __name__ == '__main__':
	p = Pool(4)
	trials = os.listdir(myPath)
	print "going!"
	p.map(procTrial,trials)