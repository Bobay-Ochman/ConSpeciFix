from config import *
import os



print PATH_TO_OUTPUT
yes = raw_input("Are you sure you would like to remove? (type 'yes' to continue):")
if yes != 'yes':
	exit()

def remove(name):
	try:
		# Leaving this method powerless unless you are actually tring to delete something.
		# Too easy to accedentially call it and start deleting things
		os.remove(PATH_TO_OUTPUT+sp+'/'+name)
		pass
	except:
		print "could not remove "+PATH_TO_OUTPUT+sp+'/'+name

def rename(name):
	try:
		os.rename(PATH_TO_OUTPUT+sp+'/'+name, PATH_TO_OUTPUT+sp+'/zold_'+name)
		pass
	except:
		print "could not rename "+name

species = getAllSpecies()

for sp in species:
	print sp
	removalList = []
	critfd = None
	try:
		critfd = open(PATH_TO_OUTPUT+sp+'/criterion.txt','r')	
	except:
		try:
			critfd = open(PATH_TO_OUTPUT+sp+'/zold_criterion.txt','r')
		except:
			pass

	removalsFlag = False

	if critfd!=None:
		for l in critfd:
			l = l.strip('\n')
			if removalsFlag and l.startswith('GCF'):
				removalList.append(l)
			if "determined to NOT" in l:
				removalsFlag = True

	#The things we need to do to everything:
	for file in os.listdir(PATH_TO_OUTPUT+sp+'/align/'):
	 	remove('align/'+file)

	for file in os.listdir(PATH_TO_OUTPUT+sp+'/'+USEARCH_FOLDER+'/'):
 		fileParts = file.split('.fa-')
 		if fileParts[0]+'.fa' in removalList or fileParts[1] in removalList:
			remove(''+USEARCH_FOLDER+'/'+file)
 			print file
	
	for file in os.listdir(PATH_TO_OUTPUT+sp+'/genes/'):
		if file in removalList:
			remove('genes/'+file)
		
	for file in os.listdir(PATH_TO_OUTPUT+sp+'/genomes/'):
		if file.strip('.fna').strip('.gff')+'.fa' in removalList:
			remove('genomes/'+file)

	remove('concat85.fa')
	remove('concat85.fa.reduced')
	remove('distrib.png')
	remove('distrib.txt')
	remove('families_'+sp+'.txt')
	remove('for_removal.txt')
	remove('gno1.png')
	remove('graph_points.txt')
	remove('graph.txt')
	remove('input_'+sp+'.txt')
	remove('key.txt')
	remove('kmeans.png')
	remove('make_distrib_graph.R')
	remove('make_hm_graph_points.R')
	remove('make_hm_graph.R')
	remove('make_kmean_graph.R')
	remove('orthologs.txt')
	remove('out.input_'+sp+'.txt.I12')
	remove('RAxML_distances.dist')
	remove('RAxML_info.dist')
	remove('RAxML_parsimonyTree.dist')
	remove('removed.txt')
	remove('sample.txt')
	remove('vector.txt')


	rename('combine.png')
	rename('gno2.png')
	rename('gno3.png')
	rename('kmeans.txt')
	rename('rm1.txt')
	rename('criterion.txt')