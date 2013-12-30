#newcode 
def power(a, b):
    return a ** b

def sum_digits(num):
    return sum([int(x) for x in str(num)])


print max([sum_digits(power(i, j)) for i in xrange(0, 100) for j in xrange(0, 100)])
