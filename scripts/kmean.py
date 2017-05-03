
import os

species=[]
f=open('../results/species.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	sp=a[0]
	species.append(a[0])

f.close()




for sp in species:
	h=open('kmean.R','w')
	h.write("tab=read.table('../results/distrib/distrib_" + sp + ".txt')\n")
	h.write("toto=kmeans(tab$V2,2)\n")
	h.write("pdf('../results/distrib/Distrib_" + sp + ".pdf')\n")
	h.write("hist(tab$V2,nclass=60)\n")
	h.write("abline(v=toto[2]$centers,col='red')\n")
	h.write("dev.off()\n")
	h.write("write(toto[1]$cluster,ncol=1,file='../results/distrib/vector_" + sp + ".txt')\n\n")
	h.write("write(toto[2]$centers,ncol=2,file='../results/distrib/key_" + sp + ".txt')\n")
	h.close()
	os.system("Rscript  kmean.R  ")






