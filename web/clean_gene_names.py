from config import *
import os


def validLine(l):
#	digits = any(char.isdigit() for char in l)
	l = l.rstrip()
	nonNucleotide = any(char not in {'A','T','G','C','-','N'} for char in l)
	if nonNucleotide:
		return False
	else:
		return True

errors = []

print printAllArgs()

f = open(PATH_TO_UPLOAD+getCompStrain(),'r')
out = open(PATH_TO_UPLOAD+getCompStrain()+"_clean.fa",'w')
count = 0
for l in f:
	if(l.startswith('>')):
		count+=1
		out.write('>gene'+str(count)+'\n')
	else:
		if validLine(l):
			out.write(l)
		else:
			errors.append(("Error: non nucleotide character in file: ",l))
out.close()

if count < 100:
	errors.append(("Error: Too few genes to compare. Please seperate into genes as per the FASTA format. Number of genes identified: ",str(count)))


fullName = PATH_TO_UPLOAD+getCompStrain()
indexOfEnd = fullName.rfind('.')
if indexOfEnd == -1:
	indexOfEnd = len(fullName)-1
fullName = fullName[:indexOfEnd+1] + '.fa'
os.system('mv '+PATH_TO_UPLOAD+getCompStrain()+"_clean.fa "+ fullName)

if len(errors)>0:
	errorFd = open(PATH_TO_UPLOAD+'cleaning_errors.txt','w')
	if len(errors)>10:
		errors.insert(0,("Printing first 10 errors. Total number of errors: ", str(len(errors))))
		errors = errors[:11]
	for error in errors:
		errorFd.write(error[0] + error[1])
	errorFd.close()