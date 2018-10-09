from config import *
import os
import sys
from multiprocessing import Pool


def validLine(l):
#	digits = any(char.isdigit() for char in l)
	l = l.rstrip()
	nonNucleotide = sum(char not in {'A','T','G','C','-','N'} for char in l)
	total = len(l)
	return (nonNucleotide,total)


def cleanFile(arg):
	errors = []
	strainName = arg
	print strainName
	if strainName == '.DS_Store' or strainName == '_conspecifix':
		return
	f = open(PATH_TO_FOLDER+strainName,'r')
	out = open(PATH_TO_FOLDER+strainName+"_clean.fa",'w')
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

	fullName = '1_'
	if strainName.endswith('.fa'):
		fullName = PATH_TO_FOLDER+strainName
	else:
		fullName = PATH_TO_FOLDER+strainName+ '.fa'
	os.system('mv '+PATH_TO_FOLDER+strainName+' '+PATH_TO_MAT+'orig/'+strainName)
	os.system('mv '+PATH_TO_FOLDER+strainName+"_clean.fa "+ fullName)

	if len(errors)>0:
		errorFd = open(PATH_TO_FOLDER+'cleaning_errors.txt','a')
		if len(errors)>10:
			errors.insert(0,("Printing first 10 errors. Total number of errors: ", str(len(errors))))
			errors = errors[:11]
		for error in errors:
			errorFd.write('File:'+strainName+'\t'+error[0] + error[1]+'\n')
		errorFd.close()


if __name__ == '__main__':
	print 'args: '+str(sys.argv)
	p = Pool(MAX_THREADS)
	print 'Starting! with '+ str(MAX_THREADS) + ' threads.'
	filesToProcess = os.listdir(PATH_TO_FOLDER)
	p.map(cleanFile,filesToProcess)

