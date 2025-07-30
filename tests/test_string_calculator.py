import pytest
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

def test_custom_single_char_delimiter():
    assert add("//;\n1;2") == 3

def test_negative_number_raises_exception():
    with pytest.raises(Exception) as e:
        add("1,-2,3")
    assert str(e.value) == "negatives not allowed: -2"

def test_multiple_negatives_raise_exception_with_all_values():
    with pytest.raises(Exception) as e:
        add("-1,-2,3")
    assert str(e.value) == "negatives not allowed: -1,-2"

def test_ignore_numbers_greater_than_1000():
    assert add("2,1001,6") == 8