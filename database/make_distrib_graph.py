from config import *
import os

species=getSelectedSpecies("distrib.txt")

for sp in species:
	print sp
	h=open(PATH_TO_OUTPUT+sp+'/kmean.R','w')
	toWrite = """tab=read.table('"""+PATH_TO_OUTPUT+sp+"""/distrib.txt')
toto=kmeans(tab$V2,2)
png('"+PATH_TO_OUTPUT+sp +"/Distrib.png', width = 6,
  height    = 6,
  units     = "in",
  res       = 400)
hist(tab$V2,nclass=60)
abline(v=toto[2]$centers,col='red')
dev.off()
write(toto[1]$cluster,ncol=1,file='"""+PATH_TO_OUTPUT+sp+"""/vector.txt')
write(toto[2]$centers,ncol=2,file='"""+PATH_TO_OUTPUT+sp+"""/key.txt')
"""
	h.write(toWrite)
	h.close()
	os.system("Rscript "+PATH_TO_OUTPUT+sp+"/kmean.R  ")

