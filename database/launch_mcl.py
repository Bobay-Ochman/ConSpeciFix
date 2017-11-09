from multiprocessing import Pool
import multiprocessing
import os
from config import *

def mclOnSpec(sp):
	print 'mcl on',sp
	#os.system('mv '+PATH_TO_OUTPUT + sp + '/input.txt '+ PATH_TO_OUTPUT + sp + '/input_' + sp + '.txt' )
	os.system(MCL_PATH+' ' + PATH_TO_OUTPUT + sp + '/input_' + sp + '.txt --abc -I 1.2')
	os.system('mv  out.input_' + sp + '.txt.I12 ' + PATH_TO_OUTPUT + sp + '/')

if __name__ == '__main__':
	species = giveMulti(getAllSpecies())
	complete = []
	#makes a list of stuff we are done with
	for sp in species:
		try:
			k=open(PATH_TO_OUTPUT + sp + '/out.input_'+sp+'.txt.I12','r')
			complete.append(sp)
			k.close()
		except:
			pass

	todoSpec = []
	#makes the list of stuff left to do
	for sp in species:
		if sp in complete:
			continue
		try:
			k=open(PATH_TO_OUTPUT + sp + '/input_'+sp+'.txt','r')
			todoSpec.append(sp)
			k.close()
		except:
			pass
	#now lets get cracking
	print species
	print todoSpec
	print complete


	species = todoSpec
	p = Pool(MAX_THREADS)
	p.map(mclOnSpec,species)
