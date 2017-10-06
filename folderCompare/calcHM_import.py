import os
from config import *
from multiprocessing import Pool
import multiprocessing
import traceback




def calcHMLoads(args,seq,dist):
	p = Pool(MAX_THREADS)
	f = open(PATH_TO_TODO + 'calcHM.txt','r')
	tupleArgs = []
	for l in args:
		tupleArgs.append((l,seq,dist))
	return p.map(wrapper,reversed(tupleArgs))




def wrapper(tupleArg):
	try:
		return calcHM(tupleArg[0],tupleArg[1],tupleArg[2])
	except Exception as e:
		print e
		traceback.print_exc()
		h = open (PATH_TO_TODO+'error.txt','a')



def calcHM(args,seq,dist):

	truc = args.strip('\n')
		
	alpha=['A','C','G','T']
	strains = truc.split('&&&')

	LONGUEUR = len(seq[strains[0]])
	for sp in strains:
		LONGUEUR=min(LONGUEUR,len(seq[sp]))

	if LONGUEUR > 1000000:
		LONGUEUR = 1000000
	
	bip=[]
	singleton,more=0,0
	i = 0
	r,m=0,0
	while i < LONGUEUR:
		tmp=[]
		memo=[]
		for sp in strains:
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
		return rm
	except:
		return -1
