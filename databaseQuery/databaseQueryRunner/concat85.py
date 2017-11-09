from config import *
import os

species = getSingleSpecies()
strains=getStrains(species)

specialStrain = getCompStrain()+'.fa'
strains[species[0]].append(specialStrain)

genes={}
orthologues={}
for sp in species:
	genes[sp]=[]
	orthologues[sp]={}
	f=open( PATH_TO_UPLOAD + 'orthologs.txt',"r")
	for l in f:
		a=l.strip("\n").split("\t")
		orthologues[sp][a[0]]=a[1:]
		genes[sp].append(a[0])
	f.close()

parent={}
for sp in species:
	for st in strains[sp]:
		if st != specialStrain:
			#print 'normal strain'
			f=open(PATH_TO_OUTPUT + sp + '/genes/' + st,"r")
		else:
			#print 'special strain'
			f=open(PATH_TO_UPLOAD + st,"r")
		for l in f:
			if l[0] == ">":
				id = l.strip("\n").strip(">").split(" ")[0]
				if parent.has_key(id):
					print "PROBLEM !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				parent[id] = st
		f.close()

exclusion=[]



tmp={}
for sp in species:
	tmp[sp]={}
	for ortho in genes[sp]:
		print sp, ortho
		f=open( PATH_TO_UPLOAD + 'align/'  + ortho + ".fa.align","r")
		memo=[]
		maxLen = 0;
		for l in f:
			if l[0] == ">":
				id = l.strip("\n").strip(">").split(" ")[0]
				st = parent[id]
				memo.append(st)
				if tmp[sp].has_key(st):
					pass
				else:
					tmp[sp][st]=''
			else:
				tmp[sp][st]+=(l.strip("\n").upper())
				longueur = len(tmp[sp][st])
				if longueur > maxLen:
					maxLen = longueur
		f.close()
		for st in strains[sp]:
			if tmp[sp].has_key(st):
				pass
			else:
				tmp[sp][st]=[]
			if len(tmp[sp][st]) < maxLen:
				while len(tmp[sp][st]) < maxLen:
					#print st, ' ',len(tmp[sp][st]),' ',longueur
					tmp[sp][st]+='-'


concat={}
for sp in species:
	concat[sp]={}
	for id in tmp[sp]:
		concat[sp][id] = tmp[sp][id]

tmp={}


try:
	for sp in species:
		h=open(PATH_TO_UPLOAD + 'concat85.fa',"w")
		for st in strains[sp]:
			h.write(">" + st + "\n")
			i=0
			while i < len(concat[sp][st]):		# MODIF 
				h.write(concat[sp][st][i:i+60] + "\n")
				i+=60
		h.close()
except:
	print 'skipping', sp



