import pandas as pd 
import numpy as np 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

message_type = pd.DataFrame(0, index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, "Comp"], columns=['BOSS', 'Buyers', 'Douglas', 'Fisher', 'Western', 'Blizzard', 'Henderson', 'Hiniker', 'Kage', 'Monroe', 'Meyer', 'SnowWolf', 'Sno-Way', 'Other'])

comp = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
tots = 0
cols = {0:40, 1:41, 2:42, 3:43, 4:51, 5:39, 6:44, 7:45, 8:46, 9:47, 10:48, 11:49, 12:50, 13:54}
fits = {0:{1:0}}

for j in range(14):
	for i in range(len(bdata) - 1):
		if bdata.ix[i, cols[j]] == 1:
			fits[j].append({i:[]})



for i in range(14):
	for j in range(len(fits[i])):
		for k in range(1, 17):
			message_type.ix[k, i] += (bdata.iloc[fits[i][j], cols[i]] * bdata.iloc[fits[i][j], 2307 + k] * bdata.loc[fits[i][j], 'wt_var'])


for i in range(14):
	for j in range(len(bdata) - 1):
		tots += bdata.iloc[j, cols[i]] * bdata.loc[j, 'wt_var']
	comp[i] += tots
	tots = 0

for i in range(14):
	message_type.ix['Comp', i] = comp[i]

message_type.to_csv('/home/galen/mTypeScoresReal.csv')