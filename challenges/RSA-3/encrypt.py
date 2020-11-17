from helper import *
import json
import sys

def get_keys():
	"""Extracts key from json file."""
	with open('RSA-3/keys.json') as f:
		keys = json.load(f)
	return keys

# Asymmetric encryption 
def encrypt(msg, public_key): 
	n = public_key["n"]
	e = public_key["e"]

	en_msg = []
	for word in msg.split():
		word = os2ip(word.encode())
		en_msg.append(pow(word,e,n))
	cipher = en_msg
	return cipher

if __name__ == '__main__':

	keys = get_keys()
	msg = sys.argv[1]
	cipher = encrypt(msg, keys["public_key"])
	print(cipher)