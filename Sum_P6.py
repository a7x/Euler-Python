#Sum of squares and square of sum for 1 - 100
import math
sumSquares=0
squareSum=0
sumNum=0
for i in range(1,101):
	sumSquares=sumSquares+i*i
	sumNum=sumNum+i
print (sumNum*sumNum)-sumSquares
