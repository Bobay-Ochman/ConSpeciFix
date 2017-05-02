from multiprocessing import *
import multiprocessing
import os
from config import *



species = getSingleSpecies()
sp = species[0]

strains= getGenomes(species)
specialStrain = getCompStrain()

genes,lengthOfGene={},{}

genes[sp]={}
for st in strains[sp]:
	genes[sp][st]=0
	f=open(PATH_TO_OUTPUT + sp + '/genes/' + st ,'r')

	#we go through every line in the file
	for l in f:
		if l[0]=='>':
			#the id is the first thing on the line after the >. also ignore the + and -
			id = l.strip('\n').strip('>').strip(' +').strip(' -')
			#we add one to the counter of how many genes we have
			genes[sp][st]+=1
		else:
			#we are on the second line of the thing and this is the actual gene
			#length of the gene is the length of the gene
			lengthOfGene[id] = len(l.strip('\n'))
	f.close()

#Do it again for the special strain
genes[sp][specialStrain]=0
f=open(uploadPath() '/genes/' + st ,'r')
for l in f:
	if l[0]=='>':
		id = l.strip('\n').strip('>').strip(' +').strip(' -')
		genes[sp][st]+=1
	else:
		lengthOfGene[id] = len(l.strip('\n'))
f.close()

parent={}
count = 0;

#start off buy grabbing all the origional output
origFile=open(PATH_TO_OUTPUT + sp + '/input.txt',"r")
g=open(uploadPath()+'/input.txt','w')
for l in origFile:
	g.write(l)

#input is the input for the next step. We are putting just the id of the two genes that are equivilant, and a 1
for st1 in strains[sp]:

	count = count + 1
	print sp,' ',count,'/',len(strains[sp]),' strains'
	
	st2 = specialStrain
	try:
		#open the results of usearch
		f=open(uploadPath() + '/BBH/'  + st1 + "-" + st2 ,"r") 
		geneIDs = []
		for l in f:
			a= l.strip("\n").split("\t")
			#get the ids of the two genes they are comparing
			id1 = a[0].strip(' -').strip(' +')
			id2 = a[1].strip(' -').strip(' +')
			#also get the length of the usearch rn
			len1,len2= lengthOfGene[id1] ,lengthOfGene[id2] 
	
			ratio = float(len1) / len2
			parent[id1],parent[id2]=st1,st2
			#if their lengths are similar, we pass them
			#code should probably compare len vs the length of similar dna -> (the 4th number in the USearch output)
			
			if id1 in geneIDs or id2 in geneIDs:
				pass
			elif ratio >= 0.8 and ratio <= 1.2:
				g.write(id1 + "\t" + id2 + "\t1\n" )
				geneIDs.append(id1)
				geneIDs.append(id2)
		f.close()
	except IOError:
		#print "!!!!!! ",st1,".prot-",st2,".prot"
		#h.write(st1 + "\t" + st2 + "\n")
		pass
g.truncate()
g.close()

