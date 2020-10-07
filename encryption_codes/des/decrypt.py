import ast
import json
import random
import shlex

import helper
from generate_key import get_random_key

def take_input():
	"""Takes all necessary inputs for encryption."""

	print("Enter the message to be decrypted and then press enter: ")
	ciphertext = input()
	try:
		ciphertext = ast.literal_eval(shlex.quote(ciphertext))
	except:
		pass
	return ciphertext

def get_key_from_json():
	with open('keys.json', 'r') as f:
		key = json.load(f)
	return key['key']

def pad_with_zeros(plaintext_binary):
	"""Pad with zeros such that the length is divisible by 64."""
	plaintext_len = len(plaintext_binary)
	target_len = 64 * ((plaintext_len-1) // 64 + 1)
	zero_padding = '0'*(target_len - plaintext_len)
	plaintext_binary += zero_padding
	return plaintext_binary

def get_round_keys():
	"""Get 64-bit key for each round."""

	main_key = get_key_from_json()
	key_perm = [57, 49, 41, 33, 25, 17, 9,
					1, 58, 50, 42, 34, 26, 18,
					10, 2, 59, 51, 43, 35, 27,
					19, 11, 3, 60, 52, 44, 36,
					63, 55, 47, 39, 31, 23, 15,
					7, 62, 54, 46, 38, 30, 22,
					14, 6, 61, 53, 45, 37, 29,
					21, 13, 5, 28, 20, 12, 4]
	key_compression = [14, 17, 11, 24, 1, 5,
						3, 28, 15, 6, 21, 10,
						23, 19, 12, 4, 26, 8,
						16, 7, 27, 20, 13, 2,
						41, 52, 31, 37, 47, 55,
						30, 40, 51, 45, 33, 48,
						44, 49, 39, 56, 34, 53,
						46, 42, 50, 36, 29, 32]
	main_key = helper.permute(main_key, key_perm) # get 56-bit key
	left_key = main_key[:28]
	right_key = main_key[28:]
	round_keys = []

	for i in range(16):
		shift_amount = 2
		if i < 2 or i == 8 or i == 15:
			shift_amount = 1
		left_key = helper.circular_left_shift(left_key, shift_amount)
		right_key = helper.circular_left_shift(right_key, shift_amount)
		full_key = left_key + right_key
		round_keys.append(helper.permute(full_key, key_compression)) # get 48-bit subkey
	return round_keys[::-1]

def perform_initial_perm(message):
	perm = [
		58, 50, 42, 34, 26, 18, 10, 2,
		60, 52, 44, 36, 28, 20, 12, 4,
		62, 54, 46, 38, 30, 22, 14, 6,
		64, 56, 48, 40, 32, 24, 16, 8,
		57, 49, 41, 33, 25, 17, 9, 1,
		59, 51, 43, 35, 27, 19, 11, 3,
		61, 53, 45, 37, 29, 21, 13, 5,
		63, 55, 47, 39, 31, 23, 15, 7
	]
	message = helper.permute(message, perm)
	return message

def expand_to_48_bits(message):
	perm = [
		32, 1, 2, 3, 4, 5, 4, 5,
		6, 7, 8, 9, 8, 9, 10, 11,
		12, 13, 12, 13, 14, 15, 16, 17,
		16, 17, 18, 19, 20, 21, 20, 21,
		22, 23, 24, 25, 24, 25, 26, 27,
		28, 29, 28, 29, 30, 31, 32, 1
	]
	message = helper.permute(message, perm)
	return message

def reduce_to_32_bits(message):
	perm = [
		[
			[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
			[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
			[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
			[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
		],
		[
			[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
			[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
			[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
			[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
		],
		[
			[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
			[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
			[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
			[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
		],
		[
			[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
			[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
			[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
			[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
		],
		[
			[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
			[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
			[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
			[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
		],
		[
			[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
			[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
			[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
			[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
		],
		[
			[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
			[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
			[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
			[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
		],
		[
			[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
			[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
			[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
			[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
		]
	]
	op = []
	for i in range(8):
		row = 2 * int(message[i * 6]) + int(message[i * 6 + 5])
		col = 8 * int(message[i * 6 + 1]) + 4 * int(message[i * 6 + 2]) + 2 * int(message[i * 6 + 3]) + int(message[i * 6 + 4])
		val = perm[i][row][col]
		op.append(str(val // 8))
		val %= 8
		op.append(str(val // 4))
		val %= 4
		op.append(str(val // 2))
		val %= 2
		op.append(str(val))
	return ''.join(op)

def straight_perm(message):
	perm = [
		16, 7, 20, 21, 
		29, 12, 28, 17, 
		1, 15, 23, 26, 
		5, 18, 31, 10, 
		2, 8, 24, 14, 
		32, 27, 3, 9, 
		19, 13, 30, 6, 
		22, 11, 4, 25
	]
	message = helper.permute(message, perm)
	return message

def round_operation(left_message, right_message, swap, round_key):
	right_expanded = expand_to_48_bits(right_message)
	temp_message = helper.string_xor(right_expanded, round_key)
	temp_message = reduce_to_32_bits(temp_message)
	temp_message = straight_perm(temp_message)
	left_message = helper.string_xor(temp_message, left_message)
	if swap:
		return right_message, left_message
	return left_message, right_message

def final_perm(message):
	perm = [
		40, 8, 48, 16, 56, 24, 64, 32,
		39, 7, 47, 15, 55, 23, 63, 31,
		38, 6, 46, 14, 54, 22, 62, 30,
		37, 5, 45, 13, 53, 21, 61, 29,
		36, 4, 44, 12, 52, 20, 60, 28,
		35, 3, 43, 11, 51, 19, 59, 27,
		34, 2, 42, 10, 50, 18, 58, 26,
		33, 1, 41, 9, 49, 17, 57, 25
	]
	message = helper.permute(message, perm)
	return message

def decrypt_block(block):
	"""Encrypts 64 bit plaintext (binary form)"""
	round_keys = get_round_keys()
	block = perform_initial_perm(block)
	left_block = block[:32]
	right_block = block[32:]

	for i in range(16):
		swap = True
		round_key = round_keys[i]
		if i == 15:
			swap = False
		left_block, right_block = round_operation(left_block, right_block, swap, round_key)
	decrypted_block = left_block + right_block
	return final_perm(decrypted_block)

def remove_padding_chars(message):
	idx = len(message) - 1
	while idx >= 0 and message[idx] == '\x00':
		idx -= 1
	return message[:idx + 1]

def decrypt_message(ciphertext):
	"""Decrypts the ciphertext."""

	ciphertext_binary = helper.convert_text_to_binary(ciphertext)
	ciphertext_binary = pad_with_zeros(ciphertext_binary)
	ciphertext_len = len(ciphertext_binary)
	plaintext_binary = []

	for i in range(0, ciphertext_len, 64):
		block = ciphertext_binary[i : i + 64]
		decrypted_block = decrypt_block(block)
		plaintext_binary.append(decrypted_block)

	plaintext_binary = ''.join(plaintext_binary)
	plaintext = helper.convert_binary_to_text(plaintext_binary)
	plaintext = remove_padding_chars(plaintext)
	return plaintext

if __name__ == '__main__':
	ciphertext = take_input()
	plaintext = decrypt_message(ciphertext)
	print("Decrypted message is {}".format(repr(plaintext)))
