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
		path = work[0]
		sp = work[1]
		prot1 = work[2]
		prot2 = work[3]
#		command = ' usearch61 -usearch_global ' + path + sp + '/genes/' + prot1 + ' -db  ' + path + sp + '/genes/'  + prot2 + ' -id 0.7 -strand plus -blast6out ' + path +  sp + '/BBH/' + prot1 + '-' + prot2
	
		#run usearch
		args = []
		args.append(USEARCH_PATH)
		args.append('-usearch_global')
		args.append(path + sp + '/genes/' + prot1)
		args.append('-db')
		args.append(PATH_TO_UPLOAD + prot2)
		args.append('-id')
		args.append('0.7')
		args.append('--threads')
		args.append('2')
		args.append('-strand')
		args.append('plus')
		args.append('-blast6out')
		args.append(PATH_TO_UPLOAD + 'BBH/' + prot1 + '-' + prot2)
		com = ""
		for arg in args:
			com += " "+arg
		print "command to be used:",com
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
			remQ.put(sp+'-'+prot2)
			remQ.put(sp+'-'+prot1)
			continue
		#check the result
		# res = open(path +  sp + '/BBH/' + prot1 + '-' + prot2)
		# compResults = []
		# for line in res:
		# 	compResults.append(float(line.split('\t')[2]))
		# med = median(compResults)
		# if med >99:
		# 	remQ.put(sp+'-'+prot2)
		#do a search to find things that are too similar

#		if (dupID):
#			remQ.put('187')


if __name__ == '__main__':
 	#info('main line')
	jobQ = Queue(maxsize=MAX_THREADS)#so we only ever at most have one thing waiting for a job -> ensures minimum number of similar things get processed
	remQ = Queue()
	killList = []
	processes = []
	
	largeSpecList = []
	
	for i in range(MAX_THREADS):
		p = Process(target=work, args=(jobQ,remQ))
		p.start()
		processes.append(p)

	f = open(PATH_TO_UPLOAD + 'todo/usearch.txt','r')
	lines = f.readlines()
	print len(lines)
	for l in lines:
		##see if any of our children functions have produced a thing we need to not init
		try:
			newKill = remQ.get_nowait()
			newKillSp = newKill.split('-')[0]
			if newKill not in killList and newKillSp in largeSpecList:
				killList.append(newKill)
			totalSequencesRemoved+=1
		except:
			pass
		job = l.strip('\n').split('\t')
		seqA = job[1] +'-'+ job[2]
		seqB = job[1] +'-' +job[3]
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
