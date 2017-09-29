import os
from config import *





os.chdir(PATH_TO_MAT)
print os.getcwd()
try:
	os.system('rm RAx*')
except:
	pass
os.system(RAXML_PATH+' -f x -T 10 -p 12345 -s ' +  ' concat85.fa  -m GTRGAMMA -n dist')




