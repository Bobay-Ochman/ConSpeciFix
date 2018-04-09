from multiprocessing import Pool
import multiprocessing
import os
from config import *
from random import shuffle

def runTrial(args):
	try:
		path = PATH_TO_QUERY_SPEC+args.split(' ')[3]+'/BBH'
		if not os.path.isdir(path): 
			os.system('python '+ args)	
			f = open('todo/complete.txt','a')
			f.write(args+'\n')
			f.close()
		else:
			print "is done! "+ args
	except:
		print 'Error '+args


if __name__ == '__main__':
	p = Pool(16)
	f = open('todo/runner.txt','r')
	args = []
	for l in giveMulti(f.readlines()):
		args.append(l)
	p.map(runTrial,args)
