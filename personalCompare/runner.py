from config import *
import os
import sys
import time

print " "
print " --- conspecifix ---"
print " "
print "Expecting folder of .fa files at:"
print PATH_TO_FOLDER
print " "
print "Path to log files at:"
print PATH_TO_LOGS
print " "
print "Origionals will be moved to:"
print PATH_TO_MAT+'orig/' 
print " "
print "Now beginning analysis steps:"
print "  (See progress in log files)"



try:
	os.system('mkdir '+PATH_TO_MAT)
	os.system('mkdir '+PATH_TO_LOGS)
	os.system('mkdir '+PATH_TO_TODO)
	os.system('mkdir '+PATH_TO_MAT+'align/')
	os.system('mkdir '+PATH_TO_MAT+'BBH/')
	os.system('mkdir '+PATH_TO_MAT+'results/')
	os.system('mkdir '+PATH_TO_MAT+'orig/')
except OSError as e:
	print e

ARGS = ' ' + PATH_TO_FOLDER + ' ' + PIPE_CHAR + PATH_TO_LOGS

print "Cleaning"
os.system('python clean_files.py'+ARGS+'01_cleaning.txt')

print "Usearch"
os.system('python usearch_build.py'+ ARGS+'06_u_build.txt')
os.system('python usearch_multi.py'+ ARGS+'07_u_multi.txt')

print "Parsing Usearch"
os.system('python parse_multiple_usearch.py'+ ARGS+'08_u_parse.txt')

print "MCL"
os.system('python launch_mcl.py'+ ARGS+'09_mcl.txt')

print "Getting Core Genome"
os.system('python get_core.py'+ ARGS+'10_get_core.txt')

print "Mafft"
os.system('python launch_mafft_build.py'+ ARGS+'11_mafft_build.txt')
os.system('python launch_mafft_multi.py '+PATH_TO_FOLDER)


print "Making a single Concat file"
os.system('python concat85.py'+ ARGS+'13_concat85.txt')

print "RAxML"
os.system('python raxml_distance.py'+ ARGS+'14_raxml.txt')

print "Sampling"
os.system('python sample.py' + ARGS+'15_sample.txt')

print "Calculating HM Ratio"
os.system('python calcHM_build.py' + ARGS+'16_calcHM_build.txt')
os.system('python calcHM_multi.py' + ARGS+'17_calcHM_multi.txt')

print "Making Graphs"
os.system('python graph.py' + ARGS+'18_graph.txt')
os.system('python big_graph.py'+ ARGS+'19_graph_big.txt')
os.system('Rscript '+ PATH_TO_MAT+'graph.R'+ ARGS+'20_graph_r.txt')

print "Launching "
os.system('python distrib.py '+ ARGS+'21_distrib.txt')
os.system('python kmean.py '+ ARGS+'22_kmean.txt')
os.system("Rscript " +PATH_TO_MAT + "kmean.R")

os.system('python split_kmean.py '+ ARGS+'23_split_kmean.txt')
os.system('python criterion.py '+ ARGS+'24_criterion.txt')









