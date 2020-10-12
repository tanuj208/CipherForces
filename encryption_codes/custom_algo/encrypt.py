import json

import generate_key

def take_input():
	"""Takes all necessary inputs for encryption."""

	print("Enter the message (using lowercase alphabets) to be encrypted and then press enter: ")
	plaintext = input()
	return plaintext

def add_key_to_json(keys):
	with open('keys.json', 'w+') as f:
		json.dump(keys, f)

def vigenere_encryption(plaintext, key):
	"""Encrypts the message using vigenere cipher."""

	ciphertext = []
	for i in range(len(key)):
		p = ord(plaintext[i])
		k = ord(key[i])
		min_val = ord('a')
		p -= min_val
		k -= min_val
		p += k
		p %= 26
		p += min_val
		ciphertext.append(chr(p))
	return ''.join(ciphertext)

def encrypt_key(key_val, keys):
	"""Encrypts the key using mono-alphabetic substitution cipher."""

	alphabet_map = generate_key.random_alphabet_map()
	keys['map'] = alphabet_map
	encrypted_key = []
	for char in key_val:
		encrypted_char = alphabet_map[char]
		encrypted_key.append(encrypted_char)
	return ''.join(encrypted_key)

def encrypt_message(plaintext):
	"""Encrypts the plaintext."""

	plaintext_len = len(plaintext)
	vigenere_key = generate_key.get_random_text(plaintext_len)
	ciphertext = vigenere_encryption(plaintext, vigenere_key)

	keys = {}
	encrypted_key = encrypt_key(vigenere_key, keys)
	keys['encrypted_key'] = encrypted_key
	add_key_to_json(keys)
	return ciphertext

if __name__ == '__main__':

	plaintext = take_input()
	ciphertext = encrypt_message(plaintext)
	print("Encrypted message is {}".format(repr(ciphertext)))
