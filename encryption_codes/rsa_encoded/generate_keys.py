from helper import *
from generate_large_prime import get_prime

def gen_keys(bits = 32):
	p = get_prime(bits)
	q = get_prime(bits)

	n = p*q
	phi = (p-1)*(q-1)
	e = rand_coprime_with(phi)
	d = modInverse(e,phi)

	public_key = [n, e]
	private_key = [d]

	return [public_key,private_key]

if __name__ == '__main__':
	a = gen_keys(16)
	print(a)