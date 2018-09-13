import os
from config import *
import sys

#https://www.ncbi.nlm.nih.gov/genomes/Genome2BE/genome2srv.cgi?action=todoList&orgn=&report=proks&status=50|40|30|20|%3Bnopartial|noanomalous|&group=--%20All%20Prokaryotes%20--&subgroup=--%20All%20Prokaryotes%20--&format=

species = []
dico,info={},{}
f=open("../genomes_proks.txt","r")
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


besttodoList = {}
for sp in speciesForComparison:
	minScafold = sys.maxsize
	bestLine = None
	for l in info[sp]:
		a=l.strip("\n").strip("\r").split("\t")
		if a[12] == '-':
			a[12] = sys.maxsize
		scafolds = int(a[12]) #How many scafolds	
		if(scafolds < minScafold):
			minScafold = scafolds
			bestLine = l
	besttodoList[sp] = bestLine

todoList = open('todo/runner.txt','w')

for sp in speciesForComparison:
	a = besttodoList[sp].strip("\n").strip("\r").split("\t")
	tmp=[]
	for stuff in a:
		if 'ftp://' in stuff:
			tmp.append(stuff)
	if len(tmp) > 0:
		ftp = tmp[0]
		id1 = ftp.split('/')[-1] + '_genomic.fna.gz'
		id2 = ftp.split('/')[-1] + '_genomic.gff.gz'
		
		for databaseSp in getAllSpecies(database = True):
			if sp.split('_')[0] == databaseSp.split('_')[0] and sp!=databaseSp:
				todoList.write('\t'.join([databaseSp,sp,ftp, id1,id2]) +'\n')
			
todoList.truncate()
todoList.close()






