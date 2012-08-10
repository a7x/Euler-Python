def factorial(n):
	s=1
	for i in range(2,n+1):
		s=s*i
	return s

fact=str(factorial(100))
sumNum=0
for i in fact:
	sumNum=sumNum+int(i)
print sumNum
