from helpers import main_helper
import sys, cProfile


def words_search(a, b):
	"""Main function to run program"""
	main_helper.create_grid(a, b)
	main_helper.grid_transpose(b)
	main_helper.grid_diagonals()
	main_helper.letters_to_string()
	main_helper.get_all_words()


def execute_with_output(a, b):
	"""Run program with displayed output"""
	words_search(a, b)
	print()
	print(f'Randomly generated letters grid with dimentions of: {a}x{b}')
	for row in main_helper.grid_letters:
		print()
		for letter in row:
			print(letter, end = '     ')
		print()
	print('')
	print(f'Total words found in grid: {len(main_helper.found_words)}')
	print()
	print(f'Words are: {main_helper.found_words}')
	print()


def run_performance():
	"""Profile words_search"""
	cProfile.run('words_search(15, 15)')


if sys.argv[0] == 'words_search_main.py':
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	execute_with_output(a, b)


def user_input():
	"""Run program using user input"""
	global a, b
	while True:
		try:
			print()
			a = int(input('Enter grid width: '))
			b = int(input('Enter grid height: '))
			print()
			if a < 1 or b < 1:
				raise ValueError()
		except ValueError:
			print('========== Oops, value must be a positive integer > 1  ==========')
			print('Please try again')
			continue
		break
	
	execute_with_output(a, b)
