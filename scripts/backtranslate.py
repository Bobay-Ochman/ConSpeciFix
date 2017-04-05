import os

species=[]
f=open('../selected_species.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	species.append(a[0])

f.close()

strains={}
for sp in species:
	strains[sp]=[]
	f=open('../results/' + sp + '/new_strains.txt' , 'r')
	for l in f:
		strains[sp].append(l.strip('\n'))
	f.close()


liste={}
for sp in species:
	liste[sp]=[]
	for st in strains[sp]:
		truc = st + '.prot'
		liste[sp].append(truc)



print 'Load IDs'

parent={}
seq={}
for sp in species:
	parent[sp]={}
	for st in strains[sp]:
		truc = st + '.fa'
		f=open('../genomes/' + sp + '/' + truc ,'r')
		for l in f:
			if l[0] == '>':
				id = l.strip('>').split(' ')[0]
				parent[sp][id]=st
		f.close()





print 'Load proteins'

shortcut={}
robert={}
corres={}
for sp in species:
	corres[sp],robert[sp]={},{}
	fichiers = os.listdir('../results/' + sp +  '/align/' )
	for truc in fichiers:
		if truc.endswith('.prot.align'):
			ortho = truc.split('.prot')[0]
			robert[sp][ortho]={}
			corres[sp][ortho]={}
			f=open('../results/' + sp +  '/align/' + truc ,'r')
			for l in f:
				if l[0] == '>':
					id=l.strip('\n').lstrip('>')
					robert[sp][ortho][id]=''
					shortcut[id] = 'y'
					corres[sp][ortho][id]=id
				else:
					robert[sp][ortho][id]+=l.strip('\n')
			f.close()



print 'Load nucleotides'


tmp={}
for sp in species:
	fichiers = os.listdir('../genomes/' + sp + '/')
	for truc in fichiers:
		if truc.endswith('.fa'):
			f=open('../genomes/' + sp + '/' + truc ,"r")
			for l in f:
				if l[0]==">":
					id = l.strip("\n").strip(">").split(' ')[0]
					tmp[id] = []
				elif shortcut.has_key(id):
					tmp[id].append( l.strip("\n"))
			f.close()


seq={}
for id in tmp:
	seq[id] = ''.join(tmp[id])


tmp=[]

print 'Back translate'




back={}
for sp in species:
	back[sp]={}
	for ortho in robert[sp]:
		#print 'Back translate ',sp,' ',ortho
		back[sp][ortho]={}
		if 1==1	:
			tag=0
			for id in robert[sp][ortho]:
				back[sp][ortho][id] = ""
				tag+=1
				resu = ""
				align = robert[sp][ortho][id]
				ID = corres[sp][ortho][id]
				i,j=0,0
				while i < len(align):
					aa = align[i]
					if aa == "-":
						resu += "---"
					else:
						codon = seq[ID][j:j+3]
						resu += codon
						j+=3
					if len(resu) == 60:
						back[sp][ortho][id] += resu
						resu=""
					i+=1
				if len(resu) >= 1:
					back[sp][ortho][id] += resu



for sp in species:
	print sp, ' ',back[sp].keys()



print "Write fasta"


for sp in species:
	print "write", sp
	for ortho in back[sp]:
		h=open('../results/' + sp + '/align/' +  ortho + ".fa","w")
		for id in back[sp][ortho]:
			if 1==1:
				h.write(">" + id + "\n")
				i=0
				while i < len(back[sp][ortho][id]):
					h.write(back[sp][ortho][id][i:i+60] + "\n")
					i+=60
		h.close()



















