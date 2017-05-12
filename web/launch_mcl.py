from multiprocessing import Pool
import multiprocessing
import os
from config import *

def mclOnSpec(sp):
	print 'mcl on',sp
	#os.system('mv '+PATH_TO_OUTPUT + sp + '/input.txt '+ PATH_TO_OUTPUT + sp + '/input_' + sp + '.txt' )
	os.system(MCL_PATH+' ' + PATH_TO_UPLOAD +'input_' + sp + '.txt --abc -I 1.2')
	os.system('mv  out.input_' + sp + '.txt.I12 ' + PATH_TO_UPLOAD)

mclOnSpec(getSingleSpecies()[0])