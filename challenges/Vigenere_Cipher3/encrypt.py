import random
import sys

def encrypt(plaintext, key):
	ciphertext = []
	cnt = 0
	for c in plaintext:
		ascii_num = ord(c) - ord('a')
		ascii_num += key[cnt]
		ascii_num %= 26
		ascii_num += ord('a')
		new_char = chr(ascii_num)
		ciphertext.append(new_char)
		cnt += 1
	return ''.join(ciphertext)

if __name__ == '__main__':
	plaintext = sys.argv[1]
	key_length = random.randint(len(plaintext)//3, len(plaintext)//2)
	key = []
	for i in range(key_length):
		key.append(random.randint(0, 25))
	var = 0
	temp = 0
	final_key = []
	while temp < len(plaintext):
		if(var % 2 == 0):
			for i in range(key_length):
				if temp == len(plaintext):
					break
				final_key.append(key[i])
				temp += 1
			var = (var + 1) % 2
		else:
			for i in range(key_length):
				if temp == len(plaintext):
					break
				final_key.append(key[key_length - i - 1])
				temp += 1
			var = (var + 1) % 2
	ciphertext = encrypt(plaintext, final_key)
	print(ciphertext)