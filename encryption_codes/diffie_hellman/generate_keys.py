from Crypto.Util import number
import json
import random

def take_input():
	num_bits = int(input("Enter number of bits of the prime number: "))
	return num_bits

def store_keys(num_bits):
	keys = {}
	keys['prime_number'] = number.getPrime(num_bits)
	keys['generator'] = random.randint(2, 1000)
	keys['sender_secret_key'] = random.randint(2, keys['prime_number']-1)
	keys['receiver_secret_key'] = random.randint(2, keys['prime_number']-1)
	keys['sender_public_key'] = get_public_key(keys['sender_secret_key'], keys['prime_number'], keys['generator'])
	keys['receiver_public_key'] = get_public_key(keys['receiver_secret_key'], keys['prime_number'], keys['generator'])
	with open('keys.json', 'w+') as f:
		json.dump(keys, f)

def get_public_key(secret_key, prime_num, generator):
	public_key = pow(generator, secret_key, prime_num)
	return public_key

if __name__ == '__main__':
	num_bits = take_input()
	store_keys(num_bits)
