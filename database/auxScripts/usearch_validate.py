from multiprocessing import *
import multiprocessing
import subprocess
import math
import time
from config import *

sentinel = ['no work to be done, go home'] 
maxThreads = 36
totalWorkPut = 0
totalSequencesRemoved = 0

def work(jobQ,remQ):
	#info('function f')
	while True:
		work = jobQ.get()
		if work == sentinel:
			print 'done'
			return
		path = work[0]
		sp = work[1]
		v1 = work[2]
		v2 = work[3]
		name = v1 + '-' + v2
		h = None
		try:
			h = open(PATH_TO_OUTPUT + sp + '/'+USEARCH_FOLDER+'/' + name,'r')
		except:
			continue
		lines = h.readlines()
		for l in lines:
			lenLine = len(l.split('\t'))
			if lenLine != 12:
				#print lenLine
				print sp + '/'+USEARCH_FOLDER+'/' + name
				remQ.put([PATH_TO_OUTPUT,sp,v1,v2])
		h.close()		

def printInvalid(remQ):
	incomFile = open('todo/usearch_re_do.txt','w')
	while True:
		work = remQ.get()
		if work == sentinel:
			print 'done'
			return
		print 'working!!!!! ' + str(work)
		sp = work[1]
		v1 = work[2]
		v2 = work[3]
		incomFile.write(PATH_TO_OUTPUT +'\t'+ sp+'\t'+v1+'\t'+v2+'\n')
		incomFile.flush()
	
if __name__ == '__main__':
 	#info('main line')
	jobQ = Queue(maxsize=maxThreads)#so we only ever at most have one thing waiting for a job -> ensures minimum number of similar things get processed
	remQ = Queue()
	killList = []
	processes = []
	
	largeSpecList = []
	
	f = open('todo/LargeSpec.txt','r')
	for line in f:
		largeSpecList.append(line.strip('\n'))
	f.close()
	
	p = Process(target=printInvalid, args=([remQ]))
	p.start()
	
	for i in range(maxThreads):
		p = Process(target=work, args=(jobQ,remQ))
		p.start()
		processes.append(p)


	genomes = getGenomes(getSpecies())
	
	for sp in genomes:
		if sp not in largeSpecList:
			print 'doing '+sp +' ' +str(len(genomes[sp]))
			for v1 in genomes[sp]:	
				for v2 in genomes[sp]:
					if v1!=v2:				
						jobQ.put([PATH_TO_OUTPUT,sp,v1,v2])
			
	for i in range(maxThreads):
		jobQ.put(sentinel)
	print 'done producing'

	for p in processes:
		p.join()
	
	remQ.put(sentinel)
	print 'all work is done!'


	