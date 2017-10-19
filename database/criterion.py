from config import *
import os
import datetime
import time
ts = time.time()

species=getSelectedSpecies('for_removal.txt')

kick={}
tag={}
for sp in species:
	h=open(PATH_TO_OUTPUT + sp + "/criterion.txt","w")

	header = "Conspecifix Results:\n\n\tCompleted on: "+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') +"\n"
	header = header + '\tSpecies: ' + sp  +'\n\n'
	header = header + """	For more information about our process, visit our website
	https://www.conspecifix.com
	or take a look at our github
	https://github.com/Bobay-Ochman

	Exclusion criterion based off a modified
	version of that found in Bobay & Ochman, GBE 2017
	
"""

	header = header + "\nThe following strains are members of the species:\n"
	h.write(header)

	kick=[]
	keep = []
	sample = None
	removal = None
	try:
		sample=open(PATH_TO_OUTPUT + sp +"/sample.txt","r")
		removal = open(PATH_TO_OUTPUT + sp + "/for_removal.txt","r")
		for l in removal:
			kick.append(l.strip('\n'))
		for l in sample:
			strain = l.strip('\n')
			if strain not in kick:
				keep.append(strain)
	except Exception as e:
		print str(e)
		continue
	
	h.write('\n'.join(keep) + '\n\n')

	if len(kick) == 0:
		h.write("All strains were determined to be a member of the species")
	else:
		h.write("The following strains were determined to NOT be a member of the species:\n")
		h.write('\n'.join(kick) + '\n')

	h.truncate()
	h.close()
	removal.close()
	sample.close()