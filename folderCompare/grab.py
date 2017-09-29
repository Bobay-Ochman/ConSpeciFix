from config import *
import os

species = getSpeciesOfSize(500)
print len(species)
for sp in species:
	os.system('cp '+PATH_TO_OUTPUT+sp+'/input_'+sp+'.txt inputs/')