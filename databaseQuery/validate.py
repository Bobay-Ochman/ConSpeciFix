import os
from config import *
from multiprocessing import Pool




def validate(timestamp):
	thingsToRemove = []
	pathCrit = PATH_TO_QUERY_SPEC+timestamp+'/criterion.txt'
	pathFold = PATH_TO_QUERY_SPEC+timestamp+'/BBH'
	#print os.path.isfile(pathCrit)
	#print os.path.isdir(pathFold)
	pathToTrial = PATH_TO_QUERY_SPEC+timestamp+'/'
	#print pathToTrial
	if (not os.path.isfile(pathCrit)) and os.path.isdir(pathFold):
		#check folders for empty files:
	
		for folderName in ['align','BBH']:
			try:
				for fileName in os.listdir(pathToTrial+folderName):
					if os.stat(pathToTrial+folderName+'/'+fileName).st_size == 0:
						thingsToRemove.append(folderName+'/'+fileName)
			except Exception as e:
				print e
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
		thingsToRemove.append('align') 
		thingsToRemove.append('vector_*')

		# thingsToRemove.append('BBH')
		#print "hi"
		os.system('rm -r '+pathToTrial+ (' '+pathToTrial).join(thingsToRemove))



trials = os.listdir(PATH_TO_QUERY_SPEC)
trials.remove('.DS_Store')
if __name__ == '__main__':
    p = Pool(72)
    print(len(trials))
    p.map(validate, trials)






