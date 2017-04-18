from config import *
import os

species = giveMulti(getSelectedSpecies())

for sp in species:
	try:
		h=open(PATH_TO_OUTPUT + sp + '/concat85.fa',"r")
		h.close()
		print sp + ' it is done'
	except:
		print sp + ' it aint'