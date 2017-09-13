import os
from config import *
from multiprocessing import Pool
import multiprocessing
import random
	
#make the file for us
f=open(PATH_TO_UPLOAD + 'todo/exclusion.txt','w')
f.close()

SP = getSingleSpecies()[0]
	# Load distances
strains=[]
f=open(PATH_TO_UPLOAD + 'sample.txt','r')
for l in f:
	a=l.strip("\n").split("\t")
	strains.append(a[0])
f.close()


dist={}
f=open(PATH_TO_UPLOAD + 'RAxML_distances.dist',"r")
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


tmp={}
f=open(PATH_TO_UPLOAD + 'concat85.fa',"r")
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
			quit()
f.close()


seq = {}
for sp in strains:
	seq[sp] = ''.join(tmp[sp])
#strains.remove('Dsim')

memo_subset={}
tmp = os.listdir(PATH_TO_UPLOAD)
for file in tmp:
	if file.startswith("rm"):
		f=open( PATH_TO_UPLOAD + file,"r")
		for l in f:
			a=l.strip("\n").split("\t")
			if len(a) == 5:									
				memo_subset[a[0]] = a[1:]
		f.close()

f_subset=open(PATH_TO_UPLOAD + 'rm1.txt',"w")
for subset in memo_subset:
	f_subset.write(subset + "\t" + '\t'.join(memo_subset[subset])  + "\n")

f_subset.close()



tmp=[]
f=open(PATH_TO_UPLOAD + 'families_'+SP+'.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	if memo_subset.has_key(a[1]):
		pass
	else:
		tmp.append(a[1])	
	
subsets=[]
while len(tmp) > 0:
	truc = random.choice(tmp)
	subsets.append(truc)
	tmp.remove(truc)

	
alpha=['A','C','G','T']

LONGUEUR=len(seq[sp])
if LONGUEUR > 100000:
	LONGUEUR = 100000

for truc in subsets:
	strains = truc.split('&&&')
	bip=[]
	singleton,more=0,0
	i = 0
	r,m=0,0
	while i < LONGUEUR:
		tmp=[]
		memo=[]
		for sp in strains:
			# lookingAtMe = False
			# try:
			# 	testing = seq[sp]
			# 	lookingAtMe = True
			# 	testing2 = testing[i]
			# except KeyError as e:
			# 	print 'we got some real problems now!!!! ',lookingAtMe,e
			# 	errorFD = open(PATH_TO_UPLOAD + 'todo/exclusion.txt','a')
			# 	errorFD.write(str(e)+'\n')
			# 	errorFD.close()
			# 	return
			N = seq[sp][i]
			if N in alpha:
				tmp.append(N)
				memo.append(sp)
		tot = len(tmp)
		all = list(set(tmp))
		unique,number=[],[]
		for N in all:
			number.append(tmp.count(N))
			if tmp.count(N) >1:
				unique.append(N)
		if len(number) > 1:
			while 1 in number:
				number.remove(1)
				singleton+=1
				m+=1
			if len(number) == 2:																		##### 2 #####
				more += 1
				N1,N2 = unique[0],unique[1]
				nt1,nt2 = tmp.count(N1),tmp.count(N2)
				if nt1 <= nt2:
					minor = N1
				elif nt1 > nt2:
					minor = N2
				sac,other=[],[]
				j=0
				while j < len(tmp):
					N,sp = tmp[j],memo[j]
					if N == minor:
						sac.append(sp)
					else:
						other.append(sp)
					j+=1
				INTRA,INTER=[],[]
				for st1 in sac:
					for st2 in sac:
						if st1 != st2:
							INTRA.append(dist[st1][st2])
					for st2 in other:
						INTER.append(dist[st1][st2])
				if max(INTRA) > min(INTER):
					r+=1
					toto='r'
				else:
					toto='m'
					m+=1
				#print i,' ',tot,' ',unique,' ',number,' ',minor,' ',min(INTRA),' ',min(INTER),' ',toto
				bip.append(toto)
			elif len(number) == 3:																		##### 3 #####
				N1,N2,N3 = unique[0],unique[1],unique[2]
				check,check2=0,0
				done=[]
				k=0
				while k < 3:
					N,nt = unique[k],number[k]
					if nt == min(number):
						if check == 0:
							minor1 =  N
							done.append(N)
							check=1
					elif nt == max(number):
						if check2==0:
							major = N
							done.append(N)
							check2=1
					k+=1
				for N in unique:
					if N not in done:
						minor2 = N
				sac1,sac2,other=[],[],[]
				j=0
				while j < len(tmp):
					N,sp = tmp[j],memo[j]
					if N == minor1:
						sac1.append(sp)
					elif N == minor2:
						sac2.append(sp)
					else:
						other.append(sp)
					j+=1
				INTRA,INTER=[],[]
				for st1 in sac1:
					for st2 in sac1:
						if st1 != st2:
							INTRA.append(dist[st1][st2])
					for st2 in other:
						INTER.append(dist[st1][st2])
				if max(INTRA) > min(INTER):
					r+=1
					toto='r'
				else:
					toto='m'
					m+=1	
				#print i,' ',tot,' ',unique,' ',number,' ',minor1,' ',min(INTRA),' ',min(INTER),' ',toto
				bip.append(toto)
				INTRA,INTER=[],[]
				for st1 in sac2:
					for st2 in sac2:
						if st1 != st2:
							INTRA.append(dist[st1][st2])
					for st2 in other:
						INTER.append(dist[st1][st2])
				if max(INTRA) > min(INTER):
					r+=1
					toto='r'
				else:
					toto='m'
					m+=1
				#print i,' ',tot,' ',unique,' ',number,' ',minor2,' ',min(INTRA),' ',min(INTER),' ',toto
				bip.append(toto)
			elif len(number) == 4:																		##### 4 #####
				N1,N2,N3,N4 = unique[0],unique[1],unique[2],unique[3]
				done=[]
				check,check2=0,0
				k=0
				while k < 4:
					N,nt = unique[k],number[k]
					if nt == min(number):
						if check==0:
							minor1 =  N
							done.append(N)
							check=1
					elif nt == max(number):
						if check2==0:
							major = N
							done.append(N)
							check2=1
					k+=1
				left=[]
				for N in unique:
					if N not in done:
						left.append(N)
				souvenir=[]
				k=0
				while k < 4:
					N,nt = unique[k],number[k]
					if N in left:
						souvenir.append(nt)
					k+=1
				if souvenir[0] <= souvenir[1]:
					minor2,minor3 = left[0],left[1]
				else:
					minor2,minor3 = left[1],left[0]
				sac1,sac2,sac3,other=[],[],[],[]
				j=0
				while j < len(tmp):
					N,sp = tmp[j],memo[j]
					if N == minor1:
						sac1.append(sp)
					elif N == minor2:
						sac2.append(sp)
					elif N == minor3:
						sac3.append(sp)
					else:
						other.append(sp)
					j+=1
				INTRA,INTER=[],[]
				for st1 in sac1:
					for st2 in sac1:
						if st1 != st2:
							INTRA.append(dist[st1][st2])
					for st2 in other:
						INTER.append(dist[st1][st2])
				if max(INTRA) > min(INTER):
					r+=1
					toto='r'
				else:
					toto='m'
					m+=1	
				#print i,' ',tot,' ',unique,' ',number,' ',minor1,' ',min(INTRA),' ',min(INTER),' ',toto
				bip.append(toto)
				INTRA,INTER=[],[]
				for st1 in sac2:
					for st2 in sac2:
						if st1 != st2:
							INTRA.append(dist[st1][st2])
					for st2 in other:
						INTER.append(dist[st1][st2])
				if max(INTRA) > min(INTER):
					r+=1
					toto='r'
				else:
					toto='m'
					m+=1
				#print i,' ',tot,' ',unique,' ',number,' ',minor2,' ',min(INTRA),' ',min(INTER),' ',toto
				bip.append(toto)
				INTRA,INTER=[],[]
				for st1 in sac3:
					for st2 in sac3:
						if st1 != st2:
							INTRA.append(dist[st1][st2])
					for st2 in other:
						INTER.append(dist[st1][st2])
				if max(INTRA) > min(INTER):
					r+=1
					toto='r'
				else:
					toto='m'
					m+=1
				#print i,' ',tot,' ',unique,' ',number,' ',minor3,' ',min(INTRA),' ',min(INTER),' ',toto
				bip.append(toto)
		i+=1
	try:
		rm = float(r)/m
	except ZeroDivisionError:
		rm = 'NA'
	print  SP, len(strains),' r/m= ', rm      #,' r= ',r,' m= ',m	, '   Bips:  r= ',bip.count('r'),'  m= ',bip.count('m'),' |  for ',singleton,' singleton'
	h=open(PATH_TO_UPLOAD + 'rm1.txt',"a")
	h.write(truc + '\t' + str(r) + '\t' + str(m) + '\t' + str(rm) + '\t' + str(len(bip)) + '\n'   )
	h.close()