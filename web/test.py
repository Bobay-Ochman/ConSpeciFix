f = open(testFile,'r')
out = open(testFile+"_clean.fa",'w')

count = 0
for l in f:
	if(l.startswith('>')):
		count+=1
		out.write('>gene'+str(count)+'\n')
	else:
		out.write(l)
out.close()
