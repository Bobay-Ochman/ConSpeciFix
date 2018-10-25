import os
from config import *
import sys
import random

totalArgs= []
for dbSp in os.lisdir(PATH_TO_DATABASE):
	for cpSp in os.lisdir(PATH_TO_DATABASE):
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
			args = '\t'.joint([dbSp,cpSp,strainToDo])
			totalArgs.append(args)
print totalArgs
