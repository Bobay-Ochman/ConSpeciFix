from config import *
import os

species = getAllSpecies()

for sp in species:
	genePairs = {} #will map set of (a,b) to [dist1, dist2, ... dist100]
	for i in range(100):
		try:
			print sp,i
			raxmlFD = open(PATH_TO_OUTPUT+sp+'/geneSubsets/geneSubsetNo'+str(i)+'/RAxML_distances.dist')
			for l in raxmlFD:
				parts = l.strip('\n').split('\t')
				dist = float(parts[1])
				strainA = parts[0].split(' ')[0]
				strainB = parts[0].split(' ')[1]
				pairGenes = parts[0]
				if pairGenes in genePairs:
					genePairs[pairGenes].append(dist)
				else:
					genePairs[pairGenes] = [dist]
				if strainB+' '+strainA in genePairs:
					print 'PROBLEM!'
			raxmlFD.close()
		except:
			print sp,i,'ERROR!!!!'
	try:
		oldRAXML = open(PATH_TO_OUTPUT+sp+'/old_RAxML_distances.dist','r')
		oldRAXML.close()
	except:
		os.rename(PATH_TO_OUTPUT+sp+'/RAxML_distances.dist',PATH_TO_OUTPUT+sp+'/old_RAxML_distances.dist')

	fd = open(PATH_TO_OUTPUT+sp+'/RAxML_distances.dist','w')
	for key in genePairs:
		val = median(genePairs[key])
		fd.write(key+'\t'+ ("%.7f" % val) +'\n')
	fd.close()

