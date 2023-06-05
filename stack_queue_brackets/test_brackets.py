import pytest
from brackets import validate_brackets

def test_brackets_one():
    _str = "{}"
    actual = validate_brackets(_str)
    expected = True
    assert actual == expected

def test_brackets_two():
    _str = "{}(){}"
    actual = validate_brackets(_str)
    expected = True
    assert actual == expected

def test_brackets_three():
    _str = "()[[Extra Characters]]"
    actual = validate_brackets(_str)
    expected = True
    assert actual == expected

def test_brackets_four():
    _str = "(){}[[]]"
    actual = validate_brackets(_str)
    expected = True
    assert actual == expected

def test_brackets_five():
    _str = "{}{Code}[Fellows](())"
    actual = validate_brackets(_str)
    expected = True
    assert actual == expected

def test_brackets_six():
    _str = "[({}]"
    actual = validate_brackets(_str)
    expected = False
    assert actual == expected

def test_brackets_seven():
    _str = "(]("
    actual = validate_brackets(_str)
    expected = False
    assert actual == expected

def test_brackets_eight():
    _str = "{(})"
    actual = validate_brackets(_str)
    expected = False
    assert actual == expected

def test_brackets_nine():
    _str = "{"
    actual = validate_brackets(_str)
    expected = False
    assert actual == expected

def test_brackets_ten():
    _str = ")"
    actual = validate_brackets(_str)
    expected = False
    assert actual == expected

def test_brackets_eleven():
    _str = "[}"
    actual = validate_brackets(_str)
    expected = False
    assert actual == expected