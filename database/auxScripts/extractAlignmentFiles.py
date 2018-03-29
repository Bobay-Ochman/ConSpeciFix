from config import *
from shutil import copyfile
from multiprocessing import Pool
import os


WEB_OUT = '/Volumes/APE_MacPro_External_2/brian/webDatabaseAlignmentFiles/'

def copySpec(sp):
	copyfile(PATH_TO_OUTPUT+sp+'/concat85.fa', WEB_OUT+sp+'_concat85.fa')

def wrapper(sp):
	try:
		copySpec(sp)
	except Exception as e:
		print e 

if __name__ == '__main__':
	species = getAllSpecies()
	p = Pool(16)
	p.map(wrapper,species)