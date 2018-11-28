from config import *
import os
import sys
import time

runId = str(time.time())
PATH_TO_LOGS =PATH_TO_OUTPUT+'out_'+runId+'/'





print " "
print " ---ConSpeciFix---"
print " "
print "Expecting species.txt to already be in place"
print " "
print "runId:" + runId
print "path of log files:"
print PATH_TO_LOGS
print " "

try:
	os.system('mkdir '+PATH_TO_LOGS) #to make our log file folder
	pass
except OSError as e:
	print e

print "Making folders"
os.system('python folders.py'+ PIPE_CHAR+PATH_TO_LOGS+'00_folders.txt')

print "Downloading Genomes"
os.system('python download_build.py'+ PIPE_CHAR+PATH_TO_LOGS+'01_download_build.txt')
os.system('python download_multi.py'+ PIPE_CHAR+PATH_TO_LOGS+'02_download_multi.txt')

print "Unziping Genomes"
os.system('python unzip.py'+ PIPE_CHAR+PATH_TO_LOGS+'03_unzip.txt')

print "Parsing GFF"
os.system('python parse_gff_build.py'+ PIPE_CHAR+PATH_TO_LOGS+'04_parse_gff_build.txt')
os.system('python parse_gff_multi.py'+ PIPE_CHAR+PATH_TO_LOGS+'05_parse_gff_multi.txt')

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
os.system('python launch_mafft_multi.py')

print "Making a single Concat file"
os.system('python concat85.py'+ PIPE_CHAR+PATH_TO_LOGS+'13_concat85.txt')

print "RAxML"
os.system('python raxml_distance.py'+ PIPE_CHAR+PATH_TO_LOGS+'14_raxml.txt')

print "Sampling"
os.system('python sample.py' + PIPE_CHAR+PATH_TO_LOGS+'15_sample.txt')

print "Calculating HM Ratio"
os.system('python calcHM_build.py' + PIPE_CHAR+PATH_TO_LOGS+'16_calcHM_build.txt')
os.system('python calcHM_multi.py' + PIPE_CHAR+PATH_TO_LOGS+'17_calcHM_multi.txt')

print "Making HM Graph"
os.system('python graph.py' + PIPE_CHAR+PATH_TO_LOGS+'18_graph.txt')
os.system('python make_hm_graph.py'+ PIPE_CHAR+PATH_TO_LOGS+'19_make_hm_graphs.txt')

print "Making Distrib Graphs"
os.system('python distrib.py '+ PIPE_CHAR+PATH_TO_LOGS+'20_distrib.txt')
os.system('python make_distrib_graph.py '+ PIPE_CHAR+PATH_TO_LOGS+'21_make_distrib_graph.txt')

print "Making KMeans Graphs"
os.system('python split_kmean.py '+ PIPE_CHAR+PATH_TO_LOGS+'22_split_kmean.txt')
os.system('python make_kmeans_graph.py '+ PIPE_CHAR+PATH_TO_LOGS+'23_make_kmeans_graph.txt')

print "Criterion..."
os.system('python criterion.py '+ PIPE_CHAR+PATH_TO_LOGS+'24_criterion.txt')

print "Making Point Graph"
os.system('python graph_point.py '+ PIPE_CHAR+PATH_TO_LOGS+'25_graph_point.txt')
os.system('python make_hm_graph_point.py '+ PIPE_CHAR+PATH_TO_LOGS+'26_make_hm_graph_point.txt')

print "Combine the images"
os.system('python assembleImages.py '+ PIPE_CHAR+PATH_TO_LOGS+'27_assembleImages.txt')

print "Making Map of Genome"
os.system('python visualize.py '+ PIPE_CHAR+PATH_TO_LOGS+'28_map_genome.txt')

print "Completed\n..."
print "Results in:\n"+PATH_TO_OUTPUT+'\n'







