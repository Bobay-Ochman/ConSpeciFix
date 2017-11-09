from config import *
import os

species= getSelectedSpecies('graph.txt')

for sp in species:
	h = open(PATH_TO_OUTPUT+sp+'/make_hm_graph.R','w')
	toWrite = """png('"""+PATH_TO_OUTPUT+sp+"""/gno1.png' ,width = 6,
  height    = 6,
  units     = "in",
  res       = 200)
par(mfrow=c(1,1))
tab = read.table('"""+PATH_TO_OUTPUT+sp+"""/graph.txt',h=T)
w=c(tab$Nb,rev(tab$Nb))
v=c(tab$Median-tab$SD,rev(tab$Median + tab$SD))
plot(100,100,cex=0.5,cex.main=0.8,xlim=c(3,max(w)),ylim=c(0,max(v) + 0.1),xlab=c("# Genomes"),ylab=c("h/m"),main='"""+sp+"""')
polygon(w,v,col="gray88",border=NA)
points(tab$Nb,tab$Median,pch=16,cex=0.3,t="b")
abline(h=0.108065507964,col="red", lwd=2, lty=2)
abline(h=0.196154000259,col="red", lwd=1, lty=3)
"""
	h.write(toWrite)
	h.close()
	os.system('Rscript '+PATH_TO_OUTPUT+sp+'/make_hm_graph.R')

