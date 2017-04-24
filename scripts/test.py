from config import *
import os

fd = open('todo/calcHM.txt','r')
spec = []
for l in fd.readlines():
	sp = l.split('\t')[0]
	if sp in spec:
		pass
	else:
		spec.append(sp)
print len(spec)
print spec