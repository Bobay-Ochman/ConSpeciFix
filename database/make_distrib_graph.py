from config import *
import os

species=getSelectedSpecies("distrib.txt")

for sp in species:
	print sp
	h=open(PATH_TO_OUTPUT+sp+'/make_distrib_graph.R','w')
	toWrite = """tab=read.table('"""+PATH_TO_OUTPUT+sp+"""/distrib.txt',sep = "\\t")
toto=kmeans(tab$V2,2)
png('"""+PATH_TO_OUTPUT+sp +"""/distrib.png', width = 6,
  height    = 6,
  units     = "in",
  res       = 200)
hist(tab$V2,nclass=60,main="Frequency of ratios", xlab="h/m", ylab="Frequency")
abline(v=toto[2]$centers,col='red')
dev.off()
write(toto[1]$cluster,ncol=1,file='"""+PATH_TO_OUTPUT+sp+"""/vector.txt')
write(toto[2]$centers,ncol=2,file='"""+PATH_TO_OUTPUT+sp+"""/key.txt')
"""
	h.write(toWrite)
	h.close()
	os.system("Rscript "+PATH_TO_OUTPUT+sp+"/make_distrib_graph.R  ")

