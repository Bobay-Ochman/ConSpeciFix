from config import *

out = open(PATH_TO_TODO + 'mafft.txt','w')
out.seek(0)
files = os.listdir(PATH_TO_MAT + 'align/')
done = []
files = files[::-1]
#print files
nb = 0
for fichier in files:
	if str(fichier).endswith('.fa.align'):
		#We've already done it, we'll let them know
		continue
	if fichier+'.align' not in files:
		out.write(fichier + '\n');
		nb +=1
out.truncate()
out.close()
print 'todo list made with',nb,'files'