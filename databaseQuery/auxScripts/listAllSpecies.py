import os
from config import *
import sys

#https://www.ncbi.nlm.nih.gov/genomes/Genome2BE/genome2srv.cgi?action=download&orgn=&report=proks&status=50|40|30|20|%3Bnopartial|noanomalous|&group=--%20All%20Prokaryotes%20--&subgroup=--%20All%20Prokaryotes%20--&format=

def genusName(strName):
	return strName.split("_")[0]


def getSize():
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

	print len(species)

	speciesForComparison = []
	totalCompPerGenome = {}
	for sp in getAllSpecies(database = True):
		familyA = genusName(sp)
		if not familyA in totalCompPerGenome:
			totalCompPerGenome[familyA] = 0
			for compSp in species:
				familyC = genusName(compSp)
				if familyA == familyC:
					if sp != compSp:
						speciesForComparison.append(compSp)
						totalCompPerGenome[familyA] += 1
	print "Total= ",len(speciesForComparison)
	return totalCompPerGenome












