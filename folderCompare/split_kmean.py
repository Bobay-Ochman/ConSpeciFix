from config import *
import os

sample=[]
f = None
try:
	f=open(PATH_TO_MAT + 'sample.txt','r')
except IOError as e:
	print 'error', str(e)
for l in f:
	sample.append(l.strip('\n'))
f.close()


key={}

f = None
try:
	f=open(PATH_TO_MAT +"key.txt" ,"r")
except IOError as e:
	print 'error', str(e)
lines = f.readlines()
if(len(lines) == 0):
	print 'error, no lines in file',str(f)
for l in lines:
	a=l.strip('\n').split(' ')
	if float(a[0]) < float(a[1]):
		key = 'direct'
	else:
		key = 'reverse'
	print  a,key 
f.close()

euk=[]
print "*********"
liste=[]
f=open(PATH_TO_MAT +"distrib.txt" , "r")
for l in f:
	a=l.strip('\n').split('\t')
	liste.append(a[0])
f.close()
vector=[]
try:
	f=open(PATH_TO_MAT +"vector.txt" , "r")
except Error as e:
	print 'error', str(e)

	
for l in f:
	a=l.strip('\n').split('\t')
	vector.append(a[0])
f.close()
low,high=[],[]
i=0
while i < len(vector):
	subset = liste[i]
	strains = subset.split('&&&') # split on &&&
	tag = vector[i]
	if key=="direct":
		if tag == "1":
			low.extend(strains)
		elif tag == "2":
			high.extend(strains)
	else:
		if tag == "2":
			low.extend(strains)
		elif tag == "1":
			high.extend(strains)
	i+=1
TOT = len(low) + len(high)
h=open(PATH_TO_MAT +'kmeans.txt','w')
h.write('tot\t' + str(len(low))  + '\t' +  str(round(100*len(low)/float(TOT),1)) + '\t' + str(len(high))  + '\t' +  str(round(100*len(high)/float(TOT),1)) + '\n')
for st in sample:
	L = low.count(st)
	H = high.count(st)
	tot = L + H
	try:
		h.write(st + '\t' + str(L) + '\t' + str(round(100*L/float(tot),1)) + '\t' + str(H) + '\t' + str(round(100*H/float(tot),1)) +  '\n')
	except:
		pass
h.close()







