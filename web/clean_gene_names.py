from config import *
import os

f = open(PATH_TO_UPLOAD+getCompStrain(),'r')
out = open(PATH_TO_UPLOAD+getCompStrain()+"_clean.fa",'w')

count = 0
for l in f:
	if(l.startswith('>')):
		count+=1
		out.write('>gene'+str(count)+'\n')
	else:
		out.write(l)
out.close()
os.system('mv '+PATH_TO_UPLOAD+getCompStrain()+"_clean.fa "+ PATH_TO_UPLOAD+getCompStrain())