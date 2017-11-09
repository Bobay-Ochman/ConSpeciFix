from config import *
import os

species=getSelectedSpecies("geneSubsetHMVals.txt")

"""+PATH_TO_OUTPUT+sp+"""

for sp in species:
	print sp
	h=open('graphPointWithBox.R','w')
	h.write("""png('"""+PATH_TO_OUTPUT+sp+"""/gno2_box.png' ,width = 6,
  height    = 6,
  units     = "in",
  res       = 200)
par(mfrow=c(1,1))
tab = read.table('"""+PATH_TO_OUTPUT+sp+"""/graph_points.txt')
secTab = read.table('"""+PATH_TO_OUTPUT+sp+"""/geneSubsetHMVals.txt',h=T)
w=tab$V1
v=tab$V2

overallMax <- max(v)
if(overallMax < max(secTab$hmRatio)){
	overallMax <- max(secTab$hmRatio)
}
overallMax + 0.1

par(fig=c(0,.85,0,1), new=TRUE)
plot(tab$V1,tab$V2,main='"""+sp+"""',cex=0.5,cex.main=0.8,xlim=c(3,max(w)),ylim=c(0,overallMax),xlab=c("# Genomes"),ylab=c("h/m"),plot=FALSE)
points(tab$Nb,tab$Median,pch=16,cex=0.3,t="b")
abline(h=0.108065507964,col="red", lwd=2, lty=2)
abline(h=0.196154000259,col="red", lwd=1, lty=3)

par(fig=c(0.65,1,0,1),new=TRUE)
boxplot(hmRatio~size, data=secTab,ylim=c(0,overallMax),axes=FALSE,xlab="end result with\nresampled core")

dev.off()""")
	h.truncate()
	h.close()
	os.system("Rscript graphPointWithBox.R  ")

os.remove("graphPointWithBox.R")


