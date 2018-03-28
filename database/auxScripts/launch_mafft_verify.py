from config import *

species = getAllSpecies()
out = open('todo/mafft.txt','w')
for sp in species:
	files = os.listdir(PATH_TO_OUTPUT + sp + '/align/')
	done = []
	files = files[::-1]
	#print files
	for fichier in files:
		fd = open(PATH_TO_OUTPUT + sp + '/align/' + fichier)
		totalLen = len(fd.readlines())
		print sp, fichier, totalLen
		if totalLen == 0 :
			print 
			out.write(sp + '\t' + fichier.strip('.fa.align') + '.fa\n');

out.truncate()
out.close()
