from config import *
import os


def validLine(l):
#	digits = any(char.isdigit() for char in l)
	l = l.rstrip()
	nonNucleotide = sum(char not in {'A','T','G','C','-','N'} for char in l)
	total = len(l)
	return (nonNucleotide,total)

errors = []

print printAllArgs()

f = open(PATH_TO_UPLOAD+getCompStrain(),'r')
out = open(PATH_TO_UPLOAD+getCompStrain()+"_clean.fa",'w')
count = 0
totalLen = 0.0
totalNonNucleotide = 0.0
maxGeneLen = 0
geneLen = 0
for l in f:
	if(l.startswith('>')):
		count+=1
		out.write('>gene'+str(count)+'\n')
		if geneLen > maxGeneLen:
			maxGeneLen = geneLen
		geneLen = 0
	else:
		countOfValid = validLine(l)
		totalNonNucleotide += countOfValid[0]
		totalLen += countOfValid[1]
		geneLen += countOfValid[1]
		out.write(l)
if count < 2:
	errors.append(("Error: too few genes to compare. Please seperate into genes as per the FASTA format. Number of genes identified: ",str(count)))

if totalLen > 0 and totalNonNucleotide / totalLen > .1:
	errors.append(("Error: too many non-nucleotide characters in file: ",str(totalNonNucleotide)+' non-nucleotide to '+str(totalLen)+' total'))

if maxGeneLen > 30000:
	errors.append(("Error: longest gene is > 30kbp. Are your genes annotated? Max len: ",str(maxGeneLen)))

out.close()



fullName = PATH_TO_UPLOAD+getCompStrain().split('.fa')[0] + '.fa'
os.system('mv '+PATH_TO_UPLOAD+getCompStrain()+"_clean.fa "+ fullName)

if len(errors)>0:
	errorFd = open(PATH_TO_UPLOAD+'cleaning_errors.txt','w')
	if len(errors)>10:
		errors.insert(0,("Printing first 10 errors. Total number of errors: ", str(len(errors))))
		errors = errors[:11]
	for error in errors:
		errorFd.write(error[0] + error[1]+'\n')
	errorFd.close()