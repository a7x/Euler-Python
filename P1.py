#print sum of all numbers divisible by 3 or 5 in the range (3, 1000)
def ifDivisible(n):
    if n%3 == 0 or n%5 == 0:
        return True
    return False

print sum([i for i in range(3, 1000) if ifDivisible(i)])
