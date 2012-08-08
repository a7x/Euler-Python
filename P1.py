#Sum of all multiples of 3 or 5 below 1000
def ifDivisible(n):
	#return true if divisible by 3 or 5
	if(n%3==0 or n%5==0):
		return True
	else:
		return False
sum = 0
for i in range(3,1000):
	if(ifDivisible(i)):
		sum=sum+i
print sum

