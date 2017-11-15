from multiprocessing import Pool
import multiprocessing
import os
from config import *

#species=getSpeciesOfSize(500)


species = getSingleSpecies()
sp = species[0]
strains=getStrains(species)
specialStrain = getCompStrain()+'.fa'

# build dictionary of orthologs already identified as core
orthofd = open(PATH_TO_OUTPUT+sp+'/orthologs.txt')
geneOrthoLabels = {}
orthoNumberToGenes = {}
for line in orthofd:
	l = line.strip('\n').split('\t')
	orthoNumb = l[0]
	l.pop(0)#remove the ortho number from list of genes
	orthoNumberToGenes[orthoNumb] = l[:] #map ortho# to the database genes it matches with
	for gene in l:
		geneOrthoLabels[gene] = orthoNumb

#build the new dictionary of user genes and all database they map to
geneMap = {}
identityScore = []
for st1 in strains[sp]:
	st2 = specialStrain
	try:
		#open the results of usearch
		identityScoreForFile = []
		f=open(PATH_TO_UPLOAD + 'BBH/'  + st1 + "-" + st2 ,"r") 
		for l in f:
			a = l.strip("\n").split("\t")
			#get the ids of the two genes they are comparing
			id1 = a[0].strip(' -').strip(' +')
			id2 = a[1].strip(' -').strip(' +')
			identityScoreForFile.append(float(a[2]))
			userGene = ''
			databaseGene = ''
			if 'gene' in id1:
				userGene = id1
				databaseGene = id2
			else:
				userGene = id2
				databaseGene = id1
			if userGene in geneMap:
				geneMap[userGene].append(databaseGene)
			else:
				geneMap[userGene] = [databaseGene]
		f.close()
		identityScore.append(median(identityScoreForFile))
	except IOError:
		print "!!!!!! ",st1, st2
		pass

#maps an ortho number to a user gene
assignedOrthos = {}

#goes through each user gene and assigns it to a particular ortholog family
for userGene in geneMap:
	#maps ortho numbers to a count of # times user gene matches genes in that ortho
	possibleOrthos = {} #(all the ones we might be)
	for databaseGene in geneMap[userGene]:
		if databaseGene in geneOrthoLabels: #only use the core genes
			ortho  = geneOrthoLabels[databaseGene]
			if ortho in possibleOrthos:
				possibleOrthos[ortho] = possibleOrthos[ortho] + 1
			else:
				possibleOrthos[ortho] = 1
	bestCandidateOrtho = '' #(The one the we think we are the most)
	for ortho in possibleOrthos:
		if possibleOrthos[ortho] / (len(geneMap[userGene]) + 0.0) >= .85:
			bestCandidateOrtho = ortho
	if bestCandidateOrtho != '':
		assignedOrthos[bestCandidateOrtho] = userGene

# add user gene to the list of database genes
for orthoNumb in assignedOrthos:
	orthoNumberToGenes[orthoNumb].append(assignedOrthos[orthoNumb])



#write orthologs.txt
h=open(PATH_TO_UPLOAD + 'orthologs.txt',"w")
for orthoNumb in orthoNumberToGenes:
	stringToWrite = '\t'.join(orthoNumberToGenes[orthoNumb])
	if 'gene' in stringToWrite:
		h.write(orthoNumb + '\t' + stringToWrite + '\n')
h.close()



critInfoFD = open(PATH_TO_UPLOAD+'crit_stats.txt','w')
critInfoFD.write('Average Identity Score relative to other members of species: '+str(mean(identityScore))+'%\n')
critInfoFD.close()



