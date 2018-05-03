from config import *
import sys
import os
from multiprocessing import Pool

args = []
for arg in sys.argv:
	args.append(arg.lower())

import findRepForBigSpecies as readRaxml



dico={}
species = []


placesWithSpecies = ['a_website','b_problemFolk','c_med_ready_boys','medlostboys']

existingSpecies = []
for local in placesWithSpecies:
	existingSpecies.extend(os.listdir('/Users/ochmanlab/Desktop/ConSpeciFix/env/work/Ochman/brian/'+local))



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







speciesWeHaveDistancesFor = []
possibleBigSpecies = os.listdir('/Volumes/APE_MacPro_External_2/brian/distances/')
for item in possibleBigSpecies:
	speciesWeHaveDistancesFor.append(item.rstrip('.txt').lstrip('names_').lstrip('distances_'))

speciesWeHaveDistancesFor = list(set(speciesWeHaveDistancesFor))





bigSpecies = []
count = 0
totalStrainsCount = 0

needsToBeDone = []
needsToAskLm = []


for sp in species:
	if dico[sp]>20 and (not sp in existingSpecies):
		# if dico[sp]>500:
		# 	bigSpecies.append(sp)
		# else:
		print sp, dico[sp], sp in speciesWeHaveDistancesFor
		if sp in speciesWeHaveDistancesFor:
			needsToBeDone.append(sp)
		else:
			needsToAskLm.append(sp)
		count+=1

print needsToAskLm


# for sp in species:
# 	if dico[sp] > 15:
# 		totalStrainsCount+=dico[sp]

print"_________________"
print count
print"_________________"


if __name__ == '__main__':
	p = Pool(16)
	p.map(readRaxml.sample,needsToBeDone)



# for sp in bigSpecies:
# 	print sp, dico[sp]

# print len(bigSpecies)

# print "total strains: "+str(totalStrainsCount) 