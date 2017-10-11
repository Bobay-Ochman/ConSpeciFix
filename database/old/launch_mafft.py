from config import *
import os
from multiprocessing import Pool

def launchMafft(sp):
	files = os.listdir(PATH_TO_OUTPUT + sp + '/align/')
	done = []
	files = files[::-1]
	for fichier in files:
		if str(fichier).endswith('.fa.align'):
			#We've already done it, we'll let them know
			done.append(str(fichier).strip('.align'))
			continue

		if str(fichier).strip('a') in done:
			#skip it, we've done it already
			continue
		printLog('starting ' + sp +' ' +str(fichier))
		os.system(MAFFT_PATH+'  ' + PATH_TO_OUTPUT + sp + '/align/' + fichier + '  >   '  + PATH_TO_OUTPUT + sp + '/align/' + fichier + '.align > /dev/null 2>&1')
		printLog('done! w/ ' +sp+ ' '+str(fichier))


if __name__ == '__main__':
	species = giveMulti(getSelectedSpecies())
	p = Pool(MAX_THREADS)
	p.map(launchMafft,species)