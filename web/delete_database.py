from config import *
import os

species=getSingleSpecies()
sp = species[0]
PATH = '/var/app/current/efs/results/'

#we need to do some threadsafety here, but like fingers crossed this won't be an issue until we are NCBIg

fd = open(PATH+sp+'/useCounter.txt','r')
numbUsers = len(f.read().split('\n'))
if numbUsers < 3:#because if there is one non-zero, there'll be a trailing newline.
	#delete the system, we are the last
	os.system('rm -rf 'PATH+sp)
	os.system('rm -rf 'PATH+sp+'.zip')
else:
	#there are others using it, so we need to not delete it.
	fd.close()
	fd = open(PATH+sp+'/useCounter.txt','w')
	for i in range(numbUsers):
		fd.write(i+'\n')
	fd.close()