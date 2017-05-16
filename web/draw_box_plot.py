import os
from config import *

species = getSingleSpecies()

sp = species[0]
h=open(PATH_TO_UPLOAD + "draw.R","w")
h.write("tab=read.table('"+PATH_TO_UPLOAD+"distrib_" + sp + ".txt')\n")
h.write("pdf('"+PATH_TO_UPLOAD+"boxPlot.pdf')\n")
h.write("boxplot(tab$V2[which(tab$V3=='with')],tab$V2[which(tab$V3=='without')])\n")
h.write("dev.off()\n")
h.close()
os.system("Rscript  "+PATH_TO_UPLOAD+"draw.R ")