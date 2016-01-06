import pandas as pd 
import numpy as np 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

product_type = pd.DataFrame(np.nan, index=range(1, 29), columns=['BOSS', 'Buyers', 'Douglas', 'Fisher', 'Western', 'Blizzard', 'Henderson', 'Hiniker', 'Kage', 'Monroe', 'Meyer', 'SnowWolf', 'Sno-Way', 'Other'])
product_score = pd.DataFrame(np.nan, index=range(1, 29), columns=['BOSS', 'Buyers', 'Douglas', 'Fisher', 'Western', 'Blizzard', 'Henderson', 'Hiniker', 'Kage', 'Monroe', 'Meyer', 'SnowWolf', 'Sno-Way', 'Other'])

cols = {0:40, 1:41, 2:42, 3:43, 4:51, 5:39, 6:44, 7:45, 8:46, 9:47, 10:48, 11:49, 12:50, 13:54}
comps = []

for i in range(1, 29):
	for j in range(14):
		x = 0
		for k in range(len(bdata) - 1):
			if bdata.ix[k, cols[j]] == 1 and bdata.ix[k, i + 1727] == 1:
				x += bdata.ix[k, 2483]
		product_type.ix[i, j] = x

for i in range(14):
	comp = 0
	for j in range(len(bdata) - 1):
		if bdata.ix[j, cols[i]] == 1:
			comp += bdata.ix[j, 2483]
	comps.append(comp)

for i in range(1, 29):
	for j in range(14):
		product_score.ix[i, j] = product_type.ix[i, j] * comps[j]

product_score.to_csv('/home/galen/product_x_ownerType.csv')