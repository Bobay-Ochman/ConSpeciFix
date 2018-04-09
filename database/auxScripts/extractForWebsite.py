from config import *
from shutil import copyfile
from multiprocessing import Pool
import os


WEB_OUT = '/Volumes/ITDR/brian/websiteOutput/'

def copySpec(sp):
	os.mkdir(WEB_OUT+sp)
	os.mkdir(WEB_OUT+sp+'/align')
	os.mkdir(WEB_OUT+sp+'/BBH')
	os.mkdir(WEB_OUT+sp+'/genes')
	os.mkdir(WEB_OUT+sp+'/genomes')

	PATH_TO_OUTPUT = '/Volumes/ITDR/brian/a_website/'

	for file in os.listdir(PATH_TO_OUTPUT+sp+'/genes'):
		copyfile(PATH_TO_OUTPUT+sp+'/genes/'+file, WEB_OUT+sp+'/genes/'+file)
		
	copyfile(PATH_TO_OUTPUT+sp+'/orthologs.txt', WEB_OUT+sp+'/orthologs.txt')
	copyfile(PATH_TO_OUTPUT+sp+'/distrib.png', WEB_OUT+sp+'/distrib.png')
	copyfile(PATH_TO_OUTPUT+sp+'/input_'+sp+'.txt', WEB_OUT+sp+'/input_'+sp+'.txt')
	copyfile(PATH_TO_OUTPUT+sp+'/gno1.png', WEB_OUT+sp+'/hmGraph.png')
	copyfile(PATH_TO_OUTPUT+sp+'/tenForUsearch.txt', WEB_OUT+sp+'/tenForUsearch.txt')

	os.chdir(WEB_OUT)
	command = "zip -r "+sp+'.zip '+sp
	os.system(command)
	os.system(' mv '+sp+'.zip ../websiteUploads/'+sp+'.zip')

def wrapper(sp):
	try:
		copySpec(sp)
	except Exception as e:
		print e 

if __name__ == '__main__':
	species = getAllSpecies()
	p = Pool(16)
	p.map(wrapper,species)