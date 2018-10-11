import os

print "hello from launcher"
print os.getcwd()
files = os.listdir(os.getcwd())
print files
if 'config.pyc' in files:
	os.remove('config.pyc')

try:
	from config import *
	print PATH_TO_OUTPUT
except:
	print 'whelp this will be not fun'

os.system('python child_runner.py')