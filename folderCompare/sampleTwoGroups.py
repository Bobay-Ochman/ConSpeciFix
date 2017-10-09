import random
from config import *
import os
from multiprocessing import Pool
from calcHM_import import *
from scipy import stats


strains = [strainFAFile for strainFAFile in os.listdir(PATH_TO_FOLDER) if str(strainFAFile).endswith('.fa')]

dist={}
try:
	f=open(PATH_TO_MAT + 'RAxML_distances.dist',"r")
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
except Error as e:
	print "Error! " + str(e)
	
testStrains = []
for st in strains:
	testStrains.append(st)
strains = testStrains


exclusion = []
sub=list(dist.keys())
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
			elif float(dist[st1][st2]) <= 0.00005 or float(dist[st1][st2]) > 1:
				if 1==1:
					if st2 in sub:
						sub.remove(st2)
					else:
						print 'PROBLEM'
				i= -1
	i+=1
print len(sub)," strains left"
cluster= list(sub)


h=open(PATH_TO_MAT + 'sample.txt',"w")
for st in strains:
	h.write(st + "\n")
h.truncate()
h.close()



tmp={}
f=open(PATH_TO_MAT + 'concat85.fa',"r")
for l in f:
	if l[0] == '>':
		nb=0
		tag=0
		sp = l.strip('>').strip('\n') 
		tmp[sp] = []
	else:
		try:
			nb += len(l.strip('\n'))
			tmp[sp].append(l.strip('\n'))
		except (KeyError,UnboundLocalError) as e:
			print e
			exit()
f.close()


seq = {}
for sp in strains:
	seq[sp] = ''.join(tmp[sp])






#Find the two strains that are the farthest distance away from eachother

maxDist = -1;
specA = ""
specB = ""
for i in range(len(sub)):
	st1 = sub[i]
	for st2 in sub:
		if st1 != st2:
			if dist[st1][st2] > maxDist:
				maxDist = dist[st1][st2]
				specA = st1
				specB = st2

print maxDist

specAList = [(specA,0)]
specBList = [(specB,0)]

#See how far each strain is away from those two
for strain in sub:
	if strain != specA and strain != specB:
		specAList.append((strain,dist[specA][strain]))
		specBList.append((strain,dist[specB][strain]))


famSize = 15

#take the initial core of the two clades
specAList = sorted(specAList, key=lambda x: x[1])
specBList = sorted(specBList, key=lambda x: x[1])
coreA = [str(i[0]) for i in specAList[:famSize]] #make the core of A clade
coreB = [str(i[0]) for i in specBList[:famSize]] #make the core of B clade
together = coreA[:]	#make a 'together' clade with some of each
together.extend(coreB[:])
together = list(set(together))

for a in specAList:
	print a
print "----"
for a in specBList:
	print a


coreAFam = []
for strain in coreA:
	tempCoreA = coreA[:]
	tempCoreA.remove(strain)
	coreAFam.append("&&&".join(tempCoreA))

coreAHM =[1.4422163588390502, 1.4311878597592884, 1.4893655049151027, 1.4769284959492779, 1.4303250345781466, 1.489013982204467, 1.3358024691358024, 1.4162973065121036, 1.370532703978422, 1.4456427204731257, 1.485252808988764, 1.4676799440950383, 1.4345875043148084, 1.5193743334518308, 1.4169792021820662]
#calcHMLoads(coreAFam,seq,dist)


coreBFam = []
for strain in coreB:
	tempCoreB = coreB[:]
	tempCoreB.remove(strain)
	coreBFam.append("&&&".join(tempCoreB))
coreBHM = [0.11154530343238751, 0.10839541672112578, 0.10814343601585988, 0.10846375797849087, 0.1078576400974591, 0.11223701284499978, 0.11126341577228185, 0.11265547127343944, 0.11404482889622725, 0.11450337118005896, 0.12136815005516734, 0.1215060569039874, 0.12233336283969196, 0.1313005784622668, 0.13115554109609298]
#calcHMLoads(coreBFam,seq,dist)

togetherFam = []
for i in range(famSize):
	togetherDupe = together[:]
	tempTogether = []
	for i in range(famSize-1):
		strain = random.choice(togetherDupe)
		tempTogether.append(strain)
		togetherDupe.remove(strain)
	togetherFam.append("&&&".join(tempTogether))
coreTHM = calcHMLoads(togetherFam,seq,dist)

print len(coreAHM)
print coreAHM
print len(coreBHM)
print coreBHM
print len(coreTHM)
print coreTHM

print "A vs. together:"
print stats.ttest_ind(coreAHM,coreTHM)

print "B vs. together:"
print stats.ttest_ind(coreBHM,coreTHM)

# #also in the species folder
# h=open(PATH_TO_MAT +'families.txt',"w")
# familles=[]
# combin={}
# i=4
# while i <= len(strains):
# 	toto=0
# 	#print i
# 	combin[i] = []
# 	reservoire=[]
# 	mifa=i
# 	j=1
# 	limit = i**2
# 	while j <= 50:
# 		tmp=[]
# 		for truc in range(i):
# 			st = random.choice(strains)
# 			while st in tmp:
# 				st = random.choice(strains)
# 			tmp.append(st)
# 		tmp.sort()
# 		subset = "&&&".join(tmp)
# 		if subset not in combin[i]:
# 			toto+=1
# 		#	print i,' ',toto
# 			combin[i].append(subset)
# 			familles.append(subset)
# 			h.write(str(i) + "\t" + subset + "\n")
# 			j+=1
# 		elif subset not in reservoire:
# 			reservoire.append(subset)
# 			if len(reservoire) == len(combin[i]):
# 				print 'OK'
# 				break
# 	i+=1
# h.truncate()
# h.close()







