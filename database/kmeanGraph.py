from config import *
import os

species=getSelectedSpecies("distrib.txt")

for sp in species:
	print sp
	h=open('kmean_graph.R','w')
	h.write("""require('outliers')

tab=read.table('"""+PATH_TO_OUTPUT+sp+"""/kmeans.txt')
listOfValues= tab$V3

maxVal <- round(max(listOfValues))+1
if ( maxVal > 100){
	maxVal <- 100
}
minVal <- round(min(listOfValues))-1
if (minVal < 0){
	minVal <- 0
}

#calculate our breaks specifically because after removing outliers, breaks will change if defaults are used
ourBreaks <- seq(minVal, maxVal, (maxVal - minVal)/20 )

pdf('"""+PATH_TO_OUTPUT+sp+"""/kmeans.pdf')
#graph of everything. Will be red since the "good ones" will be kept later on and be printed over
p1 <- hist(tab$V3,breaks = ourBreaks,plot = FALSE)

#remove all outliers identified with pvalues of <.001
listOfValues = rm.outlier(listOfValues, fill = FALSE)
pv = chisq.out.test(listOfValues)[3][1]$p.value
while ( pv < .001)
{
	listOfValues = rm.outlier(listOfValues, fill = FALSE)
	pv = chisq.out.test(listOfValues)[3][1]$p.value
}

maxAfterOutliers <- max(listOfValues)
strainsForRemoval <- tab$V1[which(tab$V3 > maxAfterOutliers)]
print(strainsForRemoval)
write(strainsForRemoval,ncol=1,file='"""+PATH_TO_OUTPUT+sp+"""/removal.txt')

#these are just the ones that are members of the species. They get green
p2 <- hist(listOfValues,breaks = ourBreaks,plot = FALSE)

#actually plot the data
plot( p1, col='firebrick1',main = 'Outliers', xlab="frequency of appearance in lower mode",ylab="numb strains")  # first histogram
plot( p2, col='darkolivegreen3', add=T) 

dev.off()""")
	h.truncate()
	h.close()
	os.system("Rscript  kmean_graph.R  ")

os.remove("kmean_graph.R")


