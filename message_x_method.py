import pandas as pd 
import numpy as np 
import time
import progressbar as pb 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

message_type = pd.DataFrame(np.nan, index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], columns=range(1, 6))

with pb.ProgressBar(max_value=pb.UnknownLength) as bar:
	for i in range(100):
		time.sleep(0.1)
		bar.update(i)

for i in range(1, 17):
	for j in range(1, 6):
		b = 0
		x = 0
		for k in range(len(bdata) - 1):
			if bdata.ix[k, i + 2307] == 1:
				b += bdata.ix[k, 2483]
				x += bdata.ix[k, 179 + j] * bdata.ix[k, 2483]
		message_type.ix[i, j] = x / b

message_type.to_csv('/home/galen/message_x_method.csv')