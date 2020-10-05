import ast
import json
import random
import shlex

from helper import convert_text_to_binary, convert_binary_to_text, string_xor
from generate_key import get_random_key

def take_input():
	"""Takes all necessary inputs for encryption."""

	print("Enter the message to be encrypted and then press enter: ")
	plaintext = input()
	try:
		plaintext = ast.literal_eval(shlex.quote(plaintext))
	except:
		pass
	return plaintext

def add_key_to_json(keys):
	with open('keys.json', 'w+') as f:
		json.dump(keys, f)

def encrypt_message(plaintext):
	"""Encrypts the plaintext."""

	plaintext_binary = convert_text_to_binary(plaintext)
	block_len = int(len(plaintext_binary)//2)
	left_portion = plaintext_binary[0:block_len]
	right_portion = plaintext_binary[block_len::]
	num_rounds = 2
	keys = {}

	for i in range(num_rounds):
		right_portion_len = len(right_portion)
		random_key = get_random_key(right_portion_len)
		keys['K{}'.format(i + 1)] = random_key
		temp = string_xor(right_portion, random_key)

		new_left_portion = right_portion
		right_portion = string_xor(temp, left_portion)
		left_portion = new_left_portion

	ciphertext = left_portion + right_portion
	add_key_to_json(keys)
	return convert_binary_to_text(ciphertext)

if __name__ == '__main__':

	plaintext = take_input()
	ciphertext = encrypt_message(plaintext)
	print("Encrypted message is {}".format(repr(ciphertext)))
