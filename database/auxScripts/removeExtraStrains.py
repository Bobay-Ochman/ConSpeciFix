import os
import sys

bigSpecLists = '/Volumes/APE_MacPro_External_2/brian/bigspecies/'
futureContainers = '/Volumes/APE_MacPro_External_2/brian/futureJobContainers/'


containers = os.listdir(futureContainers)
for i in range(len(containers)):
	containers[i] = containers[i].strip('cont_')

for file in os.listdir(bigSpecLists):
	spname= file.strip('list_').strip('.txt')


print containers.remove('.DS_Store')
for cont in containers:
	try:
		strains = []
		fd = open(bigSpecLists+'list_'+cont+'.txt','r')
		lines= fd.readlines()
		for l in lines:
			if 'excluded' in l.split('\t')[2]:
				strains.append(l.split('\t')[1])
		fd = open(futureContainers+'cont_'+cont+'/'+cont+'/redundantStrains.txt','w')
		fd.write('\n'.join(strains))
	except:
		print "Unexpected error:", sys.exc_info()[0]
















