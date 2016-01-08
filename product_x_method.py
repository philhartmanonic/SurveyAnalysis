import pandas as pd 
import numpy as np 
import time
import progressbar as pb 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

product_type = pd.DataFrame(np.nan, index=range(1,29), columns=range(1, 6))

for i in range(1, 29):
	for j in range(1, 6):
		b = 0
		x = 0
		for k in range(len(bdata) - 1):
			if bdata.ix[k, i + 1727] == 1:
				b += bdata.ix[k, 2483]
				x += bdata.ix[k, 179 + j] * bdata.ix[k, 2483]
		product_type.ix[i, j] = x / b

product_type.to_csv('/home/galen/product_x_method.csv')