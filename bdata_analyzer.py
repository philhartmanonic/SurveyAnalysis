import pandas as pd 

bdata = pd.read_csv('/home/galen/Downloads/BOSS_Data_1316.csv')

message_region = pd.DataFrame()

for i in range(1, 17):
	message_region['Q50 - ' + str(i) + ' - NE'] = 0
	message_region['Q50 - ' + str(i) + ' - MA'] = 0
	message_region['Q50 - ' + str(i) + ' - Other'] = 0

for i in range(len(bdata) - 1):
	if bdata.ix[i, 38] == 1:
		for j in range(1, 17):
			message_region.loc[i, 'Q50 - ' + str(j) + ' - NE'] = bdata.loc[i + 1, 'Q50SELX1_' + str(j)] * bdata.loc[i, 'wt_var']
	elif bdata.ix[i, 38] == 5:
		for j in range(1, 17):
			message_region.loc[i, 'Q50 - ' + str(j) + ' - MA'] = bdata.loc[i + 1, 'Q50SELX1_' + str(j)] * bdata.loc[i, 'wt_var']
	else:
		for j in range(1, 17):
			message_region.loc[i, 'Q50 - ' + str(j) + ' - Other'] = bdata.loc[i + 1, 'Q50SELX1_' + str(j)] * bdata.loc[i, 'wt_var']

print message_region.sum(0)
message_ne = 0
message_ma = 0
message_other = 0
for i in range(len(bdata) - 1):
	if bdata.ix[i, 38] == 1:
		message_ne += bdata.loc[i, 'wt_var']
	elif bdata.ix[i, 38] == 5:
		message_ma += bdata.loc[i, 'wt_var']
	else:
		message_other += bdata.loc[i, 'wt_var']

mne = message_region[message_region.columns[0::3]]
mma = message_region[message_region.columns[1::3]]
mother = message_region[message_region.columns[2::3]]

message_ne_scores = mne.sum(0) / message_ne
message_ma_scores = mma.sum(0) / message_ma
message_other_scores = mother.sum(0) / message_other

df = []
for i in range(len(message_ne_scores)):
	df.append({'key' : i + 1, 'Northeast' : message_ne_scores[i], 'Mid-Atlantic' : message_ma_scores[i], 'Other' : message_other_scores[i]})
mScores = pd.DataFrame(df)
mScores.to_csv('/home/galen/mScores.csv')