def Fibonacci(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return Fibonacci(n-1)+Fibonacci(n-2)
	
n=int(input("Enter any number to find the fibonnaci series upto that number: "))
for i in range(n):
	print(Fibonacci(i))