from multiprocessing import Pool
import multiprocessing
import os
from config import *

def downloadFile(args):
	commands = args.strip('\n').split('\t');
	for com in commands:
		os.system(com)
	

if __name__ == '__main__':
	species = getSpecies()
	#processSpec('Escherichia_coli','GCF_000299455.1_ASM29945v1_genomic.gff')
	print multiprocessing.cpu_count()
	p = Pool(3)
	f = open('todo/download.txt','r')
	args = []
	for l in f.readlines():
		args.append(l)
	p.map(downloadFile,args)
	