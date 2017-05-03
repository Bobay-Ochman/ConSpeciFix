
# split species based on k-means method


import os

species=[]
f=open('../results/species.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	sp=a[0]
	species.append(a[0])

f.close()

sample={}
for sp in species:
	sample[sp]=[]
	try:
		f=open('../' + sp + '/subsample.txt','r')
	except IOError:
		f=open('../' + sp + '/sample.txt','r')
	for l in f:
		sample[sp].append(l.strip('\n'))
	f.close()



key={}
for sp in species:
	f=open("../results/distrib/key_" + sp + ".txt" ,"r")
	for l in f:
		a=l.strip('\n').split(' ')
		if float(a[0]) < float(a[1]):
			key[sp] = 'direct'
		else:
			key[sp] = 'reverse'
		print sp,' ', a,' ',key[sp] 
	f.close()




#euk=['drosophila','human']
euk=[]
for sp in species:
	print sp
	liste=[]
	f=open("../results/distrib/distrib_" + sp + ".txt" , "r")
	for l in f:
		a=l.strip('\n').split('\t')
		liste.append(a[0])
	f.close()
	vector=[]
	f=open("../results/distrib/vector_" + sp + ".txt" , "r")
	for l in f:
		a=l.strip('\n').split('\t')
		vector.append(a[0])
	f.close()
	low,high=[],[]
	i=0
	while i < len(vector):
		subset = liste[i]
		if sp in euk:
			strains = subset.split('_')
		else:
			strains = subset.split('-')
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
	h=open('../results/distrib/kmeans_' + sp + '.txt','w')
	h.write('tot\t' + str(len(low))  + '\t' +  str(round(100*len(low)/float(TOT),1)) + '\t' + str(len(high))  + '\t' +  str(round(100*len(high)/float(TOT),1)) + '\n')
	for st in sample[sp]:
		L = low.count(st)
		H = high.count(st)
		tot = L + H
		#print st,' ',L,' ',H,' ',tot
		h.write(st + '\t' + str(L) + '\t' + str(round(100*L/float(tot),1)) + '\t' + str(H) + '\t' + str(round(100*H/float(tot),1)) +  '\n')
	h.close()















