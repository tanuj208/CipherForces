import sys

sys.path.append('..')

from helper import power

def take_input():
	print("Enter the secret key and then press enter: ")
	secret_key = int(input())
	print("Enter the prime number to use and then press enter: ")
	prime_num = int(input())
	print("Enter the generator to use and then press enter: ")
	generator = int(input())
	return secret_key, prime_num, generator

def get_public_key(secret_key, prime_num, generator):
	public_key = power(generator, secret_key, prime_num)
	return public_key

if __name__ == '__main__':
	secret_key, prime_num, generator = take_input()
	public_key = get_public_key(secret_key, prime_num, generator)
	print("Public key is {}".format(public_key))
