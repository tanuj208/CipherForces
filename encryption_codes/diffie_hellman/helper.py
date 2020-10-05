
#TODO: Better conversion methods
def convert_to_num(text):
	"""Converts a text message to a list of numbers (their ascii codes)."""

	nums = []
	for character in text:
		nums.append(ord(character))
	return nums

def convert_to_text(nums):
	"""Converts a list of numbers to characters
	using numbers as their ascii code."""

	text = []
	for num in nums:
		text.append(chr(num))
	return ''.join(text)

