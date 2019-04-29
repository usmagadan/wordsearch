import random, string, itertools

# English words searched in a grid
words = open('words.txt', 'r').read().splitlines()
# All low case letters from English alphabet
letters = string.ascii_lowercase
found_words = set()


def create_grid(a, b):
	"""Create grid of letters with a x b dimensions"""
	if a < 1 or b < 1: raise Exception('Dimensions of grid can\'t be less than 1')
	global grid_letters
	grid_letters = [list(map(lambda let: random.choice(letters), range(a))) for _ in itertools.repeat(object, b)]


def grid_transpose(b):
	"""Transpose grid"""
	global transpose_letters
	transpose_letters = [row[i] for i in range(len(grid_letters[0])) for row in grid_letters]
	transpose_letters = [transpose_letters[x:x + b] for x in range(0, len(transpose_letters), b)]


def grid_diagonals():
	"""Get all diagonals combinations of letters from grid"""
	global diagonals_letters
	diagonals_letters = []
	for i in range(0, len(grid_letters[0]) - 1):
		temp = []
		for j in range(len(grid_letters)):
			if i + j == len(grid_letters[0]): break
			temp.append(grid_letters[j][i + j])
		diagonals_letters.append(temp)
	
	for i in range(-1, -(len(grid_letters[0])), -1):
		temp = []
		for j in range(len(grid_letters)):
			if i - j < -len(grid_letters[0]): break
			temp.append(grid_letters[j][i - j])
		diagonals_letters.append(temp)
	
	for i in range(1, len(grid_letters) - 1):
		temp = []
		for j in range(len(grid_letters)):
			if j == len(grid_letters) - i or j == len(grid_letters[0]): break
			temp.append(grid_letters[j + i][j])
		diagonals_letters.append(temp)
	
	for i in range(-1, -(len(grid_letters) - 1), -1):
		temp = []
		for j in range(len(grid_letters)):
			if j == len(grid_letters) + i or j == len(grid_letters[0]): break
			temp.append(grid_letters[j - i][-1 - j])
		diagonals_letters.append(temp)


def letters_to_string():
	"""Convert each row of letters into string"""
	global grid_strings
	global transpose_strings
	global diagonals_strings
	grid_strings = [''.join(row) for row in grid_letters]
	transpose_strings = [''.join(row) for row in transpose_letters]
	diagonals_strings = [''.join(row) for row in diagonals_letters]


def get_all_words():
	"""Find all words from given collection in grid"""
	for word in words:
		for grid_string in grid_strings:
			if word in grid_string or word in grid_string[::-1]: found_words.add(word)
		for transpose_string in transpose_strings:
			if word in transpose_string or word in transpose_string[::-1]: found_words.add(word)
		for diagonals_string in diagonals_strings:
			if word in diagonals_string: found_words.add(word)
