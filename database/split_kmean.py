from config import *
import os

species=getSelectedSpecies("key.txt")
problem = []

sample={}

for sp in species:
	sample[sp]=[]
	f = None
	try:
		f=open(PATH_TO_OUTPUT + sp + '/sample.txt','r')
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
		f=open(PATH_TO_OUTPUT + sp +"/key.txt" ,"r")
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
	print sp
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
	f=open(PATH_TO_OUTPUT + sp +"/distrib.txt" , "r")
	for l in f:
		a=l.strip('\n').split('\t')
		liste.append(a[0])
	f.close()
	vector=[]
	try:
		f=open(PATH_TO_OUTPUT + sp +"/vector.txt" , "r")
	except:
		species.remove(sp)
		continue
	
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
	h=open(PATH_TO_OUTPUT + sp +'/kmeans.txt','w')
	h.write('tot\t' + str(len(low))  + '\t' +  str(round(100*len(low)/float(TOT),1)) + '\t' + str(len(high))  + '\t' +  str(round(100*len(high)/float(TOT),1)) + '\n')
	for st in sample[sp]:
		L = low.count(st)
		H = high.count(st)
		tot = L + H
		#print st,' ',L,' ',H,' ',tot
		try:
			h.write(st + '\t' + str(L) + '\t' + str(round(100*L/float(tot),1)) + '\t' + str(H) + '\t' + str(round(100*H/float(tot),1)) +  '\n')
		except:
			pass
	h.close()















