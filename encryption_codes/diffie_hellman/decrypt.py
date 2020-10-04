import ast
import random
import shlex

from helper import power, convert_to_text, convert_to_num
from generate_public_key import get_public_key

def take_input():
	"""Takes all necessary inputs for decryption."""

	print("Enter the message to be decrypted and then press enter: ")
	ciphertext = input()
	try:
		ciphertext = ast.literal_eval(shlex.quote(ciphertext))
	except:
		pass
	print("Enter the prime number used to encryption and then press enter: ")
	prime_num = int(input())
	print("Enter the generator used during encryption and then press enter: ")
	generator = int(input())
	print("Enter the public key of the sender and then press enter: ")
	public_key = int(input())
	print("Enter the secret key to use and then press enter: ")
	private_key = int(input())
	return ciphertext, prime_num, generator, public_key, private_key


def decrypt_num(input_num, private_key, public_key, prime_num, generator):
	"""Encrypts a number."""

	super_key = power(public_key, private_key, prime_num)
	encrypted_num = (input_num - super_key + 2 * prime_num) % prime_num
	return encrypted_num


if __name__ == '__main__':

	ciphertext, prime_num, generator, public_key, private_key = take_input()
	own_public_key = get_public_key(private_key, prime_num, generator)
	print("Public key used by this code is {}".format(own_public_key))

	encrypted_nums = convert_to_num(ciphertext)
	nums = []
	for num in encrypted_nums:
		nums.append(decrypt_num(num, private_key, public_key, prime_num, generator))
	decrypted_message = convert_to_text(nums)
	print("Decrypted message is {}".format(repr(decrypted_message)))
