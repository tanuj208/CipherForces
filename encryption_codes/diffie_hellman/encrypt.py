import ast
import random
import shlex

from helper import power, convert_to_text, convert_to_num
from generate_public_key import get_public_key

def take_input():
	"""Takes all necessary inputs for encryption."""

	print("Enter the message to be encrypted and then press enter: ")
	plaintext = input()
	try:
		plaintext = ast.literal_eval(shlex.quote(plaintext))
	except:
		pass
	print("Enter the prime number to use and then press enter: ")
	prime_num = int(input())
	print("Enter the generator to use and then press enter: ")
	generator = int(input())
	print("Enter the public key of the recipient and then press enter: ")
	public_key = int(input())
	print("Enter the secret key to use and then press enter: ")
	private_key = int(input())
	return plaintext, prime_num, generator, public_key, private_key


def encrypt_num(input_num, private_key, public_key, prime_num, generator):
	"""Encrypts a number."""

	super_key = power(public_key, private_key, prime_num)
	encrypted_num = (input_num + super_key) % prime_num
	return encrypted_num


if __name__ == '__main__':

	plaintext, prime_num, generator, public_key, private_key = take_input()
	own_public_key = get_public_key(private_key, prime_num, generator)
	print("Public key used by this code is {}".format(own_public_key))

	nums = convert_to_num(plaintext)
	encrypted_nums = []
	for num in nums:
		encrypted_nums.append(encrypt_num(num, private_key, public_key, prime_num, generator))
	encrypted_message = convert_to_text(encrypted_nums)
	print("Encrypted message is {}".format(repr(encrypted_message)))
