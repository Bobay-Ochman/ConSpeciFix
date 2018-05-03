from multiprocessing import Pool
import multiprocessing
import os
from config import *
import parse_gff

def runTrial(args):
	print args
	myArgs = args.strip('\n').split('\t')
	dbSp = myArgs[0]
	cpSp = myArgs[1]
	ftp = myArgs[2]
	id1 = myArgs[3]
	id2 = myArgs[4]
	strain = id1.split('.fna')[0]

	#make folders
	try:
		os.mkdir(PATH_TO_TRIALS+dbSp)
	except:
		pass
	try:
		os.mkdir(PATH_TO_TRIALS+dbSp+'/'+cpSp)
	except:
		print "Comparison already completed?\t"+args
		return

	#just mention that we were here
	fd = open(PATH_TO_TRIALS+dbSp+'/'+cpSp+'/params.txt','w')
	fd.write(args)
	fd.close()

	#download file into folder		
	os.system('wget '+ftp + '/' + id1)
	os.system('wget '+ftp + '/' + id2)
	os.system('mv '+id1+' '+PATH_TO_TRIALS+dbSp+'/'+cpSp)
	os.system('mv '+id2+' '+PATH_TO_TRIALS+dbSp+'/'+cpSp)
	
	#unzip and parseGFF
	os.system('gunzip '+PATH_TO_TRIALS+dbSp+'/'+cpSp+'/'+id1)
	os.system('gunzip '+PATH_TO_TRIALS+dbSp+'/'+cpSp+'/'+id2)
	parse_gff.parseGffFile(PATH_TO_TRIALS+dbSp+'/'+cpSp+'/'+strain)
	os.system('mv ' + PATH_TO_TRIALS+dbSp+'/'+cpSp+'/'+strain +'.fa '+ PATH_TO_TRIALS+dbSp+'/'+cpSp+'/'+strain)

	#remove the .gff and .fna files
	os.system('rm '+PATH_TO_TRIALS+dbSp+'/'+cpSp+'/'+strain+'.fna')
	os.system('rm '+PATH_TO_TRIALS+dbSp+'/'+cpSp+'/'+strain+'.gff')

	#call web/runner
	runnerArgs = [dbSp,strain,dbSp+'/'+cpSp,'tst@me.com']
	print runnerArgs
	os.system('python web/runner.py '+ ' '.join(runnerArgs))

	#clean up!
	print "completed with: ", '\t'.join(runnerArgs)
	fd = open('todo/complete.txt','a')
	fd.write('\t'.join(runnerArgs)+'\n')
	fd.close()


if __name__ == '__main__':
	p = Pool(16)
	f = open('todo/runner.txt','r')
	args = []
	for l in giveMulti(f.readlines()):
		args.append(l)
	p.map(runTrial,args)
