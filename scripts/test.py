from config import *
import os

species = getSpeciesOfSize(500)
for sp in species:
	print sp
	os.system('mv /work/03414/be4833/inputs/input_'+sp+'.txt '+PATH_TO_OUTPUT + sp + '/input_'+sp+'.txt')