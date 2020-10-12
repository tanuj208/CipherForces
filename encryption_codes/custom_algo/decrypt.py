import json
import sys

import generate_key

def take_input():
	"""Takes all necessary inputs for encryption."""

	print("Enter the message to be decrypted and then press enter: ")
	ciphertext = str(input())
	return ciphertext

def get_keys():
	with open('keys.json', 'r') as f:
		keys = json.load(f)
	return keys

def get_vigenere_key(encrypted_key, alphabet_map):
	"""Decrypts the key using mono-alphabetic substitution cipher."""

	reverse_map = {}
	for key in alphabet_map:
		reverse_map[alphabet_map[key]] = key
	key = []
	for char in encrypted_key:
		key.append(reverse_map[char])
	return ''.join(key)

def vigenere_decryption(ciphertext, key):
	"""Decrypts the ciphertext using vigenere cipher."""

	plaintext = []
	for i in range(len(key)):
		p = ord(ciphertext[i])
		k = ord(key[i])
		min_val = ord('a')
		p -= min_val
		k -= min_val
		p -= k + 26
		p %= 26
		p += min_val
		plaintext.append(chr(p))
	return ''.join(plaintext)

def decrypt_message(ciphertext):
	"""Decrypts the ciphertext."""
	keys = get_keys()
	encrypted_key = keys['encrypted_key']
	alphabet_map = keys['map']
	vigenere_key = get_vigenere_key(encrypted_key, alphabet_map)
	plaintext = vigenere_decryption(ciphertext, vigenere_key)
	return plaintext

if __name__ == '__main__':

	ciphertext = take_input()
	plaintext = decrypt_message(ciphertext)
	print("Decrypted message is {}".format(repr(plaintext)))
