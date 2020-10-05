from helper import *
from generate_keys import gen_keys

# Asymmetric encryption 
def encrypt(msg, public_key): 
	n, e = public_key
	msg = os2ip(msg.encode())
	en_msg = pow(msg, e, n)
	cipher = [en_msg]
	return cipher

if __name__ == '__main__':

	public_key, private_key = gen_keys()
	print(public_key)
	print("Enter Message to be encoded : ")
	msg = input()
	# msg = int(input())

	cipher = encrypt(msg, public_key)
	print(cipher)