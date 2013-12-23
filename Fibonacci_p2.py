def ifEven(n):
    if n%2 == 0: 
        return True
    return False

_sum = 0
a, b = 1, 1
c= a + b
while c < 4000000:
    if ifEven(c):
        _sum += c
    a, b = b, c
    c = a + b
    
print _sum
