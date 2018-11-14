from PIL import Image
import numpy as np

pat="/Users/ochmanlab/Desktop/brian/ocmc/_conspecifix/database/User_spec/visual.txt"

fd = open(pat,'r')
totalRes = {}
totalStrains = []
length = 0
print("starting")
for l in fd.readlines():
	parts = l.strip().split('\t')
	truc = parts[0]
	trucStrains = truc.split('&&&')
	totalStrains.extend(trucStrains)
	mapping = parts[1]
	actualMap = mapping.split(',')
	length = len(actualMap)
	totalRes[str(len(trucStrains))+'-'+truc] = actualMap

print("mark")
totalStrains = list(set(totalStrains))
strainMaps = {}
for s in totalStrains:
	strainMap = []
	for index in range(length):
		maxCharSoFar = 'n'
		for key in totalRes.keys():
			if s in key:
				if totalRes[key][index] == 'r':
					maxCharSoFar = 'r'
				elif totalRes[key][index] == 'm' and maxCharSoFar == 'n':
					maxCharSoFar = 'm'
		strainMap.append(maxCharSoFar)
	strainMaps[s] = strainMap

print("consolidate")
mapToPrint = []
for s in strainMaps:
	res = []
	for item in strainMaps[s]:
		if item == 'n':
			res.append([0,0,0])
		if item == 'm':
			res.append([255,0,0])
		if item == 'r':
			res.append([0,0,255])
	mapToPrint.append(res)

print("image")
data = np.array(mapToPrint)
# w, h = len(totalRes[0]), len(totalRes)
# data = np.zeros((h, w, 3), dtype=np.uint8)
# for i in range(len(totalRes)):
# 	for j in range(len(totalRes[i])):
# 		data[i, j] = totalRes[i][j]
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()