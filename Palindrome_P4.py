def ifPalindrome(n):
    return n == n[::-1]

print max([i*j for i in xrange(100, 1000) \
               for j in xrange(i+1, 1000) if ifPalindrome(str(i*j))])
