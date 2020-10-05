from helper import *
from generate_keys import gen_keys
from encrypt import encrypt

def decrypt(cipher, keys):
	public_key, private_key = keys
	n, e = public_key
	d = private_key[0]
	en_msg = cipher[0]
	dr_msg = pow(en_msg, d, n)
	dr_msg = i2osp(dr_msg, n.bit_length() // 8).decode()
	return dr_msg


if __name__ == '__main__':
	keys = gen_keys(128)
	public_key, private_key = keys
	print(public_key,private_key)
	print("Enter Message to be encoded : ")
	msg = input()

	cipher = encrypt(msg, public_key)
	print(cipher)

	decoded_text = decrypt(cipher, keys)
	print(decoded_text)