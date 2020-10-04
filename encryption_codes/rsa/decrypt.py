from helper import *
from generate_keys import gen_keys
from encrypt import encrypt

def decrypt(cipher, keys):
	public_key, private_key = keys
	n, e = public_key
	d = private_key[0]
	en_msg = cipher[0]

	dr_msg = []
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(power(en_msg[i], d, n)))

	# dr_msg = power(en_msg, d, n)
	return dr_msg 


if __name__ == '__main__':
	keys = gen_keys(16)
	public_key, private_key = keys
	print(public_key,private_key)
	print("Enter Message to be encoded : ")
	msg = input()
	# msg = int(input())

	cipher = encrypt(msg, public_key)
	print(cipher)

	decoded_text = decrypt(cipher, keys)
	print(decoded_text)