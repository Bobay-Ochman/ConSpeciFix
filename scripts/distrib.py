from config import *

species=getSpecies()

print species


for sp in species:
	k=open(PATH_TO_OUTPUT+sp+'/distrib_' + sp + '.txt','w')
	dico={}
	print sp
	f=None
	try:
		f=open(PATH_TO_OUTPUT + sp + '/rm1.txt','r')
	except:
		continue
	for l in f:
		a=l.strip('\n').split('\t')
		strains = a[0].split('-')
		nb=len(strains)
		r,m=float(a[1]),float(a[2])
		if m > 0:
			rm = r/m
			if nb >= 10:
				k.write(a[0] + '\t' + str(rm) + '\n')
	f.close()
	k.close()

































