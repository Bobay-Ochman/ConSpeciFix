from config import *
import time
from datetime import datetime
from datetime import timedelta

species = getSpecies()

orig = -1
startTime = time.time()
sleepTime = 5
prev = -1;

while True:

	totalDone = 0
	totalToDo = 0
	
	for sp in species:
		list = os.listdir(PATH_TO_OUTPUT + sp + '/align/')
		for f in list:
			if f.endswith('.align'):
				totalDone+=1
			else:
				totalToDo +=1

	totalToDo = totalToDo - totalDone
	print totalDone , "done,", totalToDo, "to go"
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