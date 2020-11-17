from helper import *
import json

def get_keys():
	"""Extracts key from json file."""
	with open('keys.json') as f:
		keys = json.load(f)
	return keys

# Asymmetric encryption 
def encrypt(msg, public_key): 
	n = public_key["n"]
	e = public_key["e"]

	en_msg = []
	for i in range(0, len(msg)): 
		en_msg.append(msg[i]) 
	for i in range(0, len(en_msg)):
		en_msg[i] = power(ord(en_msg[i]), e, n)

	cipher = en_msg
	return cipher


if __name__ == '__main__':

	keys = get_keys()
	print(keys["public_key"])
	print("Enter Message to be encoded : ")
	msg = input()

	cipher = encrypt(msg, keys["public_key"])
	print(cipher)