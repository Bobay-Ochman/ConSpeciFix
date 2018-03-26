from multiprocessing import Pool
import multiprocessing
import os
import time
from config import *

makeSureToDo = ['Escherichia_coli']#['Aeromonas_caviae','Alteromonas_macleodii','Bacteroides_thetaiotaomicron']

#robert={}
#f=open("../genomes_proks.txt","r")
#for l in f:
#	if l[0] != "#":
#		a=l.strip("\n").strip("\r").split("\t")
#		b = a[0].split(" ")
#		if len(b) > 1 and b[1] != "sp.":
#			sp = b[0] + "_" + b[1]
#		if sp in species:
#			if robert.has_key(sp):
#				pass
#			else:
#				robert[sp]={}
#			tmp=[]
#			for stuff in a:
#				if 'ftp://' in stuff:
#					tmp.append(stuff)
#			if len(tmp) == 2:
#				GCF = tmp[0].split('/')[-1]  
#				GCA = tmp[1].split('/')[-1] 
#				robert[sp][GCF + '_genomic.fa'] = GCA + '_genomic.fa'
#
#f.close()

def processSpec(sp):
	liste=[]
	dico=[]
	
	#see if we already visited and did the work
	try:
		open(PATH_TO_OUTPUT + sp + "/complete.txt", 'r')
		
		listOfFiles = os.listdir(PATH_TO_OUTPUT + sp + '/genomes')

		if(sp not in makeSureToDo and len(listOfFiles)> 4 ):
			print 'skipping ' + sp
			return
	except:
		pass

	tmp= os.listdir(PATH_TO_OUTPUT + sp + '/genomes/')

	nb=0
	for truc in tmp:
		if truc.endswith('.gff'):
			nb+=1
			if nb >= 0: # and nb <= 5000:
				liste.append(truc)
	print sp,' : ',nb,' genomes total'


	print 'Load GFF ',sp
	dico={}
	for file in liste:
		print file
		dico[file.rstrip(".gff")] = []
		f=open(PATH_TO_OUTPUT + sp + "/genomes/" + file,"r")
		for l in f:
			if l[0] != "#":	#if not the header
				a=l.strip("\n").split("\t")
				if a[2] ==  "CDS":
					resu = [a[0],a[3],a[4],a[6]]
					dico[file.rstrip(".gff")].append(resu)
		f.close()

	
	print 'Load ', sp
	tmp={}
	for file in liste:
		print file
		try:		
			spec = file.rstrip(".gff")
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
				print 'Write ', sp,' ',NB
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
	done=open(PATH_TO_OUTPUT + sp + "/complete.txt" , "a")
	done.write('gff parsed on '+ str(time.time()) + ' with ' + str(len(dico[sp])) + '\n' )
	done.close()

if __name__ == '__main__':
	species = getSpecies()
	processSpec('Escherichia_coli')
	#print multiprocessing.cpu_count()
	#p = Pool(multiprocessing.cpu_count())
	#print processSpec
	#print species
	#p.map(processSpec,species)
	