from config import *

k=open(PATH_TO_MAT+'distrib.txt','w')
dico={}
f=None
try:
	f=open(PATH_TO_MAT + 'rm1.txt','r')
except Exception as e:
	print 'error', str(e)

for l in f:
	a=l.strip('\n').split('\t')
	strains = a[0].split('&&&')
	nb=len(strains)
	r,m=float(a[1]),float(a[2])  # change to just pull the rm ratio
	if m > 0:
		rm = r/m
		if nb >= 10:
			k.write(a[0] + '\t' + str(rm) + '\n')
f.close()
k.close()
































