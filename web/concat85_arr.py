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
	for st in strains[sp]:
		tmp[sp][st] = []
	for ortho in genes[sp]:
		try:
			print sp, ortho
			f=open( PATH_TO_UPLOAD + 'align/'  + ortho + ".fa.align","r")
			flash={}
			memo=[]
			maxLen = 0;
			for l in f:
				if l[0] == ">":
					id = l.strip("\n").strip(">").split(" ")[0]
					st = parent[id]
					memo.append(st)
					flash[st]=[]
				else:
					flash[st].append(l.strip("\n").upper())
			f.close()
			longueur = ''.join(flash[memo[0]])
			for st in strains[sp]:
				if flash.has_key(st):
					resu = ''.join(flash[st])
				else:
					resu = '-'*len(longueur)
				tmp[sp][st].append(resu)
		except:
			print 'no ortho file'

concat={}
for sp in species:
	concat[sp]={}
	for id in tmp[sp]:
		concat[sp][id] = ''.join(tmp[sp][id])

tmp={}

for sp in species:
	h=open(PATH_TO_UPLOAD + 'concat85.fa',"w")
	for st in strains[sp]:
		h.write(">" + st + "\n")
		i=0
		while i < len(concat[sp][st]):		# MODIF 
			h.write(concat[sp][st][i:i+60] + "\n")
			i+=60
	h.close()
print 'completed! '+str(species[0])

