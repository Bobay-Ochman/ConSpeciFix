from config import *
import os

species=getSingleSpecies()

sp = species[0]
print sp

h=open(PATH_TO_UPLOAD + 'make_kmean_graph.R','w')
h.write("""

install.packages("outliers", repos="https://cloud.r-project.org")

require('outliers')

tab=read.table('"""+PATH_TO_UPLOAD+"""kmeans.txt')
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

png('"""+PATH_TO_UPLOAD+"""hmGraph.png' ,width = 6,
  height    = 6,
  units     = "in",
  res       = 200)
#graph of everything. Will be red since the "good ones" will be kept later on and be printed over
p1 <- hist(tab$V3,breaks = ourBreaks,plot = FALSE)

#remove all outliers identified with pvalues of <.0001
flag = TRUE
while ( chisq.out.test(listOfValues)[3][1]$p.value < .0001 && flag)
{
	oldlistOfValues = listOfValues
	listOfValues = rm.outlier(listOfValues, fill = FALSE)
	if(min(oldlistOfValues) != min(listOfValues)){
		flag = FALSE
		listOfValues = oldlistOfValues
	}
}

maxAfterOutliers <- max(listOfValues)
strainsForRemoval <- tab$V1[which(tab$V3 > maxAfterOutliers)]
strainsForRemoval = as.character(strainsForRemoval)
print(strainsForRemoval)
write(strainsForRemoval,ncol=1,file='"""+PATH_TO_UPLOAD+"""for_removal.txt')

#these are just the ones that are members of the species. They get green
p2 <- hist(listOfValues,breaks = ourBreaks,plot = FALSE)

#actually plot the data
plot( p1, col='firebrick1',main = 'Outliers', xlab="frequency of appearance in lower mode",ylab="numb strains")  # first histogram
plot( p2, col='darkolivegreen3', add=T) 

dev.off()""")

h.truncate()
h.close()
os.system("Rscript "+PATH_TO_UPLOAD+"make_kmean_graph.R  ")

