import os
from config import *

species = getSingleSpecies()

sp = species[0]
h=open(PATH_TO_UPLOAD + "draw.R","w")
h.write("tab=read.table('"+PATH_TO_UPLOAD+"distrib_" + sp + ".txt')\n")

h.write("tabwout = tab$V2[which(tab$V3=='without')]\n")
h.write("tabw = tab$V2[which(tab$V3=='with')]\n")
h.write("W = wilcox.test(tabw,tabwout)[1]$statistic\n")
h.write("P = wilcox.test(tabw,tabwout)[3]$p.value\n")
h.write("t = t.test(v,w)[1]$statistic\n")
h.write("Pt =  t.test(v,w)[3]$p.value\n")
h.write("longlab= paste('Wilcoxon test: W=',W,'P=',P,'/n','t test: t=',t,'P=',Pt,sep=' ')\n")

h.write("pdf('"+PATH_TO_UPLOAD+"boxPlot.pdf')\n")

h.write("boxplot(tabwout,tabw,pch=16,cex=0.7,main='"+sp+"',sub=longlab,ylab ='h/m',names=c('Without Test Genome','With Test Genome'))\n")
h.write("dev.off()\n")
h.close()
os.system("Rscript  "+PATH_TO_UPLOAD+"draw.R ")


#wilcox.test(v,w)