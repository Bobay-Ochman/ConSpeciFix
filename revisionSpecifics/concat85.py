from config import *
import os
import random
from multiprocessing import Pool

def concatForSpec(sp):
	printLog('starting '+sp)
	geneSubsetNo = sp.split('\t')[1]
	sp = sp.split('\t')[0]

	species = [sp]
	strains=getGenomes(species)
	
	genes={}
	orthologues={}
	for sp in species:
		genes[sp]=[]
		orthologues[sp]={}
		f=open( PATH_TO_OUTPUT+ sp + '/orthologs.txt',"r")
		for l in f:
			a=l.strip("\n").split("\t")
			orthologues[sp][a[0]]=a[1:]
			genes[sp].append(a[0])
		f.close()

	#This is where we will go about truncating down the number of genes
	newGeneList = []
	random.shuffle(genes[sp])
	for i in range(100):
		newGeneList.append(genes[sp].pop())

	parent={}
	for sp in species:
		for st in strains[sp]:
			f=open(PATH_TO_OUTPUT + sp + '/genes/' + st,"r")
			for l in f:
				if l[0] == ">":
					id = l.strip("\n").strip(">").split(" ")[0]
					if parent.has_key(id):
						print "PROBLEM !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
					parent[id] = st
			f.close()

	exclusion=[]



	tmp={}
	for sp in species:
		tmp[sp]={}
		for st in strains[sp]:
			tmp[sp][st] = []
		for ortho in newGeneList:
			print sp, ortho
			f = None
			try:
				f=open( PATH_TO_OUTPUT + sp + '/align/'  + ortho + ".fa.align","r")
			except IOError as e:
				print 'failing to do '+sp
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
			for st in strains[sp]:
				if flash.has_key(st):
					resu = ''.join(flash[st])
				else:
					resu = '-'*len(longueur)
				tmp[sp][st].append(resu)


	concat={}
	for sp in species:
		concat[sp]={}
		for id in tmp[sp]:
			concat[sp][id] = ''.join(tmp[sp][id])

	tmp={}

	for sp in species:
		h=open(PATH_TO_OUTPUT+sp + '/geneSubsets/geneSubsetNo'+geneSubsetNo+'/concat85.fa',"w")
		for st in strains[sp]:
			h.write(">" + st + "\n")
			i=0
			while i < len(concat[sp][st]):		# MODIF 
				h.write(concat[sp][st][i:i+60] + "\n")
				i+=60
		h.truncate()
		h.close()
	print 'completed! '+str(species[0])

def wrapper(args):
	try:
		concatForSpec(args)
	except:
		print 'exception!' + str(args)

if __name__ == '__main__':
	species = giveMulti(getSelectedSpecies("align/ortho1.fa.align"))	
	args = []
	for sp in species:
		for i in range(100):
			args.append(sp+'\t'+str(i))
	p = Pool(MAX_THREADS)
	p.map(wrapper,args)


#"""
