from config import *
import os

specFolders = ''

for sp in ['Buchnera_aphidicola', 'Mycoplasma_bovis', 'Lactobacillus_fermentum', 'Propionibacterium_freudenreichii', 'Clostridium_beijerinckii', 'Mycobacterium_africanum', 'Mycobacterium_fortuitum']:
	specFolders += ' ' + sp
os.chdir(PATH_TO_OUTPUT)
os.system('tar -c -f export.zip '+specFolders)

print 'selected folders compressed into export.zip!'