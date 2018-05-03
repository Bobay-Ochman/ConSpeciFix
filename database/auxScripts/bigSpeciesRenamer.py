

import os


PREFIX = '/Volumes/APE_MacPro_External_2/brian/distances/'




speciesWeHaveDistancesFor = []
possibleBigSpecies = os.listdir('/Volumes/APE_MacPro_External_2/brian/distances/')
for item in possibleBigSpecies:
	if '100_' in item:
		speciesWeHaveDistancesFor.append(item.rstrip('.txt').lstrip('100_'))

speciesWeHaveDistancesFor = list(set(speciesWeHaveDistancesFor))

for sp in speciesWeHaveDistancesFor:
	nameKeyMap = {}
	strainNames = []
	orig = open(PREFIX+'100_'+sp+'.txt','r')
	namekey = open(PREFIX+'names_'+sp+'.txt','r')
	for l in namekey.readlines():
		bits = l.strip().split('\t')
		nameKeyMap[bits[0]] = bits[1]
	for l in orig.readlines():
		strainNames.append(nameKeyMap[l.strip()])

	fd = open(PREFIX+'strains_'+sp+'.txt','w')
	fd.write('\n'.join(strainNames))
