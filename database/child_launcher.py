import os

print "hello from launcher"
print os.getcwd()
print os.listdir(os.getcwd())

os.system('python child_runner.py')