def toh(disks,source,aux,target):
	if disks==1:
		print("Move disk from {} to {}".format(source,target))
		return
	#move n-1 disks from source to aux
	toh(disks-1,source,target,aux)
	#move nth disks from source to targer
	print("Move disk from {} to {}".format(source,target))
	#move n-1 disks from aux to taget
	toh(disks-1,aux,source,target)
	
n=int(input("Please enter number of disks: "))
print("Please follow below steps to accomplish tower of hanoi.")
toh(n,"Tower-A","Tower-B","Tower-C")