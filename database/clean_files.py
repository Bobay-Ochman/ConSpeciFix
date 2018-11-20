import os
import sys

def validLine(l):
#	digits = any(char.isdigit() for char in l)
	l = l.rstrip()
	nonNucleotide = sum(char not in {'A','T','G','C','-','N'} for char in l)
	total = len(l)
	return (nonNucleotide,total)


def cleanFile(fileName, path_to_orig, path_to_dest):
	errors = []
	strainName = fileName
	if strainName.startswith('.') or '.DS_Store' in strainName or '_conspecifix' in strainName or 'results.txt' in strainName or 'cleaning_errors' in strainName:
		return
	fullName = '1_'
	if strainName.endswith('.fa'):
		fullName = strainName
	else:
		fullName = strainName+ '.fa'

	f = open(path_to_orig+strainName,'r')
	out = open(path_to_dest+fullName,'w')
	count = 0
	totalLen = 0.0
	totalNonNucleotide = 0.0
	maxGeneLen = 0
	geneLen = 0
	cumulativeLine = []
	for l in f:
		if(l.startswith('>')):
			count+=1
			if len(cumulativeLine) != 0:
				cumulativeLine.append('\n')
				out.write(str(''.join(cumulativeLine)))
			out.write('>gene'+strainName+'-'+str(count)+'\n')
			cumulativeLine = []
			if geneLen > maxGeneLen:
				maxGeneLen = geneLen
			geneLen = 0
		else:
			countOfValid = validLine(l)
			totalNonNucleotide += countOfValid[0]
			totalLen += countOfValid[1]
			geneLen += countOfValid[1]
			cumulativeLine.append(l.rstrip())
	out.write(str(''.join(cumulativeLine)))	
	if totalNonNucleotide / totalLen > .1:
		errors.append(("Error: too many non-nucleotide characters in file: ",str(totalNonNucleotide)+' non-nucleotide to '+str(totalLen)+' total'))
	if maxGeneLen > 30000:
		errors.append(("Error: longest gene is > 30kbp. Are your genes annotated? Max len: ",str(maxGeneLen)))

	out.close()

	if count < 0:
		errors.append(("Error: too few genes to compare. Please seperate into genes as per the FASTA format. Number of genes identified: ",str(count)))

	if len(errors)>0:
		errorFd = open(path_to_orig+'cleaning_errors.txt','a')
		if len(errors)>10:
			errors.insert(0,("Printing first 10 errors. Total number of errors: ", str(len(errors))))
			errors = errors[:11]
		for error in errors:
			errorFd.write('File:'+strainName+'\t'+error[0] + error[1]+'\n')
		errorFd.close()
