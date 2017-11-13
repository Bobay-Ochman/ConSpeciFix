from config import *

species=getSingleSpecies()

sp = species[0]
k=open(PATH_TO_UPLOAD + 'distrib_' + sp + '.txt','w')
dico={}
print sp
f=None
try:
	f=open(PATH_TO_UPLOAD + 'rm1.txt','r')
except:
	print 'Major problem! Cant open rm1.txt'
for l in f:
	a=l.strip('\n').split('\t')
	strains = a[0].split('&&&')
	nb=len(strains)
	rm = 0
	try:
		rm = float(a[3])
	except:
		continue
	tag = "without"
	if str(getCompStrain()+'.fa') in strains:
		tag = "with"
	if nb >= 10:
		k.write(a[0] + '\t' + str(rm) +'\t'+tag+'\n')
f.close()
k.close()







