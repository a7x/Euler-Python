from collections import Counter
def ifSame(a, b):
    return Counter(str(a)) == Counter(str(b))

start = 11
while True:
    if ifSame(num, num * 2) and ifSame(num, num * 3) and ifSame(num, num * 4) and ifSame(num, num * 5) and \
        ifSame(num, num * 6):
            print num
            break
    else:
        start += 1
