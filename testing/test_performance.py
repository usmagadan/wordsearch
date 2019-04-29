import pytest, datetime, re
from words_search_main import words_search
from helpers import main_helper

testdata = [(15, 15, 0.5)]


@pytest.mark.parametrize("a,b,run", testdata)
def test_performance(a, b, run):
	"""Assert performance for words_search is reasonable"""
	main_helper.words = open('words.txt', 'r').read().splitlines()
	start_time = datetime.datetime.now()
	words_search(a, b)
	end_time = datetime.datetime.now()
	delta = str(end_time - start_time)
	run_time = float(re.search(r'(?<=00:).*', delta).group())
	print(run_time)
	assert run_time < run
