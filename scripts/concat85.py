from config import *
import os
from multiprocessing import Pool

def concatForSpec(sp):
	
	"""
	try:
		h=open(PATH_TO_OUTPUT + sp + '/concat85.fa',"r")
		h.close()
		return
	except:
		pass
	"""
	
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



	tirets='------------------------------------------------------------------'
	tmp={}
	for sp in species:
		tmp[sp]={}
		for ortho in genes[sp]:
			printLog(sp+' '+ortho)
			f=open( PATH_TO_OUTPUT+ sp + '/align/'  + ortho + ".fa","r")
			memo=[]
			for l in f:
				if l[0] == ">":
					id = l.strip("\n").strip(">").split(" ")[0]
					st = parent[id]
					memo.append(st)
					if tmp[sp].has_key(st):
						pass
					else:
						tmp[sp][st]=''
				else:
					tmp[sp][st]+=l.strip("\n").upper()
					longueur = len(tmp[sp][st])
			f.close()
			for st in strains[sp]:
				if tmp[sp].has_key(st):
					pass
				else:
					tmp[sp][st]=''
				if len(tmp[sp][st]) < longueur:
					while len(tmp[sp][st]) < longueur:
						#print st, ' ',len(tmp[sp][st]),' ',longueur
						tmp[sp][st]+='-'

	concat={}
	for sp in species:
		concat[sp]={}
		for id in tmp[sp]:
			concat[sp][id] = tmp[sp][id]


	tmp={}






	for sp in species:
		h=open(PATH_TO_OUTPUT + sp + '/concat85.fa',"w")
		for st in strains[sp]:
			h.write(">" + st + "\n")
			i=0
			while i < len(concat[sp][st]):		# MODIF 
				h.write(concat[sp][st][i:i+60] + "\n")
				i+=60
		h.close()



	printLog('Writing falip')

	for sp in species:
		h=open(PATH_TO_OUTPUT + sp + '/concat85.fa',"w")
		st1 = concat[sp].keys()[0]
		longueur = len(concat[sp][st1])
		h.write("   " + str(len(strains[sp])) + " " + str(longueur) + "\n")
		for st in strains[sp]:
			resu = st
			while len(resu) < 52:
				resu += " "
			i=0
			while i in range(60):
				resu+=concat[sp][st][i:i+10] + " "
				i+=10
			h.write(resu + "\n")
		h.write("\n")
		j=60
		while j < longueur:
			for st in strains[sp]:
				h.write("                                                    " + concat[sp][st][j:j+10] + " " + concat[sp][st][j+10:j+20] + " " + concat[sp][st][j+20:j+30] + " "  + concat[sp][st][j+30:j+40] + " " + concat[sp][st][j+40:j+50] + " " +  concat[sp][st][j+50:j+60] + "\n")
			h.write("\n")
			j+=60
		h.close()



if __name__ == '__main__':
	species = giveMulti(getSelectedSpecies())
	#species = ['Acetobacter_pasteurianus']
	p = Pool(MAX_THREADS)
	p.map(concatForSpec,species)




