import pandas as pd 
import numpy as np 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

message_type = pd.DataFrame(np.nan, index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], columns=['Average Age'])

for i in range(1, 17):
	b = 0
	x = 0
	for j in range(len(bdata) - 1):
		if bdata.ix[j, i + 2307] == 1:
				b += bdata.ix[j, 2483]
				x += bdata.ix[j, 2377] * bdata.ix[j, 2483]
		if b != 0:
			message_type.ix[i, 0] = x / b
		else:
			message_type.ix[i, 0] = np.nan

message_type.to_csv('/home/galen/age_x_message.csv')