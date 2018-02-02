from multiprocessing import Pool
import multiprocessing
import os
from config import *

def runTrial(args):
	try:
		os.system('python '+ args)	
		f = open('todo/complete.txt','a')
		f.write(args+'\n')
		f.close()
	except:
		print 'Error '+args


if __name__ == '__main__':
	p = Pool(16)
	f = open('todo/runner.txt','r')
	args = []
	for l in giveMulti(f.readlines()):
		args.append(l)
	args = args[200:201]
	p.map(runTrial,args)
	