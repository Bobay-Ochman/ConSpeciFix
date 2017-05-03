import os
import os.path
from config import *

species = getSingleSpecies()
#species = ['Escherichia_coli']
file = open(PATH_TO_UPLOAD+'todo/parse_gff.txt','w')

for sp in species:
	listOfFiles = os.listdir(PATH_TO_UPLOAD)
	for f in listOfFiles:
		if f.endswith('.gff'):
			f = f.strip('.gff')
			if(os.path.isfile(PATH_TO_UPLOAD+'genes/' + f + '.fa')):
				print 'skipping: '  + sp + ' '+f
			else:
				print 'doing: ' + sp + ' '+f
				file.write(sp + '\t' + f + '\n')
