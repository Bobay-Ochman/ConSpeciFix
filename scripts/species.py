from config import *

dico={}
species=[]

#The latest download from NCBI detailing all genomes possible
f=open('../genomes_proks.txt','r')

#filter out the ones that are not proper species
for l in f:
	if l[0]!='#':
		a=l.strip('\n').split('\t')
		sp = a[0]
		b = sp.split(' ')
		if len(b) > 1:
			sp = b[0] + '_' + b[1]
			if 'Candidatus' not in sp and b[1] != 'sp.' and b[1] != 'cluster' and b[1] != 'group':
				if b[0].startswith('bacterium') or b[1].startswith('bacterium') or b[0].startswith('archaeon')  or b[1].startswith('archaeon')   or  b[0].startswith('[') or b[0][0].islower() or not b[1][0].islower():
					pass
				else:
					if dico.has_key(sp):
						dico[sp]+=1
					else:
						dico[sp]=1
						species.append(sp)
f.close()

species.sort()

#Create species.txt
h=open(PATH_TO_SPECIES_TXT,'w')
NB=0
for sp in species:
	#We need at least 15 to have statistically relevant datasets.
	if dico[sp] >= 15 and dico[sp]< 20:
		NB+=1
		#print sp,' ',dico[sp]
		h.write(sp + '\t' + str(dico[sp]) + '\n')
	if dico[sp] > 19 and dico[sp]<30:
		print 'rm -r ', sp
h.truncate()
h.close()
print NB


