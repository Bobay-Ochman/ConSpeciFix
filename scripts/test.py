from config import *
import os

species = giveMulti(getSelectedSpecies())
g = getGenomes(species)
for sp in g:
	print sp, len(g[sp])