
species=[]
f=open('../selected_species.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	species.append(a[0])

f.close()



print species


h=open("big_graph.R",'w')


NB,nb=1,0
for sp in species:
	nb+=1
	if nb == 1:
		h.write("pdf('../results/Graph" + str(NB) + ".pdf')\n")
		h.write("par(mfrow=c(3,3))\n")
	h.write(  "tab = read.table('../results/" + sp + "/graph.txt',h=T)\n")
	h.write('w=c(tab$Nb,rev(tab$Nb))\n')
	h.write('v=c(tab$Median-tab$SD,rev(tab$Median + tab$SD))\n')
	h.write('plot(100,100,cex=0.5,cex.main=0.8,xlim=c(3,max(w)),ylim=c(0,max(v) + 0.1),xlab=c("# Genomes"),ylab=c("h/m"),main="' + sp + '")\n')
	h.write('polygon(w,v,col="gray88",border=NA)\n')
	h.write('points(tab$Nb,tab$Median,pch=16,cex=0.3,t="b")\n')
	if nb == 9:
		nb = 0
		NB+=1
		h.write("dev.off()\n\n")



h.write("dev.off()\n\n")

h.close()



