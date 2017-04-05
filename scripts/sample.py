
import os

species=[]
f=open('../selected_species.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	species.append(a[0])

f.close()

strains={}
for sp in species:
	strains[sp]=[]
	f=open('../results/' + sp + '/new_strains.txt','r')
	for l in f:
		strains[sp].append(l.strip('\n'))
	f.close()



dist={}
for sp in species:
	dist[sp]={}
	f=open('../results/' + sp + '/distances.dist',"r")
	for l in f:
		a=l.strip("\n").split("\t")
		st1,st2 = a[0].strip(" ").split(" ")[0], a[0].strip(" ").split(" ")[1]
		if dist[sp].has_key(st1):
			pass
		else:
			dist[sp][st1] = {}
		if dist[sp].has_key(st2):
			pass
		else:
			dist[sp][st2] = {}
		dist[sp][st1][st2] = float(a[1])
		dist[sp][st2][st1] = float(a[1])
	f.close()


# Remove identical genomes

exclusion=['NC_002513']

for sp in species:
	for st in exclusion:
		if st in strains[sp]:
			strains[sp].remove(st)


cluster={}
for sp in species:
	sub=list(dist[sp].keys())
	print sp,' ',len(sub)
	i=0
	while i in range(len(sub)):
		st1 = sub[i]
		for st2 in sub:
			if st1 != st2:
				#if float(dist[st1][st2]) == 0 or float(dist[st1][st2]) > 1:
				if st1 in exclusion or st2 in exclusion:
					if st1 in exclusion and st1 in sub:
						sub.remove(st1)
						i= -1
					elif  st2 in exclusion and st2 in sub:
						sub.remove(st2)
						i=-1
				elif float(dist[sp][st1][st2]) <= 0.00005 or float(dist[sp][st1][st2]) > 1:
					if 1==1:
						if st2 in sub:
							sub.remove(st2)
						else:
							print 'PROBLEM'
					i= -1
		i+=1
	print len(sub)," strains left"
	cluster[sp]= list(sub)



for sp in species:
	h=open('../results/' + sp + '/sample.txt',"w")
	for st in strains[sp]:
		h.write(st + "\n")
	h.close()


import random

for sp in species:
	h=open('../results/families_' + sp + '.txt',"w")
	familles=[]
	combin={}
	i=4
	while i <= len(strains[sp]):
		toto=0
		#print i
		combin[i] = []
		reservoire=[]
		mifa=i
		j=1
		limit = i**2
		while j <= 100:
			tmp=[]
			for truc in range(i):
				st = random.choice(strains[sp])
				while st in tmp:
					st = random.choice(strains[sp])
				tmp.append(st)
			tmp.sort()
			subset = "-".join(tmp)
			if subset not in combin[i]:
				toto+=1
				print i,' ',toto
				combin[i].append(subset)
				familles.append(subset)
				h.write(str(i) + "\t" + subset + "\n")
				j+=1
			elif subset not in reservoire:
				reservoire.append(subset)
				if len(reservoire) == len(combin[i]):
					print 'OK'
					break
		i+=1
	h.close()
















