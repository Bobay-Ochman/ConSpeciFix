

import os

species=[]
f=open('../results/species.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	sp=a[0]
	species.append(sp)


f.close()

kick={}
tag={}
h=open("../results/criterion.txt","w")
for sp in species:
	kick[sp]=[]
	tag[sp]="no"
	f=open("../results/distrib/kmeans_" + sp + ".txt","r")
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


h=open('../results/modification.txt','w')
for sp in species:
	print sp," ",tag[sp]
	h.write(sp + "\t" + tag[sp] + "\t" + "\t".join(kick[sp]) + "\n")

h.close()
