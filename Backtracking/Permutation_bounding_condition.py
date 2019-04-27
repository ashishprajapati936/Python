#We have 3 chairs and we have to organize Boy1, Boy2 and Girl1 in such a way that girl should not come in  between two boys.

def girlUnderAttack(board,item):
	length=len(board)
	if item=='G1' and length==1:
		return True;
	else:
		return False;


def organize(items,chosen):
	#print("current items",items)
	if len(items)==0:
		print(chosen)
	for i in range(len(items)):
		item=items[i]
		if girlUnderAttack(chosen,item):	#Bounding condition
			continue
		
		chosen.append(item)
		items.remove(item)
		organize(items,chosen)

		items.insert(i,item)	#backtrack
		chosen.remove(item)

		
l=['B2','G1','B1']



chosen=[]
organize(l,chosen)