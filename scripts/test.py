from config import *
import os


spec = getSelectedSpecies("criterion.txt")
for sp in spec:
	print "mv "+ sp +" ../completeWithCriterion/"+sp