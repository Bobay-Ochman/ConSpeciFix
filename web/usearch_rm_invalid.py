import os

f = open('todo/usearch_re_do.txt','r')
for l in f:
	args = l.strip('\n').split('\t')
	os.system('rm '+args[0]+str(args[1]) + '/BBH/'+ args[2]+'-'+args[3])