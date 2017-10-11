import os
from config import *

species = getSpecies()

dico,info={},{}
f=open("../genomes_proks.txt","r")
for l in f:
	if l[0] != "#":
		a=l.strip("\n").split("\t")
		b = a[0].split(" ")
		if len(b) > 1 and b[1] != "sp.":
			sp = b[0] + "_" + b[1]
			if "Candidatus_" not in sp and "_cluster" not in sp and "_group" not in sp:
				if dico.has_key(sp):
					dico[sp]+=1
					info[sp].append(l.strip("\n"))
				else:	
					dico[sp]=1
					info[sp]=[l.strip("\n")]

f.close()

for sp in species:
	print sp,' ',len(info[sp])

tot = 0
nb=0
for sp in species:
	if dico[sp] >=15:
		#print sp," ",dico[sp]
		tot += dico[sp]
		nb += 1


print "Total= ",tot," ",nb


download = open('todo/download.txt','w')


for sp in species:
	for l in info[sp]:
		a=l.strip("\n").strip("\r").split("\t")
		tmp=[]
		for stuff in a:
			if 'ftp://' in stuff:
				tmp.append(stuff)
		if len(tmp) > 0:
			#print sp
			ftp = tmp[0]
			id1 = ftp.split('/')[-1] + '_genomic.fna.gz'
			id2 = ftp.split('/')[-1] + '_genomic.gff.gz'
			
			download.write('wget ' + ftp + '/' + id1 + '\t')
			download.write('wget ' + ftp + '/' + id2  + '\t')
			download.write('mv  ' + id1 + '    ' + PATH_TO_OUTPUT + sp + '/genomes/' + '\t')
			download.write('mv  ' + id2 + '    ' + PATH_TO_OUTPUT + sp + '/genomes/' + '\n')
			
		#	os.system('wget ' + ftp + '/' + id1 )
		#	os.system('mv  ' + id1 + '    ' + PATH_TO_OUTPUT + sp + '/genomes/' )
		#	os.system('wget ' + ftp + '/' + id2 )
		#	os.system('mv  ' + id2 + '    ' + PATH_TO_OUTPUT + sp + '/genomes/' )
		
download.truncate()
download.close()






















