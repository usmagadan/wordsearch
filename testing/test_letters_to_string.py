from helpers import main_helper


def test_letters_to_string():
	"""Assert all letters collections converts into strings correctly"""
	a = 15; b = 15
	main_helper.create_grid(a, b)
	main_helper.grid_transpose(b)
	main_helper.grid_diagonals()
	main_helper.letters_to_string()
	assert len(main_helper.grid_letters) == len(main_helper.grid_strings)
	assert type(main_helper.grid_strings[0]) == str
	assert len(main_helper.transpose_letters) == len(main_helper.transpose_strings)
	assert type(main_helper.transpose_strings[0]) == str
	assert len(main_helper.diagonals_letters) == len(main_helper.diagonals_strings)
	assert type(main_helper.diagonals_strings[0]) == str
