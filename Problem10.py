def ifPrime(n):
    ''' returns true/false w.r.t primality of a number. 
        From wikipedia, we find that all primes are of the form 6k +/- 1
        So, instead of doing it till sq(n), lets check, 2, 3 and then every number of the form 6k +/- 1
    '''
    #print math.sqrt(n)
    sqrt = math.sqrt(n)
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if str(n).endswith('0') or str(n).endswith('5'):
        return False
    k = 1
    first, second = (6 * k) - 1, (6 * k) + 1
    while first <= sqrt:
        if n%first == 0 or n%second == 0:
            return False
        k += 1
        first, second = (6 * k) - 1, (6 * k) + 1
    return True
    
start = 2 
print start + sum([n for n in xrange(3, 2000000) if ifPrime(n)])

  
