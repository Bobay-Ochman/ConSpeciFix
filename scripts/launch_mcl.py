from multiprocessing import Pool
import multiprocessing
import os
from config import *

def mclOnSpec(sp):
	os.system('mv '+PATH_TO_OUTPUT + sp + '/input.txt '+ PATH_TO_OUTPUT + sp + '/input_' + sp + '.txt' )
	os.system('/Users/ochmanlab/Desktop/prog/mcl-14-137/src/shmcl/mcl ' + PATH_TO_OUTPUT + sp + '/input_' + sp + '.txt --abc -I 1.2')
	os.system('mv  out.input_' + sp + '.txt.I12 ' + PATH_TO_OUTPUT + sp + '/')


if __name__ == '__main__':
	species = getSpecies()
	todoSpec = []
	for sp in species:
		try:
			k=open(PATH_TO_OUTPUT + sp + '/input.txt','r')
			todoSpec.append(sp)
		except:
			pass
	species = todoSpec
	print len(species)
	p = Pool(MAX_THREADS)
	p.map(mclOnSpec,species)
