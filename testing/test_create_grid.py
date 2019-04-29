import pytest
from helpers import main_helper

testdata_positive = [
	(2, 3), (4, 1), (15, 15), (1, 1)
]


@pytest.mark.parametrize("a,b", testdata_positive)
def test_positive_create_grid(a, b):
	"""Assert expected sizes for given grid dimensions"""
	main_helper.create_grid(a, b)
	assert len(main_helper.grid_letters[0]) == a
	assert len(main_helper.grid_letters) == b


testdata_negative = [
	(0, 1), (1, 0), (0, 0), (-1, 1)
]


@pytest.mark.parametrize("a,b", testdata_negative)
def test_negative_create_grid(a, b):
	"""Assert expected exception for wrong grid dimensions"""
	with pytest.raises(Exception):
		main_helper.create_grid(a, b)
