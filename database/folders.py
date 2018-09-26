import os
from config import *

species=getSpecies()

for sp in species:
	print sp
	try:
		os.mkdir(PATH_TO_OUTPUT + sp )
		print "made folder! "+PATH_TO_OUTPUT + sp
	except OSError:
		print "error with folder: "+PATH_TO_OUTPUT + sp
	for folder in getFolders():
		try:
			os.mkdir(PATH_TO_OUTPUT + sp + folder)
			print "make folder!"+PATH_TO_OUTPUT + sp + folder
		except OSError:
			print "error with folder: "+PATH_TO_OUTPUT + sp + folder




