import json
import sys
import generate_key

def take_input():
	"""Takes all necessary inputs for encryption."""

	plaintext = sys.argv[1]
	return plaintext

def get_keys():
	with open('keys.json', 'r') as f:
		keys = json.load(f)
	return keys

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

def decrypt_key(encrypted_key, alphabet_map):
	"""Decrypts the key using mono-alphabetic substitution cipher."""

	reverse_map = {}
	for key in alphabet_map:
		reverse_map[alphabet_map[key]] = key
	key = []
	for char in encrypted_key:
		key.append(reverse_map[char])
	return ''.join(key)

def encrypt_message(plaintext):
	"""Encrypts the plaintext."""

	plaintext_len = len(plaintext)
	keys = get_keys()
	vigenere_key = decrypt_key(keys['encrypted_key'], keys['map'])
	ciphertext = vigenere_encryption(plaintext, vigenere_key)

	return ciphertext

if __name__ == '__main__':

	plaintext = take_input()
	ciphertext = encrypt_message(plaintext)
	print("Encrypted message is {}".format(repr(ciphertext)))
