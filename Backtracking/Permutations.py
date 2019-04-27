#We have 3 chairs and we have to organize Boy1, Boy2 and Girl1 in all possible ways. Print all the possible solutions



def organize(items,chosen):
	#print("current items",items)
	if len(items)==0:
		print(chosen)
	for i in range(len(items)):
		item=items[i]
		chosen.append(item)
		items.remove(item)
		organize(items,chosen)
		#print("backtracking")
		items.insert(i,item)	#backtrack
		chosen.remove(item)


l=['B1','B2','G1']
organize(l,[])