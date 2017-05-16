import os
from config import *

species = getSingleSpecies()

for sp in species:
	h=open(PATH_TO_UPLOAD + "draw.R","w")
	h.write("tab=read.table('"+PATH_TO_UPLOAD+"kmeans_" + sp + ".txt')\n")
	h.write("finpoint=tail(tab,1)\n")
	h.write("tab=head(tab,-1)\n")
	h.write("pdf('"+PATH_TO_UPLOAD+"dessin_" + sp + ".pdf')\n")
	h.write("v=1:length(tab$V1)\n")
	h.write("plot(tab$V5,pch=16,type='h',cex=0.7,ylim=c(0,100),ylab='%',xlab=('Strains'),col='grey')\n")
	h.write("points(finpoint$V5,col='red',pch=16)")
	h.write("dev.off()\n")
	h.close()
	os.system("Rscript  "+PATH_TO_UPLOAD+"draw.R ")