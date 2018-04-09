from config import *
import sys

args = []
for arg in sys.argv:
	args.append(arg.lower())


dico={}
species=[]

#The latest download from NCBI detailing all genomes possible
f=open('../../genomes_proks.txt','r')

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

existingSpecies = getAllSpecies()
bigSpecies = []
for sp in species:
	if dico[sp]>15 and (not sp in existingSpecies):
		if dico[sp]>500:
			bigSpecies.append(sp)
		else:
			print sp, dico[sp]
print"_________________"
for sp in bigSpecies:
	print sp, dico[sp]
