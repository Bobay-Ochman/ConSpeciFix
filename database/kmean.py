from config import *
import os

species=getSelectedSpecies("distrib.txt")

for sp in species:
	print sp
	h=open('kmean.R','w')
	h.write("tab=read.table('"+PATH_TO_OUTPUT+sp +"/distrib.txt')\n")
	h.write("toto=kmeans(tab$V2,2)\n")
	h.write("pdf('"+PATH_TO_OUTPUT+sp +"/Distrib.pdf')\n")
	h.write("hist(tab$V2,nclass=60)\n")
	h.write("abline(v=toto[2]$centers,col='red')\n")
	h.write("dev.off()\n")
	h.write("write(toto[1]$cluster,ncol=1,file='"+PATH_TO_OUTPUT+sp +"/vector.txt')\n\n")
	h.write("write(toto[2]$centers,ncol=2,file='"+PATH_TO_OUTPUT+sp +"/key.txt')\n")
	h.close()
	os.system("Rscript  kmean.R  ")

os.remove("kmean.R")


