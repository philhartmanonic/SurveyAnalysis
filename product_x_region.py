import pandas as pd 
import numpy as np 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

message_type = pd.DataFrame(np.nan, index=range(1,29), columns=["Northeast", "Mid Atlantic", "Other"])
message_score = pd.DataFrame(np.nan, index=range(1,29), columns=["Northeast", "Mid Atlantic", "Other"])

for i in range(1, 29):
	ne = 0
	ma = 0
	o = 0
	for j in range(len(bdata) - 1):
		if bdata.ix[j, i + 1727] == 1:
			if bdata.ix[j, 38] == 1:
				ne += bdata.ix[j, 2483]
			elif bdata.ix[j, 38] == 5:
				ma += bdata.ix[j, 2483]
			else:
				o += bdata.ix[j, 2483]
	message_type.ix[i, 0] = ne
	message_type.ix[i, 1] = ma
	message_type.ix[i, 2] = o

neb = 0
mab = 0
ob = 0

for i in range(len(bdata) - 1):
	if bdata.ix[i, 38] == 1:
		neb += bdata.ix[i, 2483]
	elif bdata.ix[i, 38] == 5:
		mab += bdata.ix[i, 2483]
	else:
		ob += bdata.ix[i, 2483]

for i in range(1, 29):
	message_score.ix[i, 0] = message_type.ix[i, 0] / neb
	message_score.ix[i, 1] = message_type.ix[i, 1] / mab
	message_score.ix[i, 2] = message_type.ix[i, 2] / ob

message_score.to_csv('/home/galen/product_x_region.csv')