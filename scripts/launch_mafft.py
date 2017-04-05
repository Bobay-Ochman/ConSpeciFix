from config import *
import os

species=[]
#these are just the species that have had their core genome completed and sorted out
f=open('../selected_species.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	species.append(a[0])

f.close()


for sp in species:
	files = os.listdir(PATH_TO_OUTPUT + sp + '/align/')
	for fichier in files:
		os.system('mafft   ' + PATH_TO_OUTPUT + sp + '/align/' + fichier + '  >   '  + PATH_TO_OUTPUT + sp + '/align/' + fichier + '.align')
