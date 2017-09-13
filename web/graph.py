from config import *


species=getSingleSpecies()

print 'hello world'

dico={}
liste={}
for sp in species:
	dico[sp]={}
	liste[sp]=[]
	try:
		f=open(PATH_TO_UPLOAD+ 'rm1.txt',"r")
		lines = f.readlines()
		if len(lines) < 100:
			continue
		for l in lines:
			a=l.strip("\n").split("\t")
			subset = a[0]
			b=subset.split("&&&")
			nb = len(b)
			#if "SAEN3" not in b and "SAEN88" not in b:  ###########################
			if nb > 3:
				rm = float(a[3])
				if dico[sp].has_key(nb):
					dico[sp][nb].append(rm)
				else:
					dico[sp][nb] = [rm]
					liste[sp].append(nb)
		f.close()
		print 'doing',sp
		print dico
	except:
		pass



for sp in species:
	liste[sp].sort()
	if len(liste[sp]) == 0:
		try:
			os.remove(PATH_TO_UPLOAD + 'graph.txt')
		except:
			continue
		continue
	h=open(PATH_TO_UPLOAD+ 'graph.txt',"w")
	h.seek(0)
	h.write("Nb\tMean\tMedian\tSD\n")
	for nb in liste[sp]:
		h.write(str(nb) + "\t" + str(mean(dico[sp][nb])) + "\t" + str(median(dico[sp][nb])) + "\t"  +  str(stat_ecart_type(dico[sp][nb])) + "\n"  )
	h.truncate()
	h.close()











		