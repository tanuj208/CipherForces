import ast
import json
import random
import shlex

from helper import convert_to_text, convert_to_num

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
	nums = convert_to_num(plaintext)
	encrypted_nums = []
	for num in nums:
		encrypted_nums.append(encrypt_num(num))
	encrypted_message = convert_to_text(encrypted_nums)
	print("Encrypted message is {}".format(repr(encrypted_message)))
