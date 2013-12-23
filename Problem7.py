#find the 10001st prime number 
import math
def ifPrime(n):
    ''' returns true/false w.r.t primality of a number. 
        From wikipedia, we find that all primes are of the form 6k +/- 1
        So, instead of doing it till sq(n), lets check, 2, 3 
        and then every number of the form 6k +/- 1
    '''
    
    sqrt = math.sqrt(n)
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

num_primes = 6
start = 17
while True:
    if num_primes == 10001:
        print start - 1
        break
    
    if ifPrime(start):
        num_primes += 1
    start += 1
