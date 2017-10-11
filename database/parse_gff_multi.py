from multiprocessing import Pool
import multiprocessing
import os
import time
from config import *

def processSpec(args):
	sp = args.split('\t')[0]
	file= args.split('\t')[1].strip('\n')
	
	dico = {}
	dico[file] = []
	f = None
	try:
		f=open(PATH_TO_OUTPUT + sp + "/genomes/" + file +'.gff',"r")
	except:
		print PATH_TO_OUTPUT + sp + "/genomes/" + file +'.gff'
		print 'file error'
		return
	
	for l in f:
		if l[0] != "#":	#if not the header
			a=l.strip("\n").split("\t")
			if a[2] ==  "CDS":
				resu = [a[0],a[3],a[4],a[6]]
				dico[file].append(resu)
	f.close()

	
	tmp={}
	
	try:		
		spec = file
		#print spec
		tmp[spec] = {}
		f=open(PATH_TO_OUTPUT + sp + "/genomes/" + spec + ".fna","r")
		for l in f:
			if l[0] == ">":
				a=l.strip(">").strip("\n").split(" ")
				contig =  a[0]
				tmp[spec][contig] = []
			else:
				tmp[spec][contig].append(l.strip("\n"))
		f.close()
	except:
		pass

	seq={}
	for spec in tmp:
		seq[spec]={}
		for contig in tmp[spec]:
			seq[spec][contig] = "".join(tmp[spec][contig])
			
	NB=0
	for spec in dico:
		NB+=1
		if len(dico[spec]) > 4:
			try:
				h=open(PATH_TO_OUTPUT + sp + "/genes/" + spec + ".fa" , "w")
				#g=open('../' + sp + "/genes/" + spec + ".prot" , "w")
				for resu in dico[spec]:
					contig = resu[0]
					deb,fin = int(resu[1]),int(resu[2])
					sens=resu[3]
					if deb > fin:
						print "problem ",spec," ",resu
					if sens== "+":
						gene = seq[spec][contig][deb-1 : fin]
					else:
						gene = rev_comp(seq[spec][contig][deb-1 : fin])
					h.write(">" + contig + "_" + str(deb) + "_" + str(fin) + " " + sens + "\n" + gene + "\n")
					#prot = translate(gene)
					#if len(gene) - 3 == len(prot) * 3:
						#g.write(">" + contig + "_" + str(deb) + "_" + str(fin) + " " + sens + "\n" + prot + "\n")
					#else:
						#print len(gene) - 3," ",len(prot) * 3
				f.close()
				h.close()
				#g.close()
				gcf = spec + ".fa"
				#if robert[sp].has_key(gcf):
					#print 'Erase ', gcf
					#os.system('rm ' + PATH_TO_OUTPUT + sp + '/genes/' + robert[sp][gcf])
			except:
				pass

		else:
			print sp,' ',spec,' ',NB,' empty'




"""
f = open('todo/parse_gff.txt','r')
args = []
for l in f.readlines():
	args.append(l)

for sp in args:
	processSpec(sp)

"""

if __name__ == '__main__':
	species = getSpecies()
	p = Pool(MAX_THREADS)
	f = open('todo/parse_gff.txt','r')
	args = []
	for l in f:
		args.append(l)
	print "going!"
	p.map(processSpec,args)

#"""
