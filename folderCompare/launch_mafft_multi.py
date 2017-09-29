from config import *
import os
from multiprocessing import Pool

def launchMafft(args):
	fichier= args.strip('\n')
	os.system(MAFFT_PATH+' ' + PATH_TO_MAT + 'align/' + fichier + '  >   '  + PATH_TO_MAT + 'align/' + fichier + '.align')

if __name__ == '__main__':
	p = Pool(MAX_THREADS)
	f = open(PATH_TO_TODO + 'mafft.txt','r')
	args = []
	for l in f:
		args.append(l)
	p.map(launchMafft,args)