from config import *
from shutil import copyfile
from multiprocessing import Pool
import os


WEB_OUT = '/Volumes/APE_MacPro_External_2/brian/AllStrains/'

def copySpec(sp):
	# os.system('mkdir '+WEB_OUT+sp)
	os.system('cp -r ' + PATH_TO_OUTPUT+sp+'/genes '+ WEB_OUT+sp+'/genes ')

def wrapper(sp):
	try:
		copySpec(sp)
	except Exception as e:
		print e 

if __name__ == '__main__':
	species = getAllSpecies()
	p = Pool(4)
	p.map(wrapper,species)