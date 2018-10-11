import os
import sys

print "hello from launcher"
print os.getcwd()
files = os.listdir(os.getcwd())
print files
if 'config.pyc' in files:
	os.remove('config.pyc')

try:
	from config import *
	print PATH_TO_OUTPUT
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)


os.system('python child_runner.py')