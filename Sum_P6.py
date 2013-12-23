#Sum of squares and square of sum for 1 - 100
import math
sumSquares, squareSum, sumNum = 0, 0, 0

for i in xrange(1,101):
	sumSquares += (i*i)
	sumNum += i
	
print (sumNum*sumNum) - sumSquares
