import random

def get_random_key():
	random_key = []
	for _ in range(64):
		bit_val = random.randint(0, 1)
		random_key.append(str(bit_val))
	return ''.join(random_key)

if __name__ == '__main__':
	key = get_random_key()
	print("Key is {}".format(key))
