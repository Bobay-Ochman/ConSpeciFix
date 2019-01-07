from config import *

species=getSelectedSpecies('rm1.txt')

print species


for sp in species:
	k=open(PATH_TO_OUTPUT+sp+'/distrib.txt','w')
	dico={}
	print sp
	f=None
	try:
		f=open(PATH_TO_OUTPUT + sp + '/rm1.txt','r')
	except:
		continue
	for l in f:
		a=l.strip('\n').split('\t')
		strains = a[0].split('&&&')
		nb=len(strains)
		r,m=float(a[1]),float(a[2])  # change to just pull the rm ratio
		if m > 0:
			rm = r/m
			k.write(a[0] + '\t' + str(rm) + '\n')
	f.close()
	k.truncate()
	k.close()

































