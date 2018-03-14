chemin = "/Users/louis-mariebobay/Desktop/patterns/"
#chemin = "/work/03239/lbobay/landscape/"



species=["Snod"]



chemin=""


print species

for SP in species:
	print SP
	f=open(chemin + "clado_nickname.tree","r")
	l=f.readline()
	l = l.strip("\n")
	l = l.strip(";")
	f.close()


	numbers=["0","1","2","3","4","5","6","7","8","9"]
	resu=""
	i=0
	while i < len(l):
		L = l[i]
		if l[i] in numbers:
			if i ==0:
				resu+=l[i]	
			elif l[i-1] == ")" or l[i-2] == ")" or l[i-3] == ")":
				pass
			else:
				resu+=l[i]
		else:
			resu+= l[i]
		i+=1


	resu = l


	I = 1
	
	dico={}
	detail={}
	arbre={}
	arbre[I]=resu
	first={}
	level={}
	while arbre[I].count("(") > 1:
		groupe=[]
		memo=[]
		resu=str(arbre[I])
		#print arbre[I]
		resu2 = resu
		node=0
		i=0
		while i < len(resu):
			k = resu[i]
			if k == "B" or k == "n":
				name=k
			elif k != "," and k !="("  and k !=")":
				name += k
			else:
				if k==",":
					if resu[i+1] == "B" or  resu[i+1] =="n":
						if name not in memo:
							groupe=[name]
						else:
							groupe=[]
				if k == ")":
					if name not in groupe:
						if name not in memo:
							if len(groupe) == 1:
								groupe.append(name)
								memo.extend(groupe)
								node += 1
								NODE = "n" + str(I) + "_" + str(node)
								mono = "(" + groupe[0] + "," + groupe[1] + ")"
								if mono in resu2:
									level[NODE] = I
									resu2 = resu2.replace(mono,NODE)
									dico[NODE] = [groupe[0] , groupe[1]]
									if "B" not in groupe[0]:
										detail[NODE] = list(detail[groupe[0]])
									else:
										detail[NODE] =[groupe[0]]
									if "B" not in groupe[1]:
										for stuff in detail[groupe[1]]:
											detail[NODE].append(stuff)
									else:
										detail[NODE].append(groupe[1])
								else:
									node = node - 1
			i+=1
		I+=1
		arbre[I] = resu2
	



	MAX_I = int(I)

	#print l.strip("\n")
	print arbre[MAX_I]
	
	nb=0
	if "B" in arbre[MAX_I]:
		a=arbre[MAX_I].strip("(").strip(")").split(",")
		for truc in a:
			if "B" in truc:
				nb+=1
				out = truc
				detail["n0_" + str(nb) + "_out"] = [out]
	
	
	
	h=open(chemin + "mono.txt","w")
	parent={}
	for NODE in detail:
		detail[NODE].sort()
		h.write(NODE + "\t" + "\t".join(detail[NODE]) + "\n")
		for st in detail[NODE]:
			if parent.has_key(st):
				parent[st].append(NODE)
			else:
				parent[st] = [NODE]
	
	h.close()

	strains=[]
	for st in parent:
		strains.append(st)



	all=list(strains)
	noeuds=[]
	for node in detail:
		noeuds.append(node)
		all.append(node)

	noeuds.sort()

	#print noeuds


	

	ancester,converge,intern={},{},{}
	for st in strains:
		ancester[st],converge[st],intern[st]={},{},{}
	

	for st1 in strains:
		for st2 in strains:
			if st1 != st2:
				family1,common=[],[]
				for node in parent[st1]:
					family1.append(node)
				for node in parent[st2]:
					if node in family1:
						common.append(node)
				if len(common) == 0:
					ancester[st1][st2] = 100000000
					ancester[st2][st1] = 100000000
				else:
					MIN = 1000000
					memo= ""
					for node in common:
						I = int(node.lstrip("n").split("_")[0])
						if I < MIN:
							memo=I
							MIN=I
					ancester[st1][st2]=memo
					ancester[st2][st1]=memo
				#print st1," ",st2," ",common," ",ancester[st1][st2]
				chemin1=0
				for node in parent[st1]:
					I = int(node.lstrip("n").split("_")[0])
					if I <= ancester[st1][st2]:
						chemin1 += 1
				chemin2=0
				for node in parent[st2]:
					I = int(node.lstrip("n").split("_")[0])
					if I <= ancester[st1][st2]:
						chemin2 += 1
				if ancester[st1][st2] == 100000000:
					total = chemin1 + chemin2 
				else:
					total = chemin1 + chemin2 - 1
				converge[st1][st2] = total
				converge[st2][st1] = total
							



	h=open(chemin +  "convergence.txt","w")
	for st1 in strains:
		for st2 in strains:
			if st1 != st2:
				h.write(st1 + "\t" + st2 + "\t" + str(converge[st1][st2]) + "\n")
	h.close()




