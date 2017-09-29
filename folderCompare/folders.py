import os
from config import *

species=getSpecies()

for sp in species:
	try:
		os.mkdir(PATH_TO_OUTPUT + sp )
	except OSError:
		pass
	try:
		for folder in getFolders():
			os.mkdir(PATH_TO_OUTPUT + sp + folder)
	except OSError:
		pass




