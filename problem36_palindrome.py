from __future__ import division
import math
def ifPalindrome(s):
	return s==s[::-1]
def getBinary(num):
	binaryNum=''

	n=num
	rem=num%2
	while(n!=0):

		binaryNum=binaryNum+str(rem)
		n=n//2
		rem=n%2
	
	return binaryNum

sum=0

for i in range(1,1000001):

	if(ifPalindrome(str(i))):
		binaryStr=str(getBinary(i))

		if(binaryStr[0]!='0' and ifPalindrome(binaryStr)):
			sum=sum+i
			print 'Adding ',i,' coz the binary is ',binaryStr
print sum



