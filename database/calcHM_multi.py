import os
from config import *
from multiprocessing import Pool
import multiprocessing
import io

def calcHM(args):


	SP = args.strip('\n').split('\t')[0]
	truc = args.strip('\n').split('\t')[1]
		# Load distances
	strains=[]
	f=open(PATH_TO_OUTPUT + SP + '/sample.txt','r')
	for l in f:
		a=l.strip("\n").split("\t")
		strains.append(a[0])
	f.close()


	dist={}
	f=open(PATH_TO_OUTPUT + SP + '/RAxML_distances.dist',"r")
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
	f=open(PATH_TO_OUTPUT + SP + '/concat85.fa',"r")
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
				return
	f.close()


	seq = {}
	for sp in strains:
		seq[sp] = ''.join(tmp[sp])

	#strains.remove('Dsim')

	memo_subset={}
	tmp = os.listdir(PATH_TO_OUTPUT + SP + '/')
	for file in tmp:
		if file.startswith("rm"):
			f=open( PATH_TO_OUTPUT + SP + '/' + file,"r")
			for l in f:
				a=l.strip("\n").split("\t")
				if len(a) == 5:									
					memo_subset[a[0]] = a[1:]
			f.close()

		
	alpha=['A','C','G','T']

	LONGUEUR=len(seq[sp])
	if LONGUEUR > 1000000:
		LONGUEUR = 1000000
	
	strains = truc.split('&&&')
	bip=[]
	singleton,more=0,0
	i = 0
	r,m=0,0
	whatHappens = []
	while i < LONGUEUR:
		whatHappens.append([])
		tmp=[]
		memo=[]
		for sp in strains:
			lookingAtMe = False
			try:
				testing = seq[sp]
				lookingAtMe = True
				testing2 = testing[i]
			except KeyError as e:
				print 'we got some real problems now!!!! ',lookingAtMe,e,sp,SP
				errorFD = open('todo/exclusion.txt','a')
				errorFD.write(str(e)+'\n')
				errorFD.close()
				return
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
				whatHappens[i].append(['m',strains])
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
					whatHappens[i].append(['r',sac])
					toto='r'
				else:
					toto='m'
					whatHappens[i].append(['m',strains])
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
					whatHappens[i].append(['r',sac1])
				else:
					toto='m'
					whatHappens[i].append(['m',strains])
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
					whatHappens[i].append(['r',sac2])
				else:
					toto='m'
					whatHappens[i].append(['m',strains])
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
					whatHappens[i].append(['r',sac1])
				else:
					toto='m'
					whatHappens[i].append(['m',strains])
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
					whatHappens[i].append(['r',sac2])
				else:
					toto='m'
					whatHappens[i].append(['m',strains])
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
					whatHappens[i].append(['r',sac3])
				else:
					toto='m'
					whatHappens[i].append(['m',strains])
					m+=1
				#print i,' ',tot,' ',unique,' ',number,' ',minor3,' ',min(INTRA),' ',min(INTER),' ',toto
				bip.append(toto)
		i+=1
	try:
		rm = float(r)/m
	except ZeroDivisionError:
		rm = 'NA'
	print  SP, len(strains),' r/m= ', rm      #,' r= ',r,' m= ',m	, '   Bips:  r= ',bip.count('r'),'  m= ',bip.count('m'),' |  for ',singleton,' singleton'
	h=io.open(PATH_TO_OUTPUT + SP + '/rm1.txt',mode="a")
	h.write(unicode(str(truc + '\t' + str(r) + '\t' + str(m) + '\t' + str(rm) + '\t' + str(len(bip)) + '\n'   )))
	h.close()
	d=io.open("todo/completed.txt",mode='a')
	d.write(unicode(args))
	d.close()
	v=io.open(PATH_TO_OUTPUT + SP + '/visual.txt',mode="a")
	v.write(unicode(str(str(whatHappens)+ '\n')))
	v.close()

"""
f = open('todo/calcHM.txt','r')
args = []
for l in giveMulti(f.readlines()):
	if l.startswith('Clostridium_botulinum'):
		args.append(l)

for sp in args:
	calcHM(sp)

"""

def wrapper(arg):
	try:
		calcHM(arg)
	except Exception as e:
		print e
		h = open('todo/error.txt','a')
		h.write(str(arg)+'\t'+str(e)+'\n')
		h.close()

if __name__ == '__main__':
	print multiprocessing.cpu_count()
	p = Pool(MAX_THREADS)
	f = open('todo/calcHM.txt','r')
	args = []
	for l in giveMulti(f.readlines()):
		args.append(l)
	print "going!"
	p.map(wrapper,reversed(args))

#"""