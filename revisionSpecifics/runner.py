from config import *
import os
import sys
import time

runId = str(time.time())

print " "
print "runId:" + runId
print "path of log files:"
print PATH_TO_OUTPUT+'out_'+runId
print " "

try:
	os.system('mkdir '+PATH_TO_OUTPUT+'out_coreGenome_'+runId) #to make our log file folder
	pass
except OSError as e:
	print e
"""
print "Making folders"
os.system('python folders.py'+ ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/13_concat85.txt')

print "Making concat files"
os.system('python concat85.py'+ ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/13_concat85.txt')

print "RAxML"
os.system('python raxml_distance.py'+ ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/14_raxml.txt')
"""
print "combine all RAxML values"
os.system('python combine_RAxML.py' + ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/14.5_combine_RAxML.txt')

print "prune sample.txt"
os.system('python prune.py'+ ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/15_prune.txt')

print "Calculating HM Ratio"
os.system('python calcHM_build.py' + ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/16_calcHM_build.txt')
os.system('python calcHM_multi.py' + ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/17_calcHM_multi.txt')


os.system('python gatherHM.py' + ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/18_gatherHM.txt')

print "Making new Graphs with boxplot"
os.system('python make_graphs.py' + ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/19_make_graphs.txt')
os.system('python make_point_graphs.py' + ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/20_make_point_graphs.txt')

print "New composite figures"
os.system('python assembleImages.py' + ' &> '+PATH_TO_OUTPUT+'out_coreGenome_'+runId+'/21_assembleImages.txt')


# at this point, you can start the full analysis over again from "CalcHM" values in the standard database builder
# It will pull from the new RAxML Values (the medians) taken from combine_RAxML
