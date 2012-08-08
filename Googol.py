#Problem 56
def power(a,b):
	#Find a**b
	print 'a=',a,'b=',b
	return a**b
def sumDigits(num):
	sumdig=0
	for i in num:
		sumdig=sumdig+int(i)
	return sumdig
maxSum=-1
print sumDigits(str(power(10,100)))
print sumDigits(str(power(2,5)))
for i in range(0,100):
	for j in range(0,100):
		sumDig=sumDigits(str(power(i,j)))
		if(sumDig>maxSum):
			maxSum=sumDig
print maxSum