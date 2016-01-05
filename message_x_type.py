import pandas as pd 
import numpy as np 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

message_type = pd.DataFrame(np.nan, index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, "Comp"], columns=['BOSS', 'Buyers', 'Douglas', 'Fisher', 'Western', 'Blizzard', 'Henderson', 'Hiniker', 'Kage', 'Monroe', 'Meyer', 'SnowWolf', 'Sno-Way', 'Other'])
cols = {0:40, 1:41, 2:42, 3:43, 4:51, 5:39, 6:44, 7:45, 8:46, 9:47, 10:48, 11:49, 12:50, 13:54}


for i in range(1, 17):
	for j in range(14):
		x = 0
		for k in range(len(bdata) - 1):
			if bdata.ix[k, cols[j]] == 1 and bdata.ix[k, i + 2307] == 1:
				x += bdata.ix[k, 2483]
		message_type.ix[i, j] = x

for i in range(14):
	comp = 0
	for j in range(len(bdata) - 1):
		if bdata.ix[j, cols[i]] == 1:
			comp += bdata.ix[j, 2483]
	message_type.ix['Comp', i] = comp

message_type.to_csv('/home/galen/mTypeScoresReal.csv')