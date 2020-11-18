import random
import string
import json

def random_alphabet_map():
	message_space = string.ascii_letters
	message_space = [char for char in message_space]
	random.shuffle(message_space)
	original_message_space = string.ascii_letters
	alphabet_map = {}
	for i in range(len(original_message_space)):
		alphabet_map[original_message_space[i]] = message_space[i]
	return alphabet_map

if __name__ == '__main__':
	alphabet_map = random_alphabet_map()
	with open('keys.json', 'w+') as f:
		json.dump(alphabet_map, f)
