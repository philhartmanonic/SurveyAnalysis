import pandas as pd 
import numpy as np 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

product_type = pd.DataFrame(np.nan, index=range(1,29), columns=['Average Age'])

for i in range(1, 29):
	b = 0
	x = 0
	for j in range(len(bdata) - 1):
		if bdata.ix[j, i + 1727] == 1:
				b += bdata.ix[j, 2483]
				x += bdata.ix[j, 2377] * bdata.ix[j, 2483]
		if b != 0:
			product_type.ix[i, 0] = x / b
		else:
			product_type.ix[i, 0] = np.nan

product_type.to_csv('/home/galen/age_x_product.csv')