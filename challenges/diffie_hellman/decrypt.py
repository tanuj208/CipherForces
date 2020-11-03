import ast
import json
import random
import shlex

import helper

def take_input():
	"""Takes all necessary inputs for decryption."""

	print("Enter the message to be decrypted and then press enter: ")
	ciphertext = input()
	try:
		ciphertext = ast.literal_eval(shlex.quote(ciphertext))
	except:
		pass
	return ciphertext

def get_keys():
	"""Extracts key from json file."""

	with open('keys.json') as f:
		keys = json.load(f)
	return keys

def decrypt_num(input_num):
	"""Decrypts a number."""

	keys = get_keys()
	sender_public_key = keys['sender_public_key']
	private_key = keys['receiver_secret_key']
	prime_num = keys['prime_number']
	super_key = pow(sender_public_key, private_key, prime_num)
	decrypted_num = (input_num - super_key + 2 * prime_num) % prime_num
	return decrypted_num


if __name__ == '__main__':

	ciphertext = take_input()
	encrypted_binary = helper.convert_text_to_binary(ciphertext)
	encrypted_num = int(encrypted_binary, 2)
	decrypted_num = decrypt_num(encrypted_num)
	bit_len = decrypted_num.bit_length()
	if bit_len % 8 != 0:
		bit_len = (bit_len // 8 + 1) * 8
	decrypted_binary = format(decrypted_num, '0{}b'.format(bit_len))
	decrypted_message = helper.convert_binary_to_text(decrypted_binary)
	print("Decrypted message is {}".format(repr(decrypted_message)))
