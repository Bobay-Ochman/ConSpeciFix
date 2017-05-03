
import os
import math
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


########################################################################



species=[]
f=open('../results/species.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	species.append(a[0])

f.close()



print species


for sp in species:
	k=open('../results/distrib/distrib_' + sp + '.txt','w')
	dico={}
	print sp
	f=open('../' + sp + '/rm1.txt','r')
	for l in f:
		a=l.strip('\n').split('\t')
		strains = a[0].split('-')
		nb=len(strains)
		r,m=float(a[1]),float(a[2])
		if m > 0:
			rm = r/m
			if nb >= 10:
				k.write(a[0] + '\t' + str(rm) + '\n')
	f.close()
	k.close()

































