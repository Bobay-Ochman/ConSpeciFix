from multiprocessing import *
import multiprocessing
import subprocess
import math
import time
from config import *

sentinel = ['no work to be done, go home'] 
totalWorkPut = 0
totalSequencesRemoved = 0

def work(jobQ,remQ):
	#info('function f')
	while True:
		work = jobQ.get()
		if work == sentinel:
			print 'done'
			return
		path = PATH_TO_FOLDER
		prot1 = work[0]
		prot2 = work[1]
#		command = ' usearch61 -usearch_global ' + path + sp + '/genes/' + prot1 + ' -db  ' + path + sp + '/genes/'  + prot2 + ' -id 0.7 -strand plus -blast6out ' + path +  sp + '/BBH/' + prot1 + '-' + prot2
	
		#run usearch
		args = []
		args.append(USEARCH_PATH)
		args.append('-usearch_global')
		args.append(path + prot1)
		args.append('-db')
		args.append(path + prot2)
		args.append('-id')
		args.append('0.7')
		args.append('-strand')
		args.append('plus')
		args.append('-blast6out')
		args.append(PATH_TO_MAT + 'BBH/' + prot1 + '-' + prot2)
		popen = subprocess.Popen(args, stderr=subprocess.PIPE, universal_newlines=True)
		for stdout_line in iter(popen.stderr.readline, ""):
			print 'out: '+ stdout_line.strip('\n') 
			if '---Fatal error---' in stdout_line:
				print 'fatal error was there we can do something to kill it now!!!!'
				popen.kill()
				continue
		popen.stderr.close()
		return_code = popen.wait()
		if return_code:
			print 'return code: '+ str(return_code)
			continue
		#check the result
		res = open(PATH_TO_MAT + 'BBH/' + prot1 + '-' + prot2)
		compResults = []
		for line in res:
			compResults.append(float(line.split('\t')[2]))
		med = median(compResults)

if __name__ == '__main__':
 	#info('main line')
	jobQ = Queue(maxsize=MAX_THREADS)#so we only ever at most have one thing waiting for a job -> ensures minimum number of similar things get processed
	remQ = Queue()
	killList = []
	processes = []
	
	for i in range(MAX_THREADS):
		p = Process(target=work, args=(jobQ,remQ))
		p.start()
		processes.append(p)

	f = open(PATH_TO_TODO + 'usearch.txt','r')
	lines = f.readlines()
	for l in lines:
		##see if any of our children functions have produced a thing we need to not init
		try:
			newKill = remQ.get_nowait()
			newKillSp = newKill.split('-')[0]
			if newKill not in killList:
				killList.append(newKill)
			totalSequencesRemoved+=1
		except:
			pass
		job = l.strip('\n').split('\t')
		seqA = job[0]
		seqB = job[1]
		#now we see if the job is not in the 'don't do' list
		if seqA not in killList and seqB not in killList:
			jobQ.put(job)
			totalWorkPut+=1
			
	for i in range(MAX_THREADS):
		jobQ.put(sentinel)
	print 'done producing'

	for p in processes:
		p.join()
	print 'all work is done!'
	print 'total comps: ' + str(totalWorkPut)
	print 'total removs:' + str(totalSequencesRemoved)
	print 'size of remove list: ' + str(len(killList))

