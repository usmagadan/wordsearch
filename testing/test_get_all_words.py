import pytest
from helpers import main_helper

testdata = [
	(
		{'ntblj', 'gorq', 'diqrv'},
		['mbvntbljlqdwcpt', 'wabpwauqfomsnel', 'idnpwqlikwlqauz', 'mzbufxcqtzbqzcu'],
	    ['mwimjgorqfygtvc', 'badzljwcuxactgm', 'vbnbqhipjilvhye', 'nppuqervyjenpfh'],
	    ['manuxzjdiqrvqwh', 'bbpfvphlqpvyia', 'vpwxtebxcwcni', 'nwqcanrghtiu']
	)
]


@pytest.mark.parametrize("words,grid,transpose,diagonals", testdata)
def test_get_all_words(words, grid, transpose, diagonals):
	"""Assert all words from given collection found in grid"""
	main_helper.words = words
	main_helper.grid_strings = grid
	main_helper.transpose_strings = transpose
	main_helper.diagonals_strings = diagonals
	main_helper.get_all_words()
	assert main_helper.found_words == words
