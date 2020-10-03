from helper import *
from generate_keys import gen_keys

# Asymmetric encryption 
def encrypt(msg, public_key): 
	h,q,g = public_key
	k = rand_coprime_with(q)# Private key for sender 
	s = power(h, k, q)

	en_msg = []
	for i in range(0, len(msg)): 
		en_msg.append(msg[i]) 
	for i in range(0, len(en_msg)): 
		en_msg[i] = s * ord(en_msg[i]) 

	p = power(g, k, q)
	cipher = [p, en_msg]
	return cipher


if __name__ == '__main__':

	public_key, private_key = gen_keys()
	print("Enter Message to be encoded : ")
	msg = input()

	cipher = encrypt(msg, public_key)
	print(cipher)