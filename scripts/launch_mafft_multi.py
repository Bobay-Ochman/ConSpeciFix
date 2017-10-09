from config import *
import os
from multiprocessing import Pool

def launchMafft(args):

	sp = args.split('\t')[0]
	fichier= args.split('\t')[1].strip('\n')
	print sp, fichier
	os.system(MAFFT_PATH+'  ' + PATH_TO_OUTPUT + sp + '/align/' + fichier + '  >   '  + PATH_TO_OUTPUT + sp + '/align/' + fichier + '.align')

if __name__ == '__main__':

	p = Pool(MAX_THREADS)
	f = open('todo/mafft.txt','r')
	args = []
	for l in f:
		args.append(l)

	args = giveMulti(args)
	p.map(launchMafft,args)