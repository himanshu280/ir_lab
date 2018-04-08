import operator

# reading output file
model_out = dict()

fh = open('./results.test')
for line in fh:
	result = line.split()
	qId = result[0]
	doc = result[2]
	rank = result[3]
	score = result[4]

	if qId not in model_out.keys():
		model_out[qId] = []
	else:
		model_out[qId].append((doc,rank,score))
fh.close()

# sort according to ranking
for key in model_out.keys():
	model_out[key].sort(key=operator.itemgetter(2),reverse=True)

print( model_out['301'] )