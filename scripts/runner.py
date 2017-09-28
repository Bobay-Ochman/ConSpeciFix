from config import *
import os
import sys
import time

runId = str(time.time())

print "Expecting species.txt to already be in place"
print " "
print "runId:" + runId
print "path of log files:"
print PATH_TO_OUTPUT+'_log.'+runId
print " "

try:
	os.system('mkdir '+PATH_TO_OUTPUT+'_log.'+runId) #to make our log file folder
except OSError as e:
	print e

print "making folders"
os.system('python folders.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/00_folders.txt')

print "Downloading Genomes"
os.system('python download_build.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/01_download_build.txt')
os.system('python download_multi.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/02_download_multi.txt')

print "Unziping Genomes"
os.system('python unzip.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/03_unzip.txt')

print "Parsing GFF"
os.system('python parse_gff_build.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/04_parse_gff_build.txt')
os.system('python parse_gff_multi.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/05_parse_gff_multi.txt')

print "Usearch"
os.system('python usearch_build.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/06_u_build.txt')
os.system('python usearch_multi.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/07_u_multi.txt')

print "Parsing Usearch"
os.system('python parse_multiple_usearch.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/08_u_parse.txt')

print "MCL"
os.system('python launch_mcl.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/09_mcl.txt')

print "Getting Core Genome"
os.system('python get_core.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/10_get_core.txt')

print "Mafft"
os.system('python launch_mafft_build.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/11_mafft_build.txt')
os.system('python launch_mafft_multi.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/12_mafft_multi.txt')

print "Making a single Concat file"
os.system('python concat85.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/13_concat85.txt')

print "RAxML"
os.system('python raxml_distance.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/14_raxml.txt')

print "Sampling"
os.system('python sample.py' + ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/15_sample.txt')

print "Calculating HM Ratio"
os.system('python calcHM_build.py' + ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/16_calcHM_build.txt')
os.system('python calcHM_multi.py' + ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/17_calcHM_multi.txt')

print "Making Graphs"
os.system('python graph.py' + ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/18_graph.txt')
os.system('python big_graph.py'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/19_graph_big.txt')
os.system('Rscript '+ PATH_TO_OUTPUT + 'graph.R'+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/20_graph_r.txt')

print "Launching "
os.system('python distrib.py '+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/21_distrib.txt')
os.system('python kmean.py '+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/22_kmean.txt')
os.system('python split_kmean.py '+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/23_split_kmean.txt')
os.system('python criterion.py '+ ' &> '+PATH_TO_OUTPUT+'_log.'+runId+'/24_criterion.txt')










