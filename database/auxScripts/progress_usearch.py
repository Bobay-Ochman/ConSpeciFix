from config import *
import time
from datetime import datetime
from datetime import timedelta

species = getSpecies()

orig = -1
startTime = time.time()
sleepTime = 10
prev = -1;

totalToDo = len(open('todo/usearch.txt','r').readlines())


while True:

	totalDone = 0

	for sp in species:
		list = os.listdir(PATH_TO_OUTPUT + sp + '/'+USEARCH_FOLDER+'/')
		for f in list:
			if f.endswith('fa'):
				totalDone+=1

	print totalDone
#	print totalDone ,' / ',totalToDo,'('+str(round(totalDone/(totalToDo * 1.0)*100,3))+'%)'
	if(orig == -1):
		orig = totalDone
		prev = orig
	else:
		diff = totalDone - orig
		now = time.time()
		rate = diff / (now - startTime)
		if rate == 0:
			print 'rate is zero'
		else:
			print '\t',round(rate,3)
			timeLeft = totalToDo/rate
			prev = totalDone
			print '\tcurrent : '+str(datetime.now().time())
			print '\ttarget  : '+str((datetime.now()+timedelta(seconds=timeLeft)).time()	)
	time.sleep(sleepTime)