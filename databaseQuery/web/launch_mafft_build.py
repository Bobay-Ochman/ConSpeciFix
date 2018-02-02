from config import *

species = getSingleSpecies()
out = open(PATH_TO_UPLOAD+'todo/mafft.txt','w')
out.seek(0)
for sp in species:
	files = os.listdir(PATH_TO_UPLOAD + 'align/')
	done = []
	files = files[::-1]
	#print files
	for fichier in files:
		#print done
		if str(fichier).endswith('.fa.align'):
			done.append(str(fichier))
	for fichier in files:
		if str(fichier)+'.align' not in done:
			out.write(sp + '\t' + fichier + '\n');
out.truncate()
out.close()
