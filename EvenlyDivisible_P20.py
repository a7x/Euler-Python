#Find the smallest number divisible by all numbers from 1 to 20 
def ifDivisible(n):
	for i in range(2,21):
		if(n%i!=0):
			return False
	return True
start=22
while(ifDivisible(start)!=True):
	start=start+1
print start