from config import *
import os

species=getSingleSpecies()

sp = species[0]

try:
	#see if we already have the goods downloaded
	fd = open(PATH_TO_OUTPUT + sp+'/orthologs.txt')
except:
	os.system("wget -A.zip 'http://conspecifix-data-bucket.s3.amazonaws.com/"+sp+".zip' -P "+PATH_TO_OUTPUT)
	os.system("unzip "+PATH_TO_OUTPUT+sp+'.zip -d '+PATH_TO_OUTPUT)
	os.system('rm -rf '+PATH_TO_OUTPUT+sp+'.zip')

#It won't be perfectly threadsafe, but that shouldn't matter with our usage
os.system("echo '1' >> "+PATH_TO_OUTPUT+sp+"/useCounter.txt")
