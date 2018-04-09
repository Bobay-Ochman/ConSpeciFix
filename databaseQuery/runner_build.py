from config import *
import os
import sys


todoFile = open('todo/runner.txt','w')
for trial in os.listdir(PATH_TO_QUERY_SPEC):
	if trial == '.DS_Store':
		continue
	if not os.path.isfile(PATH_TO_QUERY_SPEC+trial+'/criterion.txt'):
		params = open(PATH_TO_QUERY_SPEC+trial+'/params.txt').readlines()
		print params
		timestamp = params[0].strip('\n')
		fileName = params[1].strip('.fa\n')
		species = params[2].strip('\n')
		email = params[3].strip('\n')
		arg = 'web/runner.py '+species+' '+fileName+' '+timestamp+' '+email+'\n'
		todoFile.write(arg)

todoFile.close()
