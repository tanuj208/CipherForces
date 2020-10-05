import ast
import json
import random
import shlex

from helper import convert_to_text, convert_to_num

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
	encrypted_nums = convert_to_num(ciphertext)
	nums = []
	for num in encrypted_nums:
		nums.append(decrypt_num(num))
	decrypted_message = convert_to_text(nums)
	print("Decrypted message is {}".format(repr(decrypted_message)))
