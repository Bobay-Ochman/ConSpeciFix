from config import *
import os

for sp in getAllSpecies():
	os.system("rm "+PATH_TO_OUTPUT+sp+'/kmeans.txt')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/key.txt')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/graph.txt')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/distrib.txt')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/for_removal.txt')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/vector.txt')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/criterion.txt')


	os.system("rm "+PATH_TO_OUTPUT+sp+'/distrib.png')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/gno1.png')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/gno2.png')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/kmeans.png')


	os.system("rm "+PATH_TO_OUTPUT+sp+'/combine.png')


	os.system("rm "+PATH_TO_OUTPUT+sp+'/make_distrib_graph.R')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/make_hm_graph.R')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/make_kmean_graph.R')
	os.system("rm "+PATH_TO_OUTPUT+sp+'/make_hm_graph_points.R')	