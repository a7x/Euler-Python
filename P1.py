#print sum of all numbers divisible by 3 or 5 in the range (3, 1000)

#PLEASE don't see below if you haven't tried the problem yourself and given up. This solution is here only if you are horribly lost and out of ideas. 

''' 
Earlier this code was done as below. It would go through the list and then find out if it is divisible by 3 or 5 and update the sum accordingly. 
But, recently I saw a question on hackerrank which was a great twist on this question and asked me to find this sum for an arbitrary limit, 
e.g 10000000

This code is being kept here to show you the difference! '''
'''
def ifDivisible(n):
    if n%3 == 0 or n%5 == 0:
        return True
    return False

print sum([i for i in range(3, 1000) if ifDivisible(i)])
'''

''' Note that all digits divisible by 3 form an arithmetic sequence: 3, 6, 9, 12, 15, 18, 21 . . . . . 
    Similarly, all digits divisible by 5 would form a sequence: 5, 10, 15, 20, 25, 30, 35, 40 . . . . 
    We could just add those two and get our answer! But, we are repeating digits, which are, 15, 30, 45 . . . . notice a pattern?!?! 
    It's another arithmetic sequence with d = 15!
    
'''
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        if N%3==0:
            num_terms_three = N//3 - 1
        else:
            num_terms_three = N//3
        if N%5==0:
            num_terms_five = N//5 - 1
        else:
            num_terms_five = N//5
        if N%15 == 0:
            num_terms_fifteen = N//15 - 1
        else:
            num_terms_fifteen = N//15
        
        sum_three = (num_terms_three * (6 + (num_terms_three - 1) * 3))//2
        sum_five = (num_terms_five * (10 + (num_terms_five - 1) * 5))//2
        sum_fifteen = (num_terms_fifteen * (30 + (num_terms_fifteen - 1)*15))//2
        print(sum_three + sum_five - sum_fifteen)
        
