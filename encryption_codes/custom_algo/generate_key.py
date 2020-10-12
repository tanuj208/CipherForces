import random
import string

def take_input():
	print('Enter the number of bits of key required and then press enter: ')
	num_bits = int(input())
	return num_bits

def get_random_text(text_len):
	text = []
	message_space = string.ascii_lowercase
	for _ in range(text_len):
		text.append(random.choice(message_space))
	return ''.join(text)

def random_alphabet_map():
	message_space = string.ascii_lowercase
	message_space = [char for char in message_space]
	random.shuffle(message_space)
	original_message_space = string.ascii_lowercase
	alphabet_map = {}
	for i in range(26):
		alphabet_map[original_message_space[i]] = message_space[i]
	return alphabet_map
