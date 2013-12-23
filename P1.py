def ifDivisible(n):
    if n%3 == 0 or n%5 == 0:
        return True
    return False

print sum([i for i in xrange(3, 1000) if ifDivisible(i)])
