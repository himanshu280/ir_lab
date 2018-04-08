import operator

# reading output file
model_out = dict()

fh = open('./results.test')
for line in fh:
	result = line.split()
	qId = result[0]
	doc = result[2]
	rank = int(result[3])
	score = result[4]

	if qId not in model_out.keys():
		model_out[qId] = []
	else:
		model_out[qId].append((doc,rank,score))
fh.close()

# sort according to ranking
for key in model_out.keys():
	model_out[key].sort(key=operator.itemgetter(1),reverse=False)

# reading qrel file
qrel = dict()

fh = open('./qrels.test')
for line in fh:
	result = line.split()
	qId = result[0]
	doc = result[2]
	relInfo = result[3]

	if qId not in qrel.keys():
		qrel[qId] = dict()
	else:
		qrel[qId][doc] = relInfo

# get number of relevant docs
rel_docs = dict()

for qId in qrel.keys():
	rel_docs[qId] = 0
	for docId in qrel[qId]:
		if qrel[qId][docId] == '1':
			rel_docs[qId] += 1