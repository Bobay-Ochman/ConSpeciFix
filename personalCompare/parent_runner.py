import os

path = '/stor/work/Ochman/brian/viral'

for f in os.listdir(path):
	try:
		os.system('python runner.py '+path+'/'+f)
	except:
		print 'error! '+str(f)
