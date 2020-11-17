import random
import sys

def encrypt(plaintext, key):
	ciphertext = []
	for c in plaintext:
		ascii_num = ord(c)
		ascii_num -= ord('a')
		ascii_num += key
		ascii_num %= 26
		ascii_num += ord('a')
		new_char = chr(ascii_num)
		ciphertext.append(new_char)
	return ''.join(ciphertext)

if __name__ == '__main__':
	plaintext = sys.argv[1]
	key = random.randint(1, 25)
	ciphertext = encrypt(plaintext, key)
	print(ciphertext)

