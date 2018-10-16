import random
from config import *
import os
from multiprocessing import Pool


#species = giveMulti(getSpeciesForTest())

#for sp in species:
def sample(sp):
	strains = getGenomes([sp])
	strains = strains[sp]

	dist={}
	#species folder
	try:
		f=open(PATH_TO_OUTPUT + sp + '/RAxML_distances.dist',"r")
		for l in f:
			a=l.strip("\n").split("\t")
			st1,st2 = a[0].strip(" ").split(" ")[0], a[0].strip(" ").split(" ")[1]
			if dist.has_key(st1):
				pass
			else:
				dist[st1] = {}
			if dist.has_key(st2):
				pass
			else:
				dist[st2] = {}
			dist[st1][st2] = float(a[1])
			dist[st2][st1] = float(a[1])
		f.close()
	except:
		return
		
# Remove identical genomes

	exclusion=[]
	try:
		excFd = open('todo/exclusion.txt','r')
		for line in excFd.readlines():
			dat = line.replace("'","").strip('\n')+'.fa'
			if dat in exclusion:
				continue
			else:
				exclusion.append(dat)
	except:
		print "no exclusion.txt in todo folder"

	testStrains = []
	for st in strains:
		testStrains.append(st)
	strains = testStrains
		
	#eprint strains
	for st in exclusion:
		if st in strains:
			print 'removign a strain!'
			strains.remove(st)



#remove strains in exclusion, as well as prep for those greater than 1
	sub=list(dist.keys())
	countOfStrains = {}
	listPairsOfStrains = []
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
				elif float(dist[st1][st2]) > MAX_RAXML_DISTANCE_ALLOWED:
					if st1 in countOfStrains:
						countOfStrains[st1] +=1
					else:
						countOfStrains[st1] = 1
					if st2 in countOfStrains:
						countOfStrains[st2] += 1
					else:
						countOfStrains[st2] = 1
					listPairsOfStrains.append((st1,st2))
		i+=1

#going through and removing the ones that are the most distant
	removedForBeingTooDistant = []
	while len(listPairsOfStrains) > 0:
		maxCount = 0
		strainToRemove = ''
		for strain in countOfStrains:
			if(countOfStrains[strain] > maxCount):
				maxCount = countOfStrains[strain]
				strainToRemove = strain
		if maxCount == 0:
			break
		i = 0
		while i < len(listPairsOfStrains):
			if listPairsOfStrains[i][0] == strainToRemove or listPairsOfStrains[i][1] == strainToRemove:
				listPairsOfStrains.remove(listPairsOfStrains[i])
				i-=1
			i+=1
		sub.remove(strainToRemove)
		removedForBeingTooDistant.append(strainToRemove)
		countOfStrains[strainToRemove] = -1

#Now tackel the ones that are too similar
	removedForBeingTooSimmilar = []
	while len(sub) > 100:
		#generate a list of every pair and their distance from one another
		listOfSimilarities = []
		i = 0
		while i < len(sub):
			st1 = sub[i]
			for st2 in sub:
				if st1!=st2:
					listOfSimilarities.append((st1,st2,dist[st1][st2]))
			i+= 1
		listOfSimilarities = sorted(listOfSimilarities, key = lambda x: x[2])
		maxPair = listOfSimilarities[0]
		sub.remove(maxPair[1])
		removedForBeingTooSimmilar.append(maxPair)

	print len(sub)," strains left"
	cluster= list(sub)


#write out the ones we want to keep
	h=open(PATH_TO_OUTPUT + sp + '/sample.txt',"w")
	for st in sub:
		h.write(st + "\n")
	h.truncate()
	h.close()

#write out the ones we want to toss
	h=open(PATH_TO_OUTPUT + sp + '/removed.txt',"w")
	h.write("Strain in the first column is removed for being too similar to the strain in the second column:\n")
	for st in removedForBeingTooSimmilar:
		h.write(st[1] + "\t" + st[0]+ "\n")
	if len(removedForBeingTooSimmilar) == 0:
		h.write("none removed, all sufficiently distant.\n")

	h.write("\n\nRemoved for being too distant:\n")
	for st in removedForBeingTooDistant:
		h.write(st + "\n")
	if len(removedForBeingTooDistant) == 0:
		h.write("none removed, all sufficiently similar.\n")
	h.truncate()
	h.close()




	#also in the species folder
	h=open(PATH_TO_OUTPUT + sp +'/families_'+sp+'.txt',"w")
	familles=[]
	combin={}
	i=4
	while i <= len(sub):
		toto=0
		#print i
		combin[i] = []
		reservoire=[]
		mifa=i
		j=1
		limit = i**2
		while j <= 50:
			tmp=[]
			for truc in range(i):
				st = random.choice(sub)
				while st in tmp:
					st = random.choice(sub)
				tmp.append(st)
			tmp.sort()
			subset = "&&&".join(tmp)
			if subset not in combin[i]:
				toto+=1
			#	print i,' ',toto
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
	h.truncate()
	h.close()

if __name__ == '__main__':
	species = giveMulti(getSelectedSpecies('RAxML_distances.dist'))	
	p = Pool(MAX_THREADS)
	p.map(sample,species)











