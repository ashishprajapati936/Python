def gcd(a,b):
	if a%b==0:
		return b
	return gcd(b,a%b)
	
print("Program to find gcd of two numbers.")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("GCD of {} and {} is".format(a,b),gcd(a,b))
