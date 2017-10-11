from config import *

h=open(PATH_TO_MAT + "graph.R",'w')

h.write("pdf('"+PATH_TO_MAT+'gno1'+ ".pdf')\n")
h.write("par(mfrow=c(1,1))\n")
h.write(  "tab = read.table('"+PATH_TO_MAT + "graph.txt',h=T)\n")
h.write('w=c(tab$Nb,rev(tab$Nb))\n')
h.write('v=c(tab$Median-tab$SD,rev(tab$Median + tab$SD))\n')
h.write('plot(100,100,cex=0.5,cex.main=0.8,xlim=c(3,max(w)),ylim=c(0,max(v) + 0.1),xlab=c("# Genomes"),ylab=c("h/m"),main="Analysis")\n')
h.write('polygon(w,v,col="gray88",border=NA)\n')
h.write('points(tab$Nb,tab$Median,pch=16,cex=0.3,t="b")\n')
h.write("dev.off()\n\n")
h.close()



