from config import *
import os
import datetime
import time
ts = time.time()

species=getSelectedSpecies('kmeans.txt')

kick={}
tag={}
for sp in species:
	h=open(PATH_TO_OUTPUT + sp + "/criterion.txt","w")

	header = "Conspecifix Results:\n\n\tCompleted on: "+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') +"\n"
	header = header + '\tSpecies: ' + sp  +'\n\n'
	header = header + """	For more information about our process, please visit our website at
	https://www.conspecifix.com
	or take a look at our github
	https://github.com/Bobay-Ochman

	Exclusion Criterion defined in Bobay & Ochman, GBE 2017
	
"""

	header = header + "\nThe following strains are members of the species:\n"
	h.write(header)

	kick=[]
	keep = []
	tag="no"
	f = None
	try:
		f=open(PATH_TO_OUTPUT + sp +"/kmeans.txt","r")
	except Exception as e:
		print str(e)
	for l in f:
		a=l.strip('\n').split('\t')
		st = a[0]
		if st != "tot":
			mode1,mode2=float(a[1]),float(a[3])
			tot=mode1+mode2
			ratio = mode2/tot
			line = st + "\n"
			if ratio ==0:
				kick.append(st)
				print sp, st
				tag="y"
			else:
				keep.append(st)

	h.write('\n'.join(keep) + '\n\n')

	if tag is "no":
		h.write("All strains were determined to be a member of the species")
	else:
		h.write("The following strains were determined to NOT be a member of the species:\n")
		h.write('\n'.join(kick) + '\n')

	h.truncate()
	h.close()
	f.close()