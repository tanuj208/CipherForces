from helper import *
from generate_keys import gen_keys

# Asymmetric encryption 
def encrypt(msg, public_key): 
	n, e = public_key
	# en_msg = power(msg, e, n)

	en_msg = []
	for i in range(0, len(msg)): 
		en_msg.append(msg[i]) 
	for i in range(0, len(en_msg)): 
		en_msg[i] = power(ord(en_msg[i]), e, n)

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