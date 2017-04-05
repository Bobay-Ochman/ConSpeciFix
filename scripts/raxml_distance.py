from config import *
import os

species=[]
f=open('../selected_species.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	species.append(a[0])

f.close()


for sp in species:
	os.system('/Users/ochmanlab/Desktop/prog/standard-RAxML-master/raxmlHPC -f x -p 12345 -s ' + PATH_TO_OUTPUT+ sp + '/concat85.fa  -m GTRGAMMA -n dist')
	os.system('mv RAxML_distances.dist   '+PATH_TO_OUTPUT+ sp +'/distances.dist')
	os.system('rm RA*')






