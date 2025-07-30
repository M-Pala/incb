from src.string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number():
    assert add("5") == 5

def test_two_number():
    assert add("5,6") == 11
    
def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_newline_and_commas_as_delimiters():
    assert add("1\n2,3") == 6