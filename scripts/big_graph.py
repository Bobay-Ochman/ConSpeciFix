from config import *


species= ['Acetobacter_pasteurianus','Bacillus_weihenstephanensis','Buchnera_aphidicola','Clostridium_beijerinckii','Corynebacterium_glutamicum','Corynebacterium_jeikeium','Cutibacterium_acnes','Gallibacterium_anatis','Gilliamella_apicola','Klebsiella_quasipneumoniae','Klebsiella_variicola','Lactobacillus_crispatus','Lactobacillus_fermentum','Lactobacillus_helveticus','Lactobacillus_salivarius','Leptospira_kirschneri','Methanobrevibacter_smithii','Micrococcus_luteus','Microcystis_aeruginosa','Morganella_morganii','Mycobacterium_africanum','Mycobacterium_chelonae','Mycobacterium_colombiense','Mycobacterium_fortuitum','Mycobacterium_immunogenum','Mycobacterium_kansasii','Mycoplasma_bovis','Mycoplasma_gallisepticum','Mycoplasma_mycoides','Porphyromonas_gingivalis','Prochlorococcus_marinus','Pseudoalteromonas_luteoviolacea','Pseudomonas_chlororaphis','Pseudomonas_denitrificans','Pseudomonas_psychrotolerans','Pseudomonas_stutzeri','Raoultella_ornithinolytica','Rhodococcus_fascians']
h=open("big_graph.R",'w')

NB,nb=1,0
for sp in species:
	nb+=1
	if nb == 1:
		h.write("pdf('"+PATH_TO_OUTPUT+'zGraph/gno' + str(NB) + ".pdf')\n")
		h.write("par(mfrow=c(4,4))\n")
	h.write(  "tab = read.table('"+PATH_TO_OUTPUT + sp + "/graph.txt',h=T)\n")
	h.write('w=c(tab$Nb,rev(tab$Nb))\n')
	h.write('v=c(tab$Median-tab$SD,rev(tab$Median + tab$SD))\n')
	h.write('plot(100,100,cex=0.5,cex.main=0.8,xlim=c(3,max(w)),ylim=c(0,max(v) + 0.1),xlab=c("# Genomes"),ylab=c("h/m"),main="' + sp + '")\n')
	h.write('polygon(w,v,col="gray88",border=NA)\n')
	h.write('points(tab$Nb,tab$Median,pch=16,cex=0.3,t="b")\n')
	if nb == 16:
		nb = 0
		NB+=1
		h.write("dev.off()\n\n")


h.write("dev.off()\n\n")

h.close()



