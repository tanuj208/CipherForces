from helper import *
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
	e = public_key["e"]
	d = private_key["d"]
	en_msg = cipher

	dr_msg = []
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(power(en_msg[i], d, n)))

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