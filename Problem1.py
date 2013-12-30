def problem1():
	return sum([item  for item in xrange(1000) if item % 3 == 0 or item % 5 == 0])

def problem2():
	a, b = 1, 1
	c = a + b
	MAX = 4000000
	s = 0
	while c < MAX: 
		if c % 2 == 0:
			s += c
		a, b = b, c
		c =  a + b
		continue
	return s





if __name__ == '__main__':
	print problem1()
	print problem2()