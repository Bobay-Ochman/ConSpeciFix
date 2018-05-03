from config import *
from shutil import copyfile
from multiprocessing import Pool
import os


CUR_OUT = '/Volumes/APE_MacPro_External_2/brian/a_website/'
TACC_OUT = '/Users/ochmanlab/Desktop/ConSpeciFix/tacc/a_bigger_website/'



def copySpec(sp):
	print sp
	os.mkdir(TACC_OUT+sp)
	os.system('cp -r ' + CUR_OUT+sp+' '+TACC_OUT)

	# os.system('cp -r ' + PATH_TO_OUTPUT+sp+'/genes '+ WEB_OUT+sp)
	# os.system('cp ' + PATH_TO_OUTPUT+sp+'/concat85.fa '+ WEB_OUT+sp)
	# os.system('cp ' + PATH_TO_OUTPUT+sp+'/RAxML_distances.dist '+ WEB_OUT+sp)
	#os.system('cp ' + PATH_TO_OUTPUT+sp+'/criterion.txt '+ WEB_OUT+sp)
	#os.system('cp ' + PATH_TO_OUTPUT+sp+'/gno2.png '+ WEB_OUT+sp)
	#os.system('cp ' + PATH_TO_OUTPUT+sp+'/rm1.txt '+ WEB_OUT+sp)


def wrapper(sp):
	try:
		copySpec(sp)
	except Exception as e:
		print e 

if __name__ == '__main__':
	curList = os.listdir(TACC_OUT)
	futureList = os.listdir(CUR_OUT)
	todoList = list( set(futureList) - set(curList))
	p = Pool(4)
	p.map(wrapper,todoList)