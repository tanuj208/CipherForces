import ast
import json
import random
import shlex
import sys

from helper import convert_text_to_binary, convert_binary_to_text, string_xor
from generate_key import get_random_key

def take_input():
	"""Takes all necessary inputs for encryption."""

	print("Enter the message to be decrypted and then press enter: ")
	ciphertext = str(input())
	try:
		ciphertext = ast.literal_eval(shlex.quote(ciphertext))
	except:
		pass
	return ciphertext

def get_keys():
	with open('keys.json', 'r') as f:
		keys = json.load(f)
	return keys

def decrypt_message(ciphertext):
	"""Decrypts the ciphertext."""

	ciphertext_binary = convert_text_to_binary(ciphertext)
	block_len = int(len(ciphertext_binary)//2)
	left_portion = ciphertext_binary[0:block_len]
	right_portion = ciphertext_binary[block_len::]
	num_rounds = 2
	keys = get_keys()
	num_keys = len(keys)

	for i in range(num_rounds):
		left_portion_len = len(left_portion)
		random_key = keys['K{}'.format(num_keys - i)]
		temp = string_xor(left_portion, random_key)

		new_right_portion = left_portion
		left_portion = string_xor(temp, right_portion)
		right_portion = new_right_portion

	plaintext = left_portion + right_portion
	return convert_binary_to_text(plaintext)

if __name__ == '__main__':

	ciphertext = take_input()
	plaintext = decrypt_message(ciphertext)
	print("Decrypted message is {}".format(repr(plaintext)))
