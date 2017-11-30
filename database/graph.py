from config import *

#chemin = "/Users/louis-mariebobay/Desktop/landscape/"
#chemin = "/work/03239/lbobay/landscape/"

########################################################################
import math

 
def mean( echantillon ) :
    size = len( echantillon )
    moyenne = float(sum( echantillon )) / float(size)
    return moyenne


def stat_variance( echantillon ) :
    n = float(len( echantillon )) # taille
    mq = mean( echantillon )**2
    s = sum( [ x**2 for x in echantillon ] )
    variance = s / n - mq
    return variance


def stat_ecart_type( echantillon ) :
    variance = stat_variance( echantillon )
    ecart_type = math.sqrt( variance )
    return ecart_type

def median( echantillon) :
	echantillon.sort()
	size = len( echantillon )
	if len( echantillon ) % 2 == 0:
		M= float(echantillon[size / 2 - 1] + echantillon[size / 2]) / 2
	else:
		M= echantillon[size / 2]
	return M

def ninetyfive( echantillon) :
	echantillon.sort()
	size = len( echantillon )
	i95 = int( float(size) * 95/100 ) - 1
	return echantillon[i95]


def five( echantillon) :
	echantillon.sort()
	size = len( echantillon )
	i5 = int( float(size) * 5/100 ) - 1
	return echantillon[i5]


########################################################################


species=getSelectedSpecies('rm1.txt')
print len(species)

print 'hello world'

dico={}
liste={}
for sp in species:
	dico[sp]={}
	liste[sp]=[]
	f=open(PATH_TO_OUTPUT + sp + '/rm1.txt',"r")
	lines = f.readlines()
	for l in lines:
		try:
			a=l.strip("\n").split("\t")
			subset = a[0]
			b=subset.split("&&&")
			nb = len(b)
			#if "SAEN3" not in b and "SAEN88" not in b:  ###########################
			if 1==1:
				if nb > 3:
					if float(a[3]) > 0:
						rm = float(a[3])
						if dico[sp].has_key(nb):
							dico[sp][nb].append(rm)
						else:
							dico[sp][nb] = [rm]
							liste[sp].append(nb)
		except:
			print 'passing on a line in '+sp
	f.close()
	print 'doing',sp



for sp in species:
	liste[sp].sort()
	if len(liste[sp]) == 0:
		try:
			os.remove(PATH_TO_OUTPUT + sp + '/graph.txt')
		except:
			continue
		continue
	h=open(PATH_TO_OUTPUT + sp + '/graph.txt',"w")
	print PATH_TO_OUTPUT + sp + '/graph.txt'
	h.seek(0)
	h.write("Nb\tMean\tMedian\tSD\n")
	for nb in liste[sp]:
		h.write(str(nb) + "\t" + str(mean(dico[sp][nb])) + "\t" + str(median(dico[sp][nb])) + "\t"  +  str(stat_ecart_type(dico[sp][nb])) + "\n"  )
	h.truncate()
	h.close()



# Values of clonal species
#0.108065507964
#Low=  0.0199770156685
#High=  0.196154000259









		