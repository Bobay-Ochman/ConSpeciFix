from config import *
import os

specFolders = ''

for sp in ['Gallibacterium_anatis','Lactobacillus_crispatus','Porphyromonas_gingivalis','Mycobacterium_colombiense']:
	specFolders += ' ' + sp
os.chdir(PATH_TO_OUTPUT)
os.system('tar -c -f export.zip '+specFolders)

print 'selected folders compressed into export.zip!'