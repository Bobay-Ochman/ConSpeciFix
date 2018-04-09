from config import *
import os

species = getAllSpecies()

edditedSpecies = []


for sp in species:
	fdhm = open(PATH_TO_OUTPUT+sp+'/rm1.txt','r')
	completedSets = []
	for l in fdhm.readlines():
		parts = l.split('\t')
		parts = parts[0].split('&&&')
		completedSets.append('&&&'.join(sorted(parts)))
	completedSets = set(completedSets)

	fdhm = open('../todo/calcHM.txt','r')
	species = ''
	todoSets = []
	for l in fdhm.readlines():
		parts = l.strip('\n').split('\t')
		parts = parts[1].split('&&&')
		species = parts[0]
		todoSets.append('&&&'.join(sorted(parts)))
	todoSets = set(todoSets)
	leftSets = todoSets - completedSets
	print len(todoSets)
	print len(completedSets)
	print len(leftSets)

	newTodo = open('../todo/calcHM_new.txt','w')
	for item in leftSets:
		newTodo.write(sp+'\t'+item+'\n')
	newTodo.truncate()
	newTodo.close()