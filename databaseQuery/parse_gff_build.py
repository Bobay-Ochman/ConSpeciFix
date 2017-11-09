import os
import os.path
from config import *

species = getAllSpecies(False)
#species = ['Escherichia_coli']
file = open('todo/parse_gff.txt','w')
for sp in species:
	listOfFiles = os.listdir(PATH_TO_QUERY_SPEC + sp + '/genomes')
	for f in listOfFiles:
		if f.endswith('.gff'):
			f = f.strip('.gff')
			if(os.path.isfile(PATH_TO_QUERY_SPEC + sp + "/genes/" + f + '.fa')):
				print 'skipping: '  + sp + ' '+f
			else:
				print 'doing: ' + sp + ' '+f
				file.write(sp + '\t' + f + '\n')
file.truncate()
file.close()