import os
from config import *
import sys
import random

totalArgs= []
for dbSp in os.listdir(PATH_TO_DATABASE):
	for cpSp in os.listdir(PATH_TO_DATABASE):
		if dbSp==cpSp:
			continue
		tenForU = open(PATH_TO_DATABASE+cpSp+'/tenForUsearch.txt')
		possibleStrains = []
		for l in tenForU:
			possibleStrains.append(l.strip())
		doingComp = []
		for i in range(3):
			strainToDo = random.choice(possibleStrains)
			possibleStrains.remove(strainToDo)
			doingComp.append(strainToDo)
			args = '\t'.join([dbSp,cpSp,strainToDo,str(i+1)])
			totalArgs.append(args)
fd = open('todo/runner.txt','w')
fd.write('\n'.join(totalArgs))
fd.close()
