import os

print "hello from launcher"
print os.getcwd()
print os.listdir(os.getcwd())

from config import *
try:
	print PATH_TO_OUTPUT
except:
	print 'whelp this will be not fun'

os.system('python child_runner.py')