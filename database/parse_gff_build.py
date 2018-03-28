import os
import os.path
from config import *

species = getSpecies()
#species = ['Acinetobacter_baumannii']
file = open('todo/parse_gff.txt','w')
for sp in species:
	listOfFiles = os.listdir(PATH_TO_OUTPUT + sp + '/genomes')
	for f in listOfFiles:
		if f.endswith('.gff'):
			f = f.strip('.gff')
			if(os.path.isfile(PATH_TO_OUTPUT + sp + "/genes/" + f + '.fa')):
				print 'skipping: '  + sp + ' '+f
			else:
				print 'doing: ' + sp + ' '+f
				file.write(sp + '\t' + f + '\n')
file.truncate()
file.close()