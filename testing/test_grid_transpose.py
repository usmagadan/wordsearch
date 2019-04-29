import pytest
from helpers import main_helper

testdata = [
	(2, 3), (4, 1), (15, 15)
]


@pytest.mark.parametrize("a,b", testdata)
def test_grid_transpose(a, b):
	"""Assert created grid transpose correctly"""
	main_helper.create_grid(a, b)
	main_helper.grid_transpose(b)
	assert len(main_helper.grid_letters[0]) == len(main_helper.transpose_letters)
	assert len(main_helper.grid_letters) == len(main_helper.transpose_letters[0])
