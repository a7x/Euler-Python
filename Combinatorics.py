#Find how many nCr are > 1 million
from __future__ import division

def factorial(n):
	#Returns n!
	fact=1
	if(n==0):return 1
	for i in range(2,n+1):
		fact=fact*i
	return fact
def combination(n,r):
	#Returns nCr
	numerator=factorial(n)
	denominator=factorial(r)*factorial(n-r)
	return numerator//denominator
millionMore=0
MILLION=1000000
for i in range(1,101):
	for j in range(0,i):
		if(combination(i,j)>MILLION):
			millionMore=millionMore+1
print factorial(5)
print factorial(3)

print combination(5,3)
print millionMore
print combination(23,10)




