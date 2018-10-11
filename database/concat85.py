from config import *
import os
import sys
from multiprocessing import Pool

def concatForSpec(sp):
	printLog('starting '+sp)
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
		for ortho in genes[sp]:
			print sp, ortho
			f = None
			try:
				f=open( PATH_TO_OUTPUT + sp + '/align/'  + ortho + ".fa.align","r")
				if os.stat(PATH_TO_OUTPUT + sp + '/align/'  + ortho + ".fa.align").st_size == 0:
					raise NotImplementedError("ortho file is empty, skipping.")
			except Exception as e:
				print 'failing to do '+sp+' - '+ortho
				continue
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
		for st in strains[sp]:
			if ('G' not in concat[sp][st]) and ('A' not in concat[sp][st]) and ('T' not in concat[sp][st]) and ('C' not in concat[sp][st]):
				print 'no values found for: '+st
				strains[sp].remove(st)
	
	for sp in species:
		h=open(PATH_TO_OUTPUT+sp + '/concat85.fa',"w")
		for st in strains[sp]:
			h.write(">" + st + "\n")
			i=0
			while i < len(concat[sp][st]):		# MODIF 
				h.write(concat[sp][st][i:i+60] + "\n")
				i+=60
		h.close()
	print 'completed! '+str(species[0])

def wrapper(args):
	try:
		concatForSpec(args)
	except Exception as e:
	    exc_type, exc_obj, exc_tb = sys.exc_info()
	    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	    print(exc_type, fname, exc_tb.tb_lineno)


if __name__ == '__main__':
	species = giveMulti(getSelectedSpecies("align/ortho1.fa.align"))	
	p = Pool(MAX_THREADS)
	p.map(wrapper,species)


#"""
