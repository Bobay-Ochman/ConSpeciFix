from config import *
import os

print PATH_TO_OUTPUT

spec = getSpecies()
for sp in spec:
	files = os.listdir(PATH_TO_OUTPUT+sp+'/align/')
	print sp
	for f in files:
		if(f.endswith('.align')):
			os.remove(PATH_TO_OUTPUT+sp+'/align/'+str(f))