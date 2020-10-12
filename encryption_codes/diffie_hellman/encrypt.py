import ast
import json
import random
import shlex

import helper

def take_input():
	"""Takes all necessary inputs for encryption."""

	print("Enter the message to be encrypted and then press enter: ")
	plaintext = input()
	try:
		plaintext = ast.literal_eval(shlex.quote(plaintext))
	except:
		pass
	return plaintext

def get_keys():
	"""Extracts key from json file."""

	with open('keys.json') as f:
		keys = json.load(f)
	return keys

def encrypt_num(input_num):
	"""Encrypts a number."""

	keys = get_keys()
	receiver_public_key = keys['receiver_public_key']
	private_key = keys['sender_secret_key']
	prime_num = keys['prime_number']
	super_key = pow(receiver_public_key, private_key, prime_num)
	encrypted_num = (input_num + super_key) % prime_num
	return encrypted_num


if __name__ == '__main__':

	plaintext = take_input()
	plaintext_binary = helper.convert_text_to_binary(plaintext)
	plaintext_num = int(plaintext_binary, 2)
	encrypted_num = encrypt_num(plaintext_num)
	bit_len = encrypted_num.bit_length()
	if bit_len % 8 != 0:
		bit_len = (bit_len // 8 + 1) * 8
	encrypted_binary = format(encrypted_num, '0{}b'.format(bit_len))
	encrypted_message = helper.convert_binary_to_text(encrypted_binary)
	print("Encrypted message is {}".format(repr(encrypted_message)))
