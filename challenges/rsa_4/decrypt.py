from helper import *
from padding import *
from encrypt import encrypt
import json

def get_keys():
	"""Extracts key from json file."""
	with open('keys.json') as f:
		keys = json.load(f)
	return keys

def decrypt(cipher, keys):
	public_key = keys['public_key']
	private_key = keys['private_key']
	n = public_key["n"]
	d = private_key["d"]
	en_msg = cipher

	hlen = 20  # SHA-1 hash length
	k = ceil(n.bit_length() / 8)
	assert len(en_msg) == k
	# assert k >= 2*hlen + 2

	dr_msg = pow(os2ip(en_msg), d, n)
	dr_msg = i2osp(dr_msg, k)

	dr_msg = oaep_decode(dr_msg, k).decode()
	return dr_msg


if __name__ == '__main__':
	keys = get_keys()
	print(keys)
	print("Enter Message to be encoded : ")
	msg = input()

	cipher = encrypt(msg, keys["public_key"])
	print(cipher)

	decoded_text = decrypt(cipher, keys)
	print(decoded_text)