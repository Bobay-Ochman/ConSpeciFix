require('outliers')

tab=read.table('kmeans.txt')
listOfValues= tab$V3

maxVal <- round(max(listOfValues))+1
if ( maxVal > 100){
	maxVal <- 100
}
minValue <- round(min(listOfValues))-1
ourBreaks <- seq(minValue, maxVal, (maxVal - minValue)/20 )

pdf('kmeans.pdf')
#par(mfrow = c(2,2))
p1 <- hist(tab$V3,breaks = ourBreaks,plot = FALSE)


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

p2 <- hist(listOfValues,breaks = ourBreaks,plot = FALSE)
plot( p1, col='firebrick1',main = 'Outliers', xlab="frequency of appearance in lower mode",ylab="numb strains")  # first histogram
plot( p2, col='darkolivegreen3', add=T) 

dev.off()
