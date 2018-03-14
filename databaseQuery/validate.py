import os
from config import *
from multiprocessing import Pool




for trial in os.listdir(PATH_TO_QUERY_SPEC):
	if trial == '.DS_Store':
		continue
	validate(trial)

def validate(timestamp):
	thingsToRemove = []
	if not os.path.isfile(PATH_TO_QUERY_SPEC+trial+'/criterion.txt'):
		#check folders for empty files:
		for folderName in ['align','BBH']:
			for fileName in os.listdir(PATH_TO_QUERY_SPEC+timestamp+'/'+folderName):
				if os.stat(PATH_TO_QUERY_SPEC+timestamp+'/'+folderName+'/'+fileName).st_size == 0:
					thingsToRemove.append(folderName+'/'+fileName)
		thingsToRemove.append('boxPlot.pdf')
		thingsToRemove.append('concat85.fa')
		thingsToRemove.append('criterion.txt')
		thingsToRemove.append('crit_stats.txt') 
		thingsToRemove.append('Distrib_*') 
		thingsToRemove.append('distrib_*') 
		thingsToRemove.append('draw.R') 
		thingsToRemove.append('families_*') 
		thingsToRemove.append('graph.R') 
		thingsToRemove.append('graph.txt') 
		thingsToRemove.append('key_*') 
		thingsToRemove.append('kmeans_*') 
		thingsToRemove.append('orthologs.txt') 
		thingsToRemove.append('out') 
		thingsToRemove.append('RAxML*') 
		thingsToRemove.append('results') 
		thingsToRemove.append('rm1.txt') 
		thingsToRemove.append('sample.txt') 
		thingsToRemove.append('testGraph.pdf') 
		thingsToRemove.append('todo') 
		thingsToRemove.append('vector_*')

		print ('rm -r '+ (' '+PATH_TO_QUERY_SPEC+timestamp+'/').join(thingsToRemove))