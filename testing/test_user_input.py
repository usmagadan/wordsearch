import pytest

testdata = [
	('-2'), ('0'), ('a'), ('%'), ('3')
]


@pytest.mark.parametrize("a", testdata)
def test_user_input(a):
	"""Assert exception raises when incorrect input"""
	input = lambda _: a
	
	if a == '3':
		width = int(input('Enter grid width: '))
		if width < 1:
			raise ValueError()
		assert int(a) == width
	else:
		with pytest.raises(ValueError):
			width = int(input('Enter grid width: '))
			if width < 1:
				raise ValueError()
