def ifSame(a,b):
	if(a>b):
		larger=a
		smaller=b
	else:
		larger=b
		smaller=a
	larger=str(larger)
	smaller=str(smaller)
	
	for i in larger:
		if(i not in smaller):
			return False
	return True

smallest=True
num=11

while(smallest):
	
	
	if(ifSame(num,num*2) and ifSame(num,num*3) and ifSame(num,num*4) and ifSame(num,num*5) and ifSame(num,num*6)):
		print num
		smallest=False
	else:
		num=num+1


