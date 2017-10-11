from multiprocessing import Pool
import multiprocessing
import os
from config import *


strains = [strainFAFile for strainFAFile in os.listdir(PATH_TO_FOLDER) if str(strainFAFile).endswith('.fa')]
parent={}
tmp={}
genes=[]
for st in strains:
	nb=0
	f=open(PATH_TO_FOLDER + st,"r")
	for l in f:
		if l[0] == ">":
			#should add .strip('+').strip('-')
			id = l.strip("\n").strip(">").split(" ")[0]
			if parent.has_key(id):
				print "PROBLEM !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
			parent[id] = st
			nb+=1
			tmp[id]=[]
		else:
			tmp[id].append(l)
	f.close()
	genes.append(nb)

seq={}
for id in tmp:
	seq[id] = "".join(tmp[id])

tmp={}

doublons=0
core=[]
f = None
try:
	f=open(PATH_TO_MAT + 'out.input.txt.I12',"r")
except:
	print 'skipping!'
for l in f:
	a=l.strip("\n").split("\t")
	tmp=[]
	for id in a:
		try:
			st = parent[id]
			if st in strains:
				tmp.append(id)
		except KeyError:
			pass
	a=list(tmp)
	if len(a) >= 0.85 * len(strains):
		tmp=[]
		tag=0
		b=[]
		for id in a:
			if parent.has_key(id):
				st = parent[id]
				if st not in tmp:
					tmp.append(st)
				else:
					tag=1
				b.append(st)
		if tag == 1:
			doublons += 1
		if len(tmp) >= 0.85 * len(strains) and tag==0:
			core.append(a)
f.close()

#Remove all alignment files
try:
	files = os.listdir(PATH_TO_MAT + 'align/')
	for f in files:
		os.remove(f)
except OSError:
	pass

h=open(PATH_TO_MAT + 'orthologs.txt',"w")
nb=0
for lili in core:
	nb+=1
	ortho = "ortho" + str(nb)
	h.write(ortho + "\t" + "\t".join(lili) + "\n")
	g=open(PATH_TO_MAT + 'align/' + ortho + ".fa","w")
	for id in lili:
		g.write(">" + id + "\n" + seq[id]  )
	g.truncate()
	g.close()	
h.close()

ratio = 0
if mean(genes) > 0:	
	ratio = nb/mean(genes)
	print 'There are ',nb,' core genes and ',doublons,' doublons ',mean(genes), ' genes on average for',len(strains),' strains.  Ratio=',100*nb/mean(genes),' %'






