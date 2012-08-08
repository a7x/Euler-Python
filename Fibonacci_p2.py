def ifEven(n):
	if(n%2==0):
		return True
	else:
		return False
sum=0
a=1
b=1
c=a+b
while(c<4000000):
	if(ifEven(c)):
		sum=sum+c

	a=b
	b=c
	c=a+b
print sum