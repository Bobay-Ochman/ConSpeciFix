from config import *

species = getSelectedSpecies()
out = open('todo/mafft.txt','w')
for sp in species:
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
		out.write(sp + '\t' + fichier + '\n');
out.close()