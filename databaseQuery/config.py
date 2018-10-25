
import os
import multiprocessing
import sys
import platform
import math


############### VARIABLES USERS WILL NEED TO CHANGE ###############


#Path to output should be followed by a tailing slash
#This is where the full database will be built,
# and if all the species are being processed,
# this can be upwards of 500GB
PATH_TO_TRIALS = '/stor/work/Ochman/brian/entroCross/'
PATH_TO_DATABASE = '/stor/work/Ochman/brian/compDB/'

#your local instalations for the following programs,
# or simply the name of the program if it can be accessed from the command line
# for example
# RAXML_PATH = '/Users/Admin/programs/standard-RAxML-master/raxmlHPC-SSE3'
# We have all of ours on our path as the following names
USEARCH_PATH = '/stor/home/be4833/usearch6.1.544_i86linux32' 
MAFFT_PATH = 'mafft'
MCL_PATH = 'mcl'
RAXML_PATH = 'raxml'


############### VARIABLES USERS MIGHT NEED TO CHANGE ###############


# Used on larger jobs where all work is linear, or in cases like
# RAXML where the binaries themselves are optomized for multithreading
MAX_THREADS = multiprocessing.cpu_count()

#Used to ignore species that would take computationally very long times
MAX_SPECIES_SIZE = 500


############### Things users will not need to change ###############

PATH_TO_TRIALS = '/' + PATH_TO_TRIALS.strip('/') + '/'
PATH_TO_DATABASE = '/' + PATH_TO_DATABASE.strip('/') + '/'

PATH_TO_SPECIES_TXT = "../species.txt"


def giveMulti(list):
	rank = 0
	worldSize = 1
	if len(sys.argv) == 3:
		rank = int(sys.argv[1])
		worldSize = int(sys.argv[2])
	ret = []
	for l in list[rank::worldSize]:
		ret.append(l)
	return ret

def printLog(string):
	string = str(string)
	if len(sys.argv) == 3:
		print '***'+str(sys.argv[1]) + ' ' + string
	else:
		print '*** '+string
		
def getSelectedSpecies(file,database):
	ret = []
	spec = getAllSpecies(database)
	for sp in spec:
		try:
			h = None
			if(database):
				h = open(PATH_TO_DATABASE + sp+'/' + file)
			else:
				h = open(PATH_TO_TRIALS + sp+'/' + file)
			h.close()
			ret.append(sp)
		except:
			continue
	return ret
	
def getAllSpecies(database):
	allSpec = []
	if database:
		allSpec = os.listdir(PATH_TO_DATABASE)
	else:
		allSpec = os.listdir(PATH_TO_TRIALS)
	i = 0
	while i < len(allSpec):
		if allSpec[i] == '.DS_Store' or allSpec[i] == 'big_graph.R' or any(char.isdigit() for char in allSpec[i]):
			del allSpec[i]
			i-=1
		i+=1
	return allSpec
	
def getGenomes(species,database):
	dico = {}
	for sp in species:
		if database:
			dico[sp] = os.listdir(PATH_TO_DATABASE + sp+'/genes')
		else:
			dico[sp] = os.listdir(PATH_TO_TRIALS + sp+'/genes')
	return dico

def getFolders():
	return ['/genes','/genomes','/align','/BBH']
	

########################################################################
def translate(seq):
	d={}
	d["TTT"],d["TTC"],d["TTA"],d["TTG"]="F","F","L","L"
	d["CTT"],d["CTC"],d["CTA"],d["CTG"]="L","L","L","L"
	d["ATT"],d["ATC"],d["ATA"],d["ATG"]="I","I","I","M"
	d["GTT"],d["GTC"],d["GTA"],d["GTG"]="V","V","V","V"
	d["TCT"],d["TCC"],d["TCA"],d["TCG"]="S","S","S","S"
	d["CCT"],d["CCC"],d["CCA"],d["CCG"]="P","P","P","P"
	d["ACT"],d["ACC"],d["ACA"],d["ACG"]="T","T","T","T"
	d["GCT"],d["GCC"],d["GCA"],d["GCG"]="A","A","A","A"
	d["TAT"],d["TAC"],d["TAA"],d["TAG"]="Y","Y","*","*"
	d["CAT"],d["CAC"],d["CAA"],d["CAG"]="H","H","Q","Q"
	d["AAT"],d["AAC"],d["AAA"],d["AAG"]="N","N","K","K"
	d["GAT"],d["GAC"],d["GAA"],d["GAG"]="D","D","E","E"
	d["TGT"],d["TGC"],d["TGA"],d["TGG"]="C","C","*","W"
	d["CGT"],d["CGC"],d["CGA"],d["CGG"]="R","R","R","R"
	d["AGT"],d["AGC"],d["AGA"],d["AGG"]="S","S","R","R"
	d["GGT"],d["GGC"],d["GGA"],d["GGG"]="G","G","G","G"
	i=0
	tmp=[]
	while i in range(len(seq)-3):
		codon= seq[i:i+3]
		if codon not in d.keys():
			tmp.append("X")
		else:
			tmp.append(d[codon])
			if d[codon]=="*":
				break
		i += 3
	prot="".join(tmp)
	return	prot
 
def mean( echantillon ) :
    size = len( echantillon )
    moyenne = float(sum( echantillon )) / float(size)
    return moyenne


def stat_variance( echantillon ) :
    n = float(len( echantillon )) # taille
    mq = mean( echantillon )**2
    s = sum( [ x**2 for x in echantillon ] )
    variance = s / n - mq
    return variance


def stat_ecart_type( echantillon ) :
    variance = stat_variance( echantillon )
    ecart_type = math.sqrt( variance )
    return ecart_type

def median( echantillon) :
	echantillon.sort()
	size = len( echantillon )
	if len(echantillon)==0:
		M=0
	elif len( echantillon ) % 2 == 0:
		M= float(echantillon[size / 2 - 1] + echantillon[size / 2]) / 2
	else:
		M= echantillon[size / 2]
	return M

def ninetyfive( echantillon) :
	echantillon.sort()
	size = len( echantillon )
	i95 = int( float(size) * 95/100 ) - 1
	return echantillon[i95]




########################################################################

def rev_comp( seq ):
	new_seq=""
	SEQ = seq[::-1]
	SEQ = SEQ.upper()
	for B in SEQ:
		if B == "G":
			new_seq+="C"
		elif B == "C":
			new_seq+="G"
		elif B == "A":
			new_seq+="T"
		elif B == "T":
			new_seq+= "A"
		elif B == "R":
			new_seq+="Y"
		elif B == "S" or B == "W" or B == "N":
			new_seq += B
		elif B == "Y":
			new_seq+="R"
		elif B == "K":
			new_seq += "M"
		elif B == "M":
			new_seq+="K"
		elif B == "B":
			new_seq+="V"
		elif B == "V":
			new_seq += "B"
		elif B == "D":
			new_seq+="H"
		elif B =="H":
			new_seq+="D"
		else:
			print "!!! ",B
	return new_seq

