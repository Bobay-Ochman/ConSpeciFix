from config import *
import os


h=open(PATH_TO_MAT + "criterion.txt","w")
kick=[]
tag="no"
f = None
try:
	f=open(PATH_TO_MAT +"kmeans.txt","r")
except Exception as e:
	print str(e)
for l in f:
	a=l.strip('\n').split('\t')
	st = a[0]
	if st != "tot":
		mode1,mode2=float(a[1]),float(a[3])
		tot=mode1+mode2
		ratio = mode2/tot
		if ratio ==0:
			print st
			kick.append(st)
			tag="y"
		h.write(st + "\t" + str(ratio) + "\n")
f.close()
