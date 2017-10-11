import os


def translate(seq):
	d={}
	d["TTT"],d["TTC"],d["TTA"],d["TTG"]="F","F","L","L"
	d["CTT"],d["CTC"],d["CTA"],d["CTG"]="L","L","L","L"
	d["ATT"],d["ATC"],d["ATA"],d["ATG"]="I","I","I","M"
	d["GTT"],d["GTC"],d["GTA"],d["GTG"]="V","V","V","V"
	d["TCT"],d["TCC"],d["TCA"],d["TCG"]="S","S","S","S"
	d["CCT"],d["CCC"],d["CCA"],d["CCG"]="P","P","P","P"
	d["ACT"],d["ACC"],d["ACA"],d["ACG"]="T","T","T","T"
	d["GCT"],d["GCC"],d["GCA"],d["GCG"]="A","A","A","A"
	d["TAT"],d["TAC"],d["TAA"],d["TAG"]="Y","Y","*","*"
	d["CAT"],d["CAC"],d["CAA"],d["CAG"]="H","H","Q","Q"
	d["AAT"],d["AAC"],d["AAA"],d["AAG"]="N","N","K","K"
	d["GAT"],d["GAC"],d["GAA"],d["GAG"]="D","D","E","E"
	d["TGT"],d["TGC"],d["TGA"],d["TGG"]="C","C","*","W"
	d["CGT"],d["CGC"],d["CGA"],d["CGG"]="R","R","R","R"
	d["AGT"],d["AGC"],d["AGA"],d["AGG"]="S","S","R","R"
	d["GGT"],d["GGC"],d["GGA"],d["GGG"]="G","G","G","G"
	i=0
	tmp=[]
	while i in range(len(seq)-3):
		codon= seq[i:i+3]
		if codon not in d.keys():
			tmp.append("X")
		else:
			tmp.append(d[codon])
			if d[codon]=="*":
				break
		i += 3
	prot="".join(tmp)
	return	prot




species=[]
f=open('../taxonomy.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	species.append(a[0])

f.close()



print 'Load sequences'
genes={}
genomes={}
seq={}
for sp in species:
	print sp
	genes[sp]={}
	genomes[sp]=[]
	seq[sp]={}
	f=open('../data/' + sp + '.fa','r')
	for l in f:
		if l[0] == '>':
			a=l.strip('\n').split('\t')
			virus = a[0].strip('>').split('.')[0].split('|')[1]
			id = a[0].split(' ')[0].split('|')[1]
			if virus not in genomes[sp]:
				genomes[sp].append(virus)
				genes[sp][virus] = [id]
				seq[sp][virus]={}
			else:
				genes[sp][virus].append(id)
			seq[sp][virus][id]=''
		else:
			seq[sp][virus][id]+=l.strip('\n')
	f.close()

print 'Write'
for sp in species:
	print sp,' ',len(genomes[sp])
	for virus in genomes[sp]:
		h=open('../genomes/' + sp + '/' + virus + '.fa','w')
		for id in genes[sp][virus]:
			h.write('>' + id + '\n' + seq[sp][virus][id] + '\n')
		h.close()
		h=open('../genomes/' + sp + '/' + virus + '.prot','w')
		for id in genes[sp][virus]:
			h.write('>' + id + '\n' + translate(seq[sp][virus][id]) + '\n')
		h.close()

























