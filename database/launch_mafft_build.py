from config import *

species = getAllSpecies()
out = open('todo/mafft.txt','w')
out.seek(0)
for sp in species:
	files = os.listdir(PATH_TO_OUTPUT + sp + '/align/')
	if '.DS_Store' in files:
		files.remove('.DS_Store')
	done = []
	files = files[::-1]
	#print files
	for fichier in files:
		if str(fichier).endswith('.fa.align'):
			#We've already done it, we'll let them know
			continue
		if fichier+'.align' not in files:
			out.write(sp + '\t' + fichier + '\n');

out.truncate()
out.close()