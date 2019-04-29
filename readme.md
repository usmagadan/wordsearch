To run program using CLI args:
    
    python words_search_main.py a b
where `a` and `b` are dimensions of a grid of letters

`OR`

To run program using user input:
    
    python run.py
___
To profile main program:

    python -c 'from words_search_main import *; run_performance()'
___
For tests:

    pip install -U pytest

___
To run a specific test within a module:

    python -m pytest testing/test_create_grid.py::test_negative_create_grid
___  
Run tests in a directory:

    python -m pytest testing/
---
Dry run and quiet modes:

    python -m pytest tests.py --collect-only
    python -m pytest tests.py -q