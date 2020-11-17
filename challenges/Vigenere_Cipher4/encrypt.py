import random
import sys

def encrypt(plaintext, key):
	ciphertext = []
	cnt = 0
	for c in plaintext:
		ascii_num = ord(c) - ord('a')
		ascii_num += key[cnt]
		if(cnt > 0):
			ascii_num += ord(ciphertext[cnt - 1]) - ord('a')
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
	for i in range(key_length, len(plaintext)):
		key.append(key[i % key_length])
	ciphertext = encrypt(plaintext, key)
	print(ciphertext)