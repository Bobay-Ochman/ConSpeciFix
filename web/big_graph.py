from config import *


species= getSingleSpecies()
h=open(PATH_TO_UPLOAD + "graph.R",'w')

NB,nb=1,0
for sp in species:
	nb+=1
	if nb == 1:
		h.write("pdf('"+PATH_TO_UPLOAD+'testGraph' + ".pdf') \n")
		h.write("par(mfrow=c(1,1))\n")
	h.write(  "tab = read.table('"+PATH_TO_UPLOAD + "graph.txt',h=T) \n")
	h.write('w=c(tab$Nb,rev(tab$Nb))\n')
	h.write('v=c(tab$Median-tab$SD,rev(tab$Median + tab$SD))\n')
	h.write('plot(100,100,cex=0.5,cex.main=0.8,xlim=c(3,max(w)),ylim=c(0,max(v) + 0.1),xlab=c("# Genomes"),ylab=c("h/m"),main="Testing strain against ' + sp + '")\n')
	h.write('polygon(w,v,col="gray88",border=NA)\n')
	h.write('points(tab$Nb,tab$Median,pch=16,cex=0.3,t="b")\n')
	h.write('abline(h=0.108065507964,col="red", lwd=2, lty=2)\n')
	h.write('abline(h=0.196154000259,col="red", lwd=1, lty=3)\n')
	if nb == 1:
		nb = 0
		NB+=1
		h.write("dev.off()\n\n")

h.write("dev.off()\n\n")

h.close()



