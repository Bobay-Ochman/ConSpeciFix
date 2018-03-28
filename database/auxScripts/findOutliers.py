from config import *
import numpy as np

def outliers_iqr(elements):
	sd = np.std(elements, axis=0)
	final_list = [x for x in elements if (x > mean + 2*sd)] #only care about outliers above
	return final_list



species=getSelectedSpecies('rm1.txt')

for sp in species:
	print sp
	f=None
	try:
		f=open(PATH_TO_OUTPUT + sp + '/rm1.txt','r')
	except:
		print "ERROR OPENING FILE!"
	rms = {}
	for l in f:
		a=l.strip('\n').split('\t')
		strains = a[0].split('&&&')
		nb=len(strains)
		r,m=float(a[1]),float(a[2])  # change to just pull the rm ratio
		if m > 0:
			rm = r/m
			if nb >= 10:
				if nb in rms:
					rms[nb].append(rm)
				else:
					rms[nb] = [rm]
	if not rms:
		pass
	else:
		for sizeOfRMComps in rms:
			elements = np.array(rms[sizeOfRMComps])
			mean = np.mean(elements, axis=0)
			outliers = outliers_iqr(elements)
			if mean < .5 and len(outliers)>1:
				print sizeOfRMComps, len(rms[sizeOfRMComps]), mean
				print outliers
	f.close()

































