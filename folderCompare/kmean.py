from config import *
import os

h=open(PATH_TO_MAT + 'kmean.R','w')
h.write("tab=read.table('"+PATH_TO_MAT+"distrib.txt')\n")
h.write("toto=kmeans(tab$V2,2)\n")
h.write("pdf('"+PATH_TO_MAT+"Distrib.pdf')\n")
h.write("hist(tab$V2,nclass=60)\n")
h.write("abline(v=toto[2]$centers,col='red')\n")
h.write("dev.off()\n")
h.write("write(toto[1]$cluster,ncol=1,file='"+PATH_TO_MAT+"vector.txt')\n\n")
h.write("write(toto[2]$centers,ncol=2,file='"+PATH_TO_MAT+"key.txt')\n")
h.close()

