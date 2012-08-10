def ifPalindrome(n):

	newS=n[::-1]
	return newS==n
largest=-1

for i in range(100,1000):
	for j in range(i+1,1000):
		product=i*j
		if(ifPalindrome(str(product))):
			if(largest<product):
				largest=product
print largest
