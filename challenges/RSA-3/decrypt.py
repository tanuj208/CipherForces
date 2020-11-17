from helper import *
from encrypt import encrypt
import json

def get_keys():
	"""Extracts key from json file."""
	with open('RSA-3/keys.json') as f:
		keys = json.load(f)
	return keys

def decrypt(cipher, keys):
	public_key = keys['public_key']
	private_key = keys['private_key']
	n = public_key["n"]
	e = public_key["e"]
	d = private_key["d"]
	en_msg = cipher

	dr_msg = []
	for word in en_msg:
		dr_word = pow(word, d, n)
		dr_word = i2osp(dr_word, n.bit_length() // 8).decode()
		dr_msg.append(dr_word)

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