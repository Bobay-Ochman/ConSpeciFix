import os
from config import *
import sys

#https://www.ncbi.nlm.nih.gov/genomes/Genome2BE/genome2srv.cgi?action=download&orgn=&report=proks&status=50|40|30|20|%3Bnopartial|noanomalous|&group=--%20All%20Prokaryotes%20--&subgroup=--%20All%20Prokaryotes%20--&format=

species = []
dico,info={},{}
f=open("genomes_proks.txt","r")
for l in f:
	if l[0] != "#":
		a=l.strip("\n").split("\t")
		b = a[0].split(" ")
		if len(b) > 1 and b[1] != "sp.":
			sp = b[0] + "_" + b[1]
			if "Candidatus_" not in sp and "_cluster" not in sp and "_group" not in sp:
				if dico.has_key(sp):
					dico[sp]+=1
					info[sp].append(l.strip("\n"))
				else:	
					dico[sp]=1
					info[sp]=[l.strip("\n")]
					species.append(sp)

f.close()

speciesForComparison = []
for sp in getAllSpecies(database = True):
	for compSp in species:
		familyC = compSp.split("_")[0]
		familyA = sp.split("_")[0]
		if familyA == familyC:
			if sp != compSp:
				speciesForComparison.append(compSp)

print "Total= ",len(speciesForComparison)


bestDownload = {}
for sp in speciesForComparison:
	minScafold = sys.maxsize
	bestLine = None
	for l in info[sp]:
		a=l.strip("\n").strip("\r").split("\t")
		scafolds = int(a[12]) #How many scafolds	
		if(scafolds < minScafold):
			minScafold = scafolds
			bestLine = l
	bestDownload[sp] = bestLine

download = open('todo/download.txt','w')

for sp in speciesForComparison:
	a = bestDownload[sp].strip("\n").strip("\r").split("\t")
	print a
	tmp=[]
	for stuff in a:
		if 'ftp://' in stuff:
			tmp.append(stuff)
	if len(tmp) > 0:
		#print sp
		ftp = tmp[0]
		id1 = ftp.split('/')[-1] + '_genomic.fna.gz'
		id2 = ftp.split('/')[-1] + '_genomic.gff.gz'
		
		download.write('wget ' + ftp + '/' + id1 + '\t')
		download.write('wget ' + ftp + '/' + id2  + '\t')
		download.write('mv  ' + id1 + '    ' + PATH_TO_QUERY_SPEC + sp + '/genomes/' + '\t')
		download.write('mv  ' + id2 + '    ' + PATH_TO_QUERY_SPEC + sp + '/genomes/' + '\n')
			
download.truncate()
download.close()


#### Make folders to recieve the things

for sp in speciesForComparison:
	try:
		os.mkdir(PATH_TO_QUERY_SPEC + sp )
	except OSError:
		pass
	try:
		for folder in getFolders():
			os.mkdir(PATH_TO_QUERY_SPEC + sp + folder)
	except OSError:
		pass
















