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

print 'hello world, graphing'

dico={}
liste=[]
try:
	f=open(PATH_TO_MAT + 'rm1.txt',"r")
	lines = f.readlines()
	for l in lines:
		a=l.strip("\n").split("\t")
		subset = a[0]
		b=subset.split("&&&")
		nb = len(b)
		#if "SAEN3" not in b and "SAEN88" not in b:  ###########################
		if 1==1:
			if nb > 3:
				if float(a[3]) > 0:
					rm = float(a[3])
					if dico.has_key(nb):
						dico[nb].append(rm)
					else:
						dico[nb] = [rm]
						liste.append(nb)
	f.close()
	print 'going!'
except Exception as e:
	print 'passing!!!' , e


liste.sort()
try:
	os.remove(PATH_TO_MAT + 'graph.txt')
except:
	pass
h=open(PATH_TO_MAT + 'graph.txt',"w")
print PATH_TO_MAT + 'graph.txt'
h.seek(0)
h.write("Nb\tMean\tMedian\tSD\n")
for nb in liste:
	h.write(str(nb) + "\t" + str(mean(dico[nb])) + "\t" + str(median(dico[nb])) + "\t"  +  str(stat_ecart_type(dico[nb])) + "\n"  )
h.truncate()
h.close()











		