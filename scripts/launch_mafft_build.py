from config import *

species = getSelectedSpecies()
#species = ['Achromobacter_xylosoxidans']
out = open('todo/mafft.txt','w')
out.seek(0)
for sp in species:
	files = os.listdir(PATH_TO_OUTPUT + sp + '/align/')
	done = []
	files = files[::-1]
	#print files
	for fichier in files:
		#print done
		if str(fichier).endswith('.fa.align'):
			#We've already done it, we'll let them know
			continue
		if fichier+'.align' not in files:
			out.write(sp + '\t' + fichier + '\n');
out.truncate()
out.close()
