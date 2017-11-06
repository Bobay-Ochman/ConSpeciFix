from multiprocessing import Pool
import multiprocessing
import os
from config import *

def downloadFile(args):
	commands = args.strip('\n').split('\t');
	for com in commands:
		os.system(com)
	

if __name__ == '__main__':
	species = getAllSpecies(database = False)
	print multiprocessing.cpu_count()
	p = Pool(1)#Instead of using MAX_THREADS, we are limited by bandwidth
	f = open('todo/download.txt','r')
	args = []
	for l in giveMulti(f.readlines()):
		args.append(l)
	p.map(downloadFile,args)
	