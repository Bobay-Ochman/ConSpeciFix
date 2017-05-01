import os
import multiprocessing
import sys
import platform

PATH_TO_OUTPUT = '/Volumes/ITDR/brian/results/'
PATH_TO_SPECIES_TXT = "../species.txt"
MAX_THREADS = multiprocessing.cpu_count()
MAX_SPECIES_SIZE = 500

USEARCH_PATH = 'usearch61'
MAFFT_PATH = 'mafft'
MCL_PATH = ''

TACC = (platform.processor() != 'i386')

if(TACC):
	PATH_TO_OUTPUT = '/work/03414/be4833/out/results/'
	MCL_PATH = '/work/03414/be4833/local/bin/mcl'
	MAX_THREADS = 4
	MAFFT_PATH = '/work/03414/be4833/bin/mafft'

WEB = True

if(WEB):
	PATH_TO_OUTPUT = '/work/03414/be4833/out/results/'
	MCL_PATH = '/work/03414/be4833/local/bin/mcl'
	MAX_THREADS = 4
	MAFFT_PATH = '/work/03414/be4833/bin/mafft'


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
		
def getSpecies():
	species=[]
	f=open(PATH_TO_SPECIES_TXT,"r")
	for l in f:
		species.append(l.strip("\n").split('\t')[0])
	f.close()
	species = list(species)
	return species
	
def getSelectedSpecies():
	"""
	species=[]
	f=open('../selected_species.txt','r')
	for l in f:
		a=l.strip('\n').split('\t')
		species.append(a[0])
	f.close()
	return species
	"""
	ret = []
	spec = getSpecies()
	for sp in spec:
		try:
			h = open(PATH_TO_OUTPUT + sp + '/orthologs.txt')
			h.close()
			ret.append(sp)
		except:
			continue
	return ret
	
def getSpeciesOfSize(maxSize):
	ret = []
	masterLen = getGenomes(getSpecies())
	for sp in getSpecies():
		if len(masterLen[sp])<maxSize:
			ret.append(sp)
	return ret
	
def getGenomes(species):
	dico = {}
	for sp in species:
		dico[sp] = os.listdir(PATH_TO_OUTPUT + sp+'/genes')
	return dico

def getFolders():
	return []
	#return ['/genes','/genomes','/align', '/phylo','/BBH']
	

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
	
	
	
########################################################################
import math

 
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

