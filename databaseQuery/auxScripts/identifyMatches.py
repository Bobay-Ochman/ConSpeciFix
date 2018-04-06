import os
import listAllSpecies

genusSizes = listAllSpecies.getSize()

print genusSizes

myPath = '/Users/ochmanlab/Desktop/ConSpeciFix/env/work/Ochman/brian/databaseQuerySpecies/'

interesting = {}
match = {}
noMatch = {}

for trial in os.listdir(myPath):
	if trial == '.DS_Store':
		continue
	if os.path.isfile(myPath+trial+'/criterion.txt'):
		print trial
#		print line
		allFiles = os.listdir(myPath+trial)
		myFileName = ''
		mySpeciesName = ''
		for f in allFiles:
			if '.fa' in f and 'concat85.fa' not in f:
				myFileName = f
			if 'distrib_' in f and '.txt' in f:
				mySpeciesName= f.strip('distrib_').strip('.txt')
				print mySpeciesName

		fd = open(myPath+trial+'/criterion.txt','r')
		lines = fd.readlines()
		line = lines[-1]
		if 'All strains were determined' in line:
			if(not mySpeciesName in match):
				match[mySpeciesName] = []
			match[mySpeciesName].append(str(myFileName)+','+str(trial))
		else:
			if(not mySpeciesName in noMatch):
				noMatch[mySpeciesName] = []
			noMatch[mySpeciesName].append(str(myFileName)+','+str(trial))

print "--------------------------------------------------------------"

fd = open('match.csv','w')
fd.write(','.join(['Species Name','# species in genus','# WITH gene flow','# WITHOUT','# Left to compute'])+'\n')
for key in sorted(match.keys()):
	genusName = listAllSpecies.genusName(key)
	thisSize = genusSizes[genusName]
	printItems = [key,str(thisSize),str(len(match[key]))]
	if key in noMatch:
		printItems.append(str(len(noMatch[key])))
		printItems.append(str(thisSize - (len(match[key]) + len(noMatch[key]))))
	else:
		printItems.append(str(0))
		printItems.append(str(thisSize - len(match[key])))

	fd.write(','.join(printItems)+'\n')


fd.write('\n\n\n\nSpecies with no evidence of gene flow yet*\n\n')
fd.write(','.join(['Species Name','# species in genus','# WITH gene flow','# WITHOUT','# Left to compute'])+'\n')
for key in sorted(noMatch.keys()):
	genusName = listAllSpecies.genusName(key)
	thisSize = genusSizes[genusName]
	printItems = [key,str(thisSize),str(0),str(len(noMatch[key]))]
	printItems.append(str(thisSize - len(noMatch[key])))
	if not key in match:
		fd.write(','.join(printItems)+'\n')

fd.truncate()
fd.close()
