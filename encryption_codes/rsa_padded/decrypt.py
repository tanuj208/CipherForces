from helper import *
from padding import *
from generate_keys import gen_keys
from encrypt import encrypt

def decrypt(cipher, keys):
	public_key, private_key = keys
	n, _ = public_key
	d = private_key[0]
	en_msg = cipher[0]

	hlen = 20  # SHA-1 hash length
	k = ceil(n.bit_length() / 8)
	assert len(en_msg) == k
	assert k >= 2*hlen + 2

	dr_msg = pow(os2ip(en_msg), d, n)
	dr_msg = i2osp(dr_msg, k)

	dr_msg = oaep_decode(dr_msg, k).decode()
	return dr_msg


if __name__ == '__main__':
	keys = gen_keys(256)
	public_key, private_key = keys
	print(public_key,private_key)
	print("Enter Message to be encoded : ")
	msg = input()

	cipher = encrypt(msg, public_key)
	print(cipher)

	decoded_text = decrypt(cipher, keys)
	print(decoded_text)