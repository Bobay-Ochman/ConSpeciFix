from config import *
import os

species=getSingleSpecies()

sp = species[0]

PATH = '/var/app/current/efs/results/'

os.system("wget -A.zip 'http://conspecifix-data-bucket.s3.amazonaws.com/"+sp+".zip' -P "+PATH)
os.system("unzip "+PATH+sp+'.zip -d '+PATH)






