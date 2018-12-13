from config import *
import os

# species = getAllSpecies()


# Used to produce a single "combine.png"
# Requires the use of 'convert' tool on command line

# for sp in species:
# 	os.system('convert -verbose -density 150 -trim '+PATH_TO_OUTPUT+sp+'/Distrib.pdf -quality 100 -flatten -sharpen 0x1.0 '+PATH_TO_OUTPUT+sp+'/Distrib.png')
# 	os.system('convert -verbose -density 150 -trim '+PATH_TO_OUTPUT+sp+'/gno1.pdf -quality 100 -flatten -sharpen 0x1.0 '+PATH_TO_OUTPUT+sp+'/gno1.png')
# 	os.system('convert -verbose -density 150 -trim '+PATH_TO_OUTPUT+sp+'/kmeans.pdf -quality 100 -flatten -sharpen 0x1.0 '+PATH_TO_OUTPUT+sp+'/kmeans.png')
# 	os.system('convert '+PATH_TO_OUTPUT+sp+'/distrib.png '+PATH_TO_OUTPUT+sp+'/gno1.png  +append '+PATH_TO_OUTPUT+sp+'/tmp.png')
# 	os.system('convert '+PATH_TO_OUTPUT+sp+'/tmp.png '+PATH_TO_OUTPUT+sp+'/gno2.png  +append '+PATH_TO_OUTPUT+sp+'/tmp2.png')
# 	os.system('convert '+PATH_TO_OUTPUT+sp+'/tmp2.png '+PATH_TO_OUTPUT+sp+'/kmeans.png  +append '+PATH_TO_OUTPUT+sp+'/combine.png')
# 	os.system('rm '+PATH_TO_OUTPUT+sp+'/tmp.png')
# 	os.system('rm '+PATH_TO_OUTPUT+sp+'/tmp2.png')
# 	pass

# print "hello?"
# Used to produce the 4perPage graph images. Highly optional.
# i = 0
# perPage = 4
# species.sort()
# while i < len(species):
# 	command = 'convert '
# 	for z in range(min(perPage,len(species)-i)):
# 		command += PATH_TO_OUTPUT+species[i+z]+'/combine.png '
# 	command+=' -append /Volumes/APE_MacPro_External_2/brian/figures/gno'+str(int(i/perPage)+1)+'.png'
# 	os.system(command)
# 	i +=perPage
