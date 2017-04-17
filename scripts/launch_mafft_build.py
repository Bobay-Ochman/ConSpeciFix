from config import *

species = getSelectedSpecies()
species = ['Achromobacter_xylosoxidans']
out = open('todo/mafft.txt','w')
out.seek(0)
for sp in species:
	files = os.listdir(PATH_TO_OUTPUT + sp + '/align/')
	done = []
	files = files[::-1]
	for fichier in files:
		if str(fichier).endswith('.fa.align'):
			#We've already done it, we'll let them know
			#done.append(str(fichier).strip('.align'))
			continue
		if str(fichier).strip('a') in done:
			#skip it, we've done it already
			continue
		out.write(sp + '\t' + fichier + '\n');
out.truncate()
out.close()
