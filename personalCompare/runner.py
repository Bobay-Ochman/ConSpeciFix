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
print "Now beginning analysis steps:"
print "  (See progress in log files)"
print "  (log files span 06_ to 24_)"


try:
	os.system('mkdir '+PATH_TO_MAT)
	os.system('mkdir '+PATH_TO_LOGS)
	os.system('mkdir '+PATH_TO_TODO)
	os.system('mkdir '+PATH_TO_MAT+'align/')
	os.system('mkdir '+PATH_TO_MAT+'BBH/')
	os.system('mkdir '+PATH_TO_MAT+'results/')
except OSError as e:
	print e


print "Usearch"
os.system('python usearch_build.py'+ PIPE_CHAR+PATH_TO_LOGS+'06_u_build.txt')
os.system('python usearch_multi.py'+ PIPE_CHAR+PATH_TO_LOGS+'07_u_multi.txt')

print "Parsing Usearch"
os.system('python parse_multiple_usearch.py'+ PIPE_CHAR+PATH_TO_LOGS+'08_u_parse.txt')

print "MCL"
os.system('python launch_mcl.py'+ PIPE_CHAR+PATH_TO_LOGS+'09_mcl.txt')

print "Getting Core Genome"
os.system('python get_core.py'+ PIPE_CHAR+PATH_TO_LOGS+'10_get_core.txt')

print "Mafft"
os.system('python launch_mafft_build.py'+ PIPE_CHAR+PATH_TO_LOGS+'11_mafft_build.txt')
os.system('python launch_mafft_multi.py'+ PIPE_CHAR+PATH_TO_LOGS+'12_mafft_multi.txt')


print "Making a single Concat file"
os.system('python concat85.py'+ PIPE_CHAR+PATH_TO_LOGS+'13_concat85.txt')

print "RAxML"
os.system('python raxml_distance.py'+ PIPE_CHAR+PATH_TO_LOGS+'14_raxml.txt')

print "Sampling"
os.system('python sample.py' + PIPE_CHAR+PATH_TO_LOGS+'15_sample.txt')

print "Calculating HM Ratio"
os.system('python calcHM_build.py' + PIPE_CHAR+PATH_TO_LOGS+'16_calcHM_build.txt')
os.system('python calcHM_multi.py' + PIPE_CHAR+PATH_TO_LOGS+'17_calcHM_multi.txt')

print "Making Graphs"
os.system('python graph.py' + PIPE_CHAR+PATH_TO_LOGS+'18_graph.txt')
os.system('python big_graph.py'+ PIPE_CHAR+PATH_TO_LOGS+'19_graph_big.txt')
os.system('Rscript '+ PATH_TO_MAT+'graph.R'+ PIPE_CHAR+PATH_TO_LOGS+'20_graph_r.txt')

print "Launching "
os.system('python distrib.py '+ PIPE_CHAR+PATH_TO_LOGS+'21_distrib.txt')
os.system('python kmean.py '+ PIPE_CHAR+PATH_TO_LOGS+'22_kmean.txt')
os.system("Rscript " +PATH_TO_MAT + "kmean.R")

os.system('python split_kmean.py '+ PIPE_CHAR+PATH_TO_LOGS+'23_split_kmean.txt')
os.system('python criterion.py '+ PIPE_CHAR+PATH_TO_LOGS+'24_criterion.txt')









