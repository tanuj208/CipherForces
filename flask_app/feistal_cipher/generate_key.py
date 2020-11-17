import json
import random

def take_input():
	print("Enter the number of bits of key required and then press enter: ")
	num_bits = int(input())
	return num_bits

def get_random_key(num_bits):
	random_key = []
	for _ in range(num_bits):
		bit_val = random.randint(0, 1)
		random_key.append(str(bit_val))
	return ''.join(random_key)

if __name__ == '__main__':
	num_bits = take_input()
	keys = {}
	keys['K1'] = get_random_key(num_bits)
	keys['K2'] = get_random_key(num_bits)
	with open('keys.json', 'w+') as f:
		json.dump(keys, f)
