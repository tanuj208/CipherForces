import random  
from math import pow

# GCD of two numbers
def gcd(a, b):
	if a < b:
		return gcd(b, a)
	elif a % b == 0:
		return b;
	else:
		return gcd(b, a % b) 

# Modular exponentiation 
def power(a, b, c):
	x = 1
	y = a
	while b > 0:
		if b % 2 == 0:
			x = (x * y) % c;
		y = (y * y) % c
		b = int(b / 2)
	return x % c 

# Generating large random numbers coprime with q
def rand_coprime_with(q):
	num = random.randint(pow(10, 20), q)
	while gcd(q, num) != 1:
		num = random.randint(pow(10, 20), q)
	return num