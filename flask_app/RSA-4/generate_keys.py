from helper import *
from Crypto.Util import number
import json

def gen_keys(bits = 32):
	keys = {}

	p = number.getPrime(bits)
	q = number.getPrime(bits)

	n = p*q
	phi = (p-1)*(q-1)
	e = rand_coprime_with(phi)
	d = modInverse(e,phi)

	keys['public_key'] = {'n' : n, 'e' : e}
	keys['private_key'] = {'d' : d}
	with open('RSA-4/keys.json', 'w+') as f:
		json.dump(keys, f)
	return keys

if __name__ == '__main__':
	a = gen_keys(256)
	print(a)