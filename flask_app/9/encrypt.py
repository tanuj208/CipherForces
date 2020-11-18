from helper import *
from padding import *
import json
import sys

def get_keys():
	"""Extracts key from json file."""
	with open('keys.json') as f:
		keys = json.load(f)
	return keys

# Asymmetric encryption 
def encrypt(msg, public_key): 
	n = public_key["n"]
	e = public_key["e"]

	msg = msg.encode()

	hlen = 20  # SHA-1 hash length
	k = ceil(n.bit_length() / 8)
	assert len(msg) <= k - hlen - 2

	pd_msg = oaep_encode(msg, k)
	pd_msg = os2ip(pd_msg)
	en_msg = pow(pd_msg, e, n)

	cipher = i2osp(en_msg, k)
	return cipher

if __name__ == '__main__':

	keys = get_keys()
	msg = sys.argv[1]

	cipher = encrypt(msg, keys["public_key"])
	print(cipher)
