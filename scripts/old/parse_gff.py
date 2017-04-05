import os
from config import *

def rev_comp( seq ):
	new_seq=""
	SEQ = seq[::-1]
	SEQ = SEQ.upper()
	for B in SEQ:
		if B == "G":
			new_seq+="C"
		elif B == "C":
			new_seq+="G"
		elif B == "A":
			new_seq+="T"
		elif B == "T":
			new_seq+= "A"
		elif B == "R":
			new_seq+="Y"
		elif B == "S" or B == "W" or B == "N":
			new_seq += B
		elif B == "Y":
			new_seq+="R"
		elif B == "K":
			new_seq += "M"
		elif B == "M":
			new_seq+="K"
		elif B == "B":
			new_seq+="V"
		elif B == "V":
			new_seq += "B"
		elif B == "D":
			new_seq+="H"
		elif B =="H":
			new_seq+="D"
		else:
			print "!!! ",B
	return new_seq




species = getSpecies()
print species



robert={}
f=open("../genomes_proks.txt","r")
for l in f:
	if l[0] != "#":
		a=l.strip("\n").strip("\r").split("\t")
		b = a[0].split(" ")
		if len(b) > 1 and b[1] != "sp.":
			sp = b[0] + "_" + b[1]
		if sp in species:
			if robert.has_key(sp):
				pass
			else:
				robert[sp]={}
			tmp=[]
			for stuff in a:
				if 'ftp://' in stuff:
					tmp.append(stuff)
			if len(tmp) == 2:
				GCF = tmp[0].split('/')[-1]  
				GCA = tmp[1].split('/')[-1] 
				robert[sp][GCF + '_genomic.fa'] = GCA + '_genomic.fa'

f.close()

PATH_TO_OUTPUT = '/Volumes/ITDR/brian/results/'





liste={}
for sp in species:
	tmp= os.listdir(PATH_TO_OUTPUT + sp + '/genomes/')
	liste[sp]=[]
	nb=0
	for truc in tmp:
		if truc.endswith('.gff'):
			nb+=1
			if nb >= 0: # and nb <= 5000:
				liste[sp].append(truc)
	print sp,' : ',nb,' genomes total'


dico={}
for sp in species:
	print 'Load GFF ',sp
	dico[sp]={}
	for file in liste[sp]:
		dico[sp][file.rstrip(".gff")] = []
		f=open(PATH_TO_OUTPUT + sp + "/genomes/" + file,"r")
		for l in f:
			if l[0] != "#":	#if not the header
				a=l.strip("\n").split("\t")
				if a[2] ==  "CDS":
					resu = [a[0],a[3],a[4],a[6]]
					dico[sp][file.rstrip(".gff")].append(resu)
		f.close()


#print dico[sp][file.rstrip(".gff")][:3]

print 'LOAD sequences'

tmp={}
for SP in species:
	print 'Load ', SP
	tmp[SP]={}
	for file in liste[SP]:
		sp = file.rstrip(".gff")
		#print sp
		tmp[SP][sp] = {}
		f=open(PATH_TO_OUTPUT + SP + "/genomes/" + sp + ".fna","r")
		for l in f:
			if l[0] == ">":
				a=l.strip(">").strip("\n").split(" ")
				contig =  a[0]
				tmp[SP][sp][contig] = []
			else:
				tmp[SP][sp][contig].append(l.strip("\n"))
		f.close()


seq={}
for SP in species:
	seq[SP]={}
	for sp in tmp[SP]:
		seq[SP][sp]={}
		for contig in tmp[SP][sp]:
			seq[SP][sp][contig] = "".join(tmp[SP][sp][contig])


tmp=''




for SP in species:
	NB=0
	for sp in dico[SP]:
		NB+=1
		if len(dico[SP][sp]) > 4:
			print 'Write ', SP,' ',NB
			h=open(PATH_TO_OUTPUT + SP + "/genes/" + sp + ".fa" , "w")
			#g=open('../' + SP + "/genes/" + sp + ".prot" , "w")
			for resu in dico[SP][sp]:
				contig = resu[0]
				deb,fin = int(resu[1]),int(resu[2])
				sens=resu[3]
				if deb > fin:
					print "problem ",sp," ",resu
				if sens== "+":
					gene = seq[SP][sp][contig][deb-1 : fin]
				else:
					gene = rev_comp(seq[SP][sp][contig][deb-1 : fin])
				h.write(">" + contig + "_" + str(deb) + "_" + str(fin) + " " + sens + "\n" + gene + "\n")
				#prot = translate(gene)
				#if len(gene) - 3 == len(prot) * 3:
					#g.write(">" + contig + "_" + str(deb) + "_" + str(fin) + " " + sens + "\n" + prot + "\n")
				#else:
					#print len(gene) - 3," ",len(prot) * 3
			f.close()
			h.close()
			#g.close()
			gcf = sp + ".fa"
			#if robert[SP].has_key(gcf):
				#print 'Erase ', gcf
				#os.system('rm ' + PATH_TO_OUTPUT + SP + '/genes/' + robert[SP][gcf])
		else:
			print SP,' ',sp,' ',NB,' empty'
















