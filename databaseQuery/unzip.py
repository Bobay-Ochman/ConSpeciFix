import os
from config import *
from multiprocessing import Pool


def unzip(sp):
	listOfFiles = os.listdir(PATH_TO_QUERY_SPEC + sp + '/genomes')
	for f in listOfFiles:
		if f.endswith('.gz'):
			os.system('gunzip ' + PATH_TO_QUERY_SPEC + sp + '/genomes/'+ f)



if __name__ == '__main__':
	species = getAllSpecies(False)
	p = Pool(MAX_THREADS)
	p.map(unzip,species)