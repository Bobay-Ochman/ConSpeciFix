import os
from config import *
import sys
import time

#https://www.ncbi.nlm.nih.gov/genomes/Genome2BE/genome2srv.cgi?action=download&orgn=&report=proks&status=50|40|30|20|%3Bnopartial|noanomalous|&group=--%20All%20Prokaryotes%20--&subgroup=--%20All%20Prokaryotes%20--&format=

database = os.listdir('/Volumes/ITDR/brian/websiteOutput/')

for file in os.listdir('/Volumes/ITDR/brian/genomesForComparison'):
	fullName = file.split('.')[0]
	genus = fullName.split('_')[0]
	species = fullName.split('_')[1]
	for websiteSpecies in database:
		if websiteSpecies.startswith(genus):
			print file+' '+websiteSpecies
			stamp = str(time.time())
			os.mkdir("/Volumes/ITDR/brian/databaseQuerySpecies/"+stamp)
			os.system('cp /Volumes/ITDR/brian/genomesForComparison/'+file+' /Volumes/ITDR/brian/databaseQuerySpecies/'+stamp+'/'+file)
			paramsFile = open('/Volumes/ITDR/brian/databaseQuerySpecies/'+stamp+'/params.txt','w')
			paramsFile.write(stamp+'\n')
			paramsFile.write(file+'\n')
			paramsFile.write(websiteSpecies+'\n')
			paramsFile.write('conspecifix@gmail.com\n')
			paramsFile.close()
			time.sleep(.01)