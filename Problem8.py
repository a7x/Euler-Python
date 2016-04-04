import operator
print max(reduce(operator.mul, [int(x) for x in large_number[i:i+5]], 1) \
               for i in range(len(large_number)))
