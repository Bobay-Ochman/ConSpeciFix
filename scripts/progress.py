from config import *
import time
import datetime


species = getSpecies()

orig = -1
startTime = time.time()
sleepTime = 5
prev = -1;

while True:

	totalDone = 0
	totalToDo = 0

	for sp in species:
		filesDone = os.listdir(PATH_TO_OUTPUT + sp + '/BBH/')
		#filesToDo = os.listdir(PATH_TO_OUTPUT + sp + '/genomes/')
		totalDone += len(filesDone)
		#totalToDo += len(filesToDo)/2

	print totalDone #,' / ',totalToDo	
	if(orig == -1):
		orig = totalDone
		prev = orig
	else:
		diff = totalDone - orig
		now = time.time()
		print diff / (now - startTime)
		if prev == totalDone:
			exit()
		prev = totalDone
	print datetime.datetime.now().time()
	time.sleep(sleepTime)