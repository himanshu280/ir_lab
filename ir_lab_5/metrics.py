from splitter import model_out,qrel,rel_docs

# print( model_out['301'] )
# print( "\n" )
# print( qrel['301'] )
# print( rel_docs )

# evaluate average precision per qurey
avg_precision = dict()

for qId in model_out.keys():
	avg_precision[qId] = 0
	tot_ret = 0
	rel_ret = 0
	avg_pre = 0
	
	for ret in model_out[qId]:
		tot_ret += 1

		try:
			if qrel[qId][ret[0]] == '1':
				rel_ret += 1

				# add to summation
				avg_pre += (rel_ret * 1.0)/tot_ret
			else:
				rel_ret += 0
		except:
			rel_ret += 0
	
	avg_precision[qId] = (avg_pre * 1.0) / rel_docs[qId]

# print(avg_precision  )
sum_precision = 0
for qId in avg_precision.keys():
	sum_precision += avg_precision[qId]

mean_average_precision = (sum_precision * 1.0) / len( avg_precision.keys() )

print( "Average Precision per query" )
for qId in avg_precision.keys():
	print( qId + " >> " + str(avg_precision[qId]) )
print("\n")
print( "MAP >> " + str(mean_average_precision) )