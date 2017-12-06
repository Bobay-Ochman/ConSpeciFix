from config import *
import os

species= getSelectedSpecies('graph_points.txt')

for sp in species:
	h = open(PATH_TO_OUTPUT+sp+'/make_hm_graph_points.R','w')
	toWrite = """png('"""+PATH_TO_OUTPUT+sp+"""/gno2.png' ,width = 6,
  height    = 6,
  units     = "in",
  res       = 200)
par(mfrow=c(1,1))
tab = read.table('"""+PATH_TO_OUTPUT+sp+"""/graph_points.txt')
plot(tab$V1,tab$V2,xlab=c("# Genomes"),ylab=c("h/m"),main='"""+sp+"""')
abline(h=0.108065507964,col="red", lwd=2, lty=2)
abline(h=0.196154000259,col="red", lwd=1, lty=3)
"""
	h.write(toWrite)
	h.close()
	os.system('Rscript '+PATH_TO_OUTPUT+sp+'/make_hm_graph_points.R')

