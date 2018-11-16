import os
import random

totalStrains = []

pathToAll = '/stor/work/Ochman/brian/DoneDengue/'
pathToOutput = '/stor/work/Ochman/brian/RefinedDengue/'
pathToSample = '/_conspecifix/database/User_spec/sample.txt'
for f in os.listdir(pathToAll):
	os.mkdir(pathToOutput+f)
	fd = open(pathToAll+f+pathToSample)
	for l in fd.readlines():
		l = l.strip()
		os.system(' cp '+pathToAll+f+'/'+l +' '+pathToOutput+f)