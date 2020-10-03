from helper import *
from generate_keys import gen_keys
from encrypt import encrypt

def decrypt(cipher, keys):
	public_key, private_key = keys
	h,q,g = public_key
	a = private_key[0]
	p, en_msg = cipher

	dr_msg = []
	h = power(p, a, q)
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(int(en_msg[i]/h)))
	return dr_msg 


if __name__ == '__main__':
	keys = gen_keys()
	public_key, private_key = keys
	print("Enter Message to be encoded : ")
	msg = input()

	cipher = encrypt(msg, public_key)
	print(cipher)

	decoded_text = decrypt(cipher, keys)
	print(decoded_text)