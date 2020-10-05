from helper import *
from padding import *
from generate_keys import gen_keys

# Asymmetric encryption 
def encrypt(msg, public_key): 
	n, e = public_key
	msg = msg.encode()

	hlen = 20  # SHA-1 hash length
	k = ceil(n.bit_length() / 8)
	assert len(msg) <= k - hlen - 2

	pd_msg = oaep_encode(msg, k)
	pd_msg = os2ip(pd_msg)
	en_msg = pow(pd_msg, e, n)

	cipher = [i2osp(en_msg, k)]
	return cipher

if __name__ == '__main__':

	public_key, private_key = gen_keys(512)
	print(public_key)
	print("Enter Message to be encoded : ")
	msg = input()
	# msg = int(input())

	cipher = encrypt(msg, public_key)
	print(cipher)