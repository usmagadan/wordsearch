import pytest
from helpers import main_helper

testdata = [
	([['a', 'v', 'd'], ['c', 'e', 'f']],
	 [['a', 'e'], ['v', 'f'], ['d', 'e'], ['v', 'c']]),
	
	([['a', 'v', 'd'], ['c', 'e', 'f'], ['g', 'h', 'x'], ['q', 'w', 'l']],
	 [['a', 'e', 'x'], ['v', 'f'], ['d', 'e', 'g'], ['v', 'c'], ['c', 'h', 'l'], ['g', 'w'], ['f', 'h', 'q'], ['x', 'w']]),
	
	([['a', 'v', 'd'], ['c', 'e', 'f'], ['g', 'h', 'x']],
	 [['a', 'e', 'x'], ['v', 'f'], ['d', 'e', 'g'], ['v', 'c'], ['c', 'h'], ['f', 'h']])
]


@pytest.mark.parametrize("grid, diagonals", testdata)
def test_grid_diagonals(grid, diagonals):
	"""Assert all diagonals from grid fetched"""
	main_helper.grid_letters = grid
	main_helper.grid_diagonals()
	assert main_helper.diagonals_letters == diagonals
