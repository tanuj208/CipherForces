import json

import generate_key

def get_keys():
	with open('keys.json', 'r') as f:
		keys = json.load(f)
	return keys

def encrypt(plaintext):
	"""Encrypts the key using mono-alphabetic substitution cipher."""

	alphabet_map = get_keys()
	ciphertext = []
	for char in plaintext:
		if char not in alphabet_map:
			ciphertext.append(char)
		else:
			encrypted_char = alphabet_map[char]
			ciphertext.append(encrypted_char)
	return ''.join(ciphertext)


if __name__ == '__main__':

	plaintext = input()
	ciphertext = encrypt(plaintext)
	print(repr(ciphertext))
