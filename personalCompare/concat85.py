from config import *
import os
from multiprocessing import Pool

strains = [strainFAFile for strainFAFile in os.listdir(PATH_TO_FOLDER) if str(strainFAFile).endswith('.fa')]
	
genes=[]
orthologues={}
f=open( PATH_TO_MAT + 'orthologs.txt',"r")
for l in f:
	a=l.strip("\n").split("\t")
	orthologues[a[0]]=a[1:]
	genes.append(a[0])
f.close()

parent={}
for st in strains:
	f=open(PATH_TO_FOLDER + st,"r")
	for l in f:
		if l[0] == ">":
			id = l.strip("\n").strip(">").split(" ")[0]
			if parent.has_key(id):
				print "PROBLEM !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
			parent[id] = st
	f.close()


tmp={}
for st in strains:
	tmp[st] = []
for ortho in genes:
	print ortho
	f = None
	try:
		f=open( PATH_TO_MAT + 'align/'  + ortho + ".fa.align","r")
	except IOError as e:
		print e
		print ortho
		exit()
	flash={}
	memo=[]
	maxLen = 0;
	for l in f:
		if l[0] == ">":
			id = l.strip("\n").strip(">").split(" ")[0]
			st = parent[id]
			memo.append(st)
			flash[st]=[]
		else:
			flash[st].append(l.strip("\n").upper())
	f.close()
	longueur = ''.join(flash[memo[0]])
	for st in strains:
		if flash.has_key(st):
			resu = ''.join(flash[st])
		else:
			resu = '-'*len(longueur)
		tmp[st].append(resu)


concat={}
for id in tmp:
	concat[id] = ''.join(tmp[id])
tmp={}

h=open(PATH_TO_MAT+'concat85.fa',"w")
for st in strains:
	if ('A' not in concat[st]) and ('S' not in concat[st]) and ('T' not in concat[st]) and ('G' not in concat[st]):
		continue
	h.write(">" + st + "\n")
	i=0
	while i < len(concat[st]):		# MODIF 
		h.write(concat[st][i:i+60] + "\n")
		i+=60
h.close()
print 'completed! '