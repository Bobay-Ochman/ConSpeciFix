from config import *
import os

species=getSingleSpecies()

kick={}
tag={}
h=open(PATH_TO_UPLOAD + "criterion.txt","w")
for sp in species:
	kick[sp]=[]
	tag[sp]="no"
	f = None
	try:
		f=open(PATH_TO_UPLOAD +"kmeans_" + sp + ".txt","r")
	except:
		continue
	for l in f:
		a=l.strip('\n').split('\t')
		st = a[0]
		if st != "tot":
			mode1,mode2=float(a[1]),float(a[3])
			tot=mode1+mode2
			ratio = mode2/tot
			if ratio ==0:
				print sp,' ',st
				kick[sp].append(st)
				tag[sp]="y"
			h.write(sp + "\t" + st + "\t" + str(ratio) + "\n")
	f.close()


h=open(PATH_TO_UPLOAD + 'modification.txt','w')
critInfoFD = open(PATH_TO_UPLOAD+'crit_stats.txt','a')
critInfoFD.write('Member of Species according to Exclusion Criterion*')
for sp in species:
	print sp," ",tag[sp]
	h.write(sp + "\t" + tag[sp] + "\t" + "\t".join(kick[sp]) + "\n")
	if tag[sp]=="no":
		critInfoFD.write(sp+': yes')
	else:
		critInfoFD.write(sp+': no')
critInfoFD.write('\n\n*Please refer to Bobay & Ochman, GBE 2017')
h.close()
critInfoFD.close()
