from config import *
import os
import datetime
import time
ts = time.time()

species=getSingleSpecies()

h=open(PATH_TO_UPLOAD + "criterion.txt","w")

critInfoFD = open(PATH_TO_UPLOAD+'crit_stats.txt','a')
critInfoFD.write('Member of '+str(getSingleSpecies()[0])+' according to Exclusion Criterion*: ')

for sp in species:
	kick = []
	keep = []
	tag="no"
	f = None
	try:
		f=open(PATH_TO_UPLOAD +"kmeans_" + sp + ".txt","r")
	except:
		continue
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
				tag="yes"
			else:
				keep.append(st)
	f.close()

header = "Conspecifix Results:\n\n\tCompleted on: "+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') +"\n\n"
header = header + """	For more information about our process, please visit our website at
	https://www.conspecifix.com
	or take a look at our github
	https://github.com/Bobay-Ochman

	Exclusion Criterion defined in Bobay & Ochman, GBE 2017
	
"""

header = header + "\nThe following strains are members of the species:\n"

h.write(header)

h.write('\n'.join(keep) + '\n\n')

if tag is "no":
	h.write("All strains were determined to be a member of the species")
else:
	h.write("The following strains were determined to NOT be a member of the species:\n")
	h.write('\n'.join(kick) + '\n')

h.truncate()
h.close()

if tag is "yes": #Tag is if something got excluded
	critInfoFD.write('no') #so if it did, we write "no"t a member of the species
else:
	critInfoFD.write('yes')

critInfoFD.write('\n\n*Please refer to Bobay & Ochman, GBE 2017')
critInfoFD.close()






