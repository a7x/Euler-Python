from __future__ import division

def pentagon(n):
	return (n * (3 * n - 1))/2

def adding(n):
	return (3*n*n) - (4 * n) + 2

def subtracting(n):
	return (3 * n) - 2

def ifPentagon(number):
	''' solve an equation of the form ax2 + bx + c,  the result should be an int '''
	rhs = number * 2
	a = 3 
	b = -1
	c = -rhs
	
		

print [pentagon(x) for x in xrange(20)]
