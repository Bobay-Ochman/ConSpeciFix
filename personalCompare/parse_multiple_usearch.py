from multiprocessing import *
import multiprocessing
import os
from config import *


sentinel = 'no work to be done, go home'

strains = [strainFAFile for strainFAFile in os.listdir(PATH_TO_FOLDER) if str(strainFAFile).endswith('.fa')]
genes,lengthOfGene={},{}

for st in strains:
	genes[st]=0
	f=open(PATH_TO_FOLDER + st ,'r')
	#we go through every line in the file
	for l in f:
		if l[0]=='>':
		#the id is the first thing on the line after the >. also ignore the + and -
			id = l.strip('\n').strip('>').strip(' +').strip(' -')
			#we add one to the counter of how many genes we have
			genes[st]+=1				
		else:
			#we are on the second line of the thing and this is the actual gene
			#length of the gene is the length of the gene
			lengthOfGene[id] = len(l.strip('\n'))
	f.close()

parent={}
count = 0;
#input is the input for the next step. We are putting just the id of the gene, and a 1
g=open(PATH_TO_MAT + 'input.txt',"w")
for st1 in strains:
	count = count + 1
	for st2 in strains:
		if st1 != st2:
			try:
				#open the results of usearch
				#print PATH_TO_OUTPUT + sp + '/BBH/'  + st1 + "-" + st2
				f=open(PATH_TO_MAT+'BBH/'  + st1 + "-" + st2 ,"r") 
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
g.close()

