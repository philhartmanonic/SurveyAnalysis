import pandas as pd 
import numpy as np 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

message_type = pd.DataFrame(np.nan, index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], columns=range(1, 29))

for i in range(1, 17):
	for j in range(1, 29):
		b = 0
		x = 0
		for k in range(len(bdata) - 1):
			if bdata.ix[k, i + 2307] == 1:
				b += bdata.ix[k, 2483]
				x += bdata.ix[k, 1727 + j] * bdata.ix[k, 2483]
		message_type.ix[i, j] = x / b

message_type.to_csv('/home/galen/message_x_product.csv')