from config import *
import os

species=getSingleSpecies()

sp = species[0]

PATH = '/var/app/current/efs/results/'

try:
	#see if we already have the goods downloaded
	fd = open(PATH + sp+'/orthologs.txt')
except:
	os.system("wget -A.zip 'http://conspecifix-data-bucket.s3.amazonaws.com/"+sp+".zip' -P "+PATH)
	os.system("unzip "+PATH+sp+'.zip -d '+PATH)

#It won't be perfectly threadsafe, but that shouldn't matter with our usage
os.system("echo '1' >> useCounter.txt")
