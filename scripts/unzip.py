import os
from config import *
from multiprocessing import Pool

species = getSpecies()

print species

def unzip(sp):
	listOfFiles = os.listdir(PATH_TO_OUTPUT + sp + '/genomes')
	print sp + ' ' + str(len(listOfFiles))
	for f in listOfFiles:
		if f.endswith('.gz'):
			print sp + ' ' + f
			os.system('gunzip ' + PATH_TO_OUTPUT + sp + '/genomes/'+ f)



if __name__ == '__main__':
	species = giveMulti(getSpecies())
	print species
	p = Pool(MAX_THREADS)
	p.map(unzip,species)