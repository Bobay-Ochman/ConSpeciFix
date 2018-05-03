from config import *
import os

species=getSingleSpecies()

problem = []
sample={}

for sp in species:
	sample[sp]=[]
	f = None
	try:
		f=open(PATH_TO_UPLOAD + 'sample.txt','r')
	except IOError:
		problem.append(sp)
		continue
	for l in f:
		sample[sp].append(l.strip('\n'))
	f.close()



key={}

for sp in species:
	f = None
	try:
		f=open(PATH_TO_UPLOAD + "key_" + sp + ".txt" ,"r")
	except IOError:
		problem.append(sp)
		continue
	lines = f.readlines()
	if(len(lines) == 0):
		problem.append(sp)
	for l in lines:
		a=l.strip('\n').split(' ')
		if float(a[0]) < float(a[1]):
			key[sp] = 'direct'
		else:
			key[sp] = 'reverse'
		print sp,' ', a,' ',key[sp] 
	f.close()

for sp in problem:
	try:
		species.remove(sp)
	except:
		pass

#euk=['drosophila','human']
euk=[]
print "*********"
#print species
for sp in species:
	print sp
	liste=[]
	f=open(PATH_TO_UPLOAD +"distrib_" + sp + ".txt" , "r")
	for l in f:
		a=l.strip('\n').split('\t')
		liste.append(a[0])
	f.close()
	vector=[]
	try:
		f=open(PATH_TO_UPLOAD +"vector_" + sp + ".txt" , "r")
	except:
		species.remove(sp)
		continue
	
	for l in f:
		a=l.strip('\n').split('\t')
		vector.append(a[0])
	f.close()
	low,high=[],[]
	i=0
	print vector
	while i < len(vector):
		subset = liste[i]
		strains = subset.split('&&&')
		tag = vector[i]
		if key[sp]=="direct":
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
	h=open(PATH_TO_UPLOAD + 'kmeans.txt','w')
	h.write('tot\t' + str(len(low))  + '\t' +  str(round(100*len(low)/float(TOT),1)) + '\t' + str(len(high))  + '\t' +  str(round(100*len(high)/float(TOT),1)) + '\n')
	for st in sample[sp]:
		L = low.count(st)
		H = high.count(st)
		tot = L + H
		#print st,' ',L,' ',H,' ',tot
		h.write(st + '\t' + str(L) + '\t' + str(round(100*L/float(tot),1)) + '\t' + str(H) + '\t' + str(round(100*H/float(tot),1)) +  '\n')
	h.close()















