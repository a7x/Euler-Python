from __future__ import division
import math

def next_two_primes(k, max_number):
	if 6*k + 1 < max_number:
		yield (6*k -1 , 6*k + 1)

max_prime = -1
main_num = 600851475143
max_number = math.pow(main_num, 0.5)
k = 1

while True:
	two_primes = next_two_primes(k, max_number).next()

	if main_num % two_primes[1] == 0 and max_prime < two_primes[1]:
			max_prime = two_primes[1]
			k += 1
			continue
	elif main_num % two_primes[0] == 0 and max_prime < two_primes[0]:
		max_prime = two_primes[0]
		k += 1
		continue 

print max_prime
