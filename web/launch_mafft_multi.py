from config import *
import os
from multiprocessing import Pool

def launchMafft(args):

	sp = args.split('\t')[0]
	fichier= args.split('\t')[1].strip('\n')
	print PATH_TO_UPLOAD + 'align/' + fichier

	os.system(MAFFT_PATH+' --quiet ' + PATH_TO_UPLOAD + 'align/' + fichier + '  >   '  + PATH_TO_UPLOAD + 'align/'+ fichier + '.align')

if __name__ == '__main__':

	p = Pool(MAX_THREADS)
	f = open(PATH_TO_UPLOAD + 'todo/mafft.txt','r')
	args = []
	for l in f:
		args.append(l)
	args = giveMulti(args)
	p.map(launchMafft,args)

	#> /dev/null 2>&1