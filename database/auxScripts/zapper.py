import multiprocessing
from multiprocessing import Pool
import os

def wrapper(f):
	os.system('python runner_personal.py -t 12 '+mydir+f)

if __name__ == '__main__':
	os.chdir('/stor/work/Ochman/brian/ConSpeciFix/database/')
	mydir = '/stor/work/Ochman/brian/dengueMix/'
	print multiprocessing.cpu_count()
	p = Pool(5)
	args = os.listdir(mydir)
	p.map(wrapper,args)