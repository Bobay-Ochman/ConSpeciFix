from shutil import copyfile
from multiprocessing import Pool
import os
from config import *



print len(getAllSpecies())

for sp in getAllSpecies():
	print "<option value=\""+sp+"\">"+sp.replace('_',' ')+'</option>'