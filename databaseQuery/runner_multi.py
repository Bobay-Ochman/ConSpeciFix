from multiprocessing import Pool
import multiprocessing
import os
import time
from config import *
import parse_gff

def runTrial(args):
	print args
	myArgs = args.strip('\n').split('\t')
	dbSp = myArgs[0] # name of database species
	cpSp = myArgs[1] # name of new species
	strain = myArgs[2]
	trialNumber = myArgs[3]
	#make folders
	destFolder = dbSp+'/'+cpSp+'_'+str(trialNumber)
	try:
		os.mkdir(PATH_TO_TRIALS+dbSp)
	except:
		pass
	try:
		os.mkdir(PATH_TO_TRIALS+destFolder)
	except:
		print "Comparison already completed?\t"+args
		return

	#just mention that we were here
	fd = open(PATH_TO_TRIALS+destFolder+'/params.txt','w')
	fd.write(args)
	fd.close()
		
	#unzip and parseGFF
	os.system('cp ' + PATH_TO_DATABASE+cpSp+'/genes/'+strain+' '+ PATH_TO_TRIALS+destFolder+'/'+strain)

	#call web/runner
	runnerArgs = [dbSp,strain,destFolder,'tst@me.com']
	print runnerArgs
	os.system('python web/runner.py '+ ' '.join(runnerArgs))

	#clean up!
	print "completed with: ", '\t'.join(runnerArgs)
	fd = open('todo/complete.txt','a')
	fd.write('\t'.join(runnerArgs)+'\n')
	fd.close()


if __name__ == '__main__':
	p = Pool(5)
	f = open('todo/runner.txt','r')
	args = []
	for l in giveMulti(f.readlines()):
		args.append(l)
	print "Starting! on: "+str(len(args))
	p.map(runTrial,args)
