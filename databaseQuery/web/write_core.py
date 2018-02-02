
from multiprocessing import Pool
import multiprocessing
import os
from config import *

species = getSingleSpecies()
strains=getStrains(species)
specialStrain = getCompStrain()+'.fa'
exclusion=[]
genes={}
parent={}
tmp={}


#get our ortholog matches loaded
orthologFD=open(PATH_TO_UPLOAD + 'orthologs.txt',"r")
core = {}
for line in orthologFD:
	l = line.strip('\n').split('\t')
	orthoName = l[0]
	l.pop(0)
	core[orthoName] = l[:] #deep copy l

#load all the genes
strains[species[0]].append(specialStrain)
for sp in species:
	tmp[sp]={}
	genes[sp]=[]
	for st in strains[sp]:
		nb=0
		if st != specialStrain:
			#print 'normal strain'
			f=open(PATH_TO_OUTPUT + sp + '/genes/' + st,"r")
		else:
			#print 'special strain'
			f=open(PATH_TO_UPLOAD + st,"r")
		for l in f:
			if l[0] == ">":
				#should add .strip('+').strip('-')
				id = l.strip("\n").strip(">").split(" ")[0]
				if parent.has_key(id):
					print "PROBLEM !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				parent[id] = st
				nb+=1
				tmp[sp][id]=[]
			else:
				tmp[sp][id].append(l)
		f.close()
		genes[sp].append(nb)



#convert the genes into readable format
seq={}
for sp in species:
	seq[sp]={}
	for id in tmp[sp]:
		seq[sp][id] = "".join(tmp[sp][id])


#output ortho(numb).fa
for sp in species:
	try:
		files = os.listdir(PATH_TO_UPLOAD + 'align/')
		for f in files:
			os.remove(f)
	except OSError:
		pass
	nb=0
	for lili in core:
		# Only write the core gene if 'gene###' is in the list
		flag = False
		for geneId in core[lili]:
			if 'gene' in geneId:
				flag=True
		if flag:
			nb = nb+1
			g=open(PATH_TO_UPLOAD+ 'align/' + lili + ".fa","w")
			for id in core[lili]:
				g.write(">" + id + "\n" + seq[sp][id]  )
			g.truncate()
			g.close()	

	critInfoFD = open(PATH_TO_UPLOAD+'crit_stats.txt','a')
	critInfoFD.write('Number of core genes orthologous to your genome: '+str(nb)+'\n')
	critInfoFD.close()


		