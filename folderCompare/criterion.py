from config import *
import os
import datetime
import time
ts = time.time()

h=open(PATH_TO_FOLDER + "results.txt","w")
header = "Conspecifix Results:\n\n\tCompleted on: "+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') +"\n"
header = header + '\tFolder Path: ' + PATH_TO_FOLDER +'\n\n'
header = header + """	For more information about our process, please visit our website at
	https://www.conspecifix.com
	or take a look at our github
	https://github.com/Bobay-Ochman
"""

header = header + "\nThe following strains are members of the species:\n"

h.write(header)

kick=[]
keep = []
tag="no"
f = None
try:
	f=open(PATH_TO_MAT +"kmeans.txt","r")
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
			tag="y"
		else:
			keep.append(st)

h.write('\n'.join(keep) + '\n\n')

if tag is "no":
	h.write("All strains were determined to be a member of the species")
else:
	h.write("The following strains were determined to NOT be a member of the species:\n")
	h.write('\n'.join(kick) + '\n')

f.close()
