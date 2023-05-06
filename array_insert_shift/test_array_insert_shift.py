import pytest
from array_insert_shift import insertShiftArray
from array_insert_shift import remove_middle_element

# array insert shift tests

def test_array_insert_shift_one():
    arr =[2,4,6,-8]
    element = 5
    actual = insertShiftArray(arr,element)
    expected = [2,4,5,6,-8]
    assert actual == expected

def test_array_insert_shift_two():
    arr =[42,8,15,23,42]
    element = 16
    actual = insertShiftArray(arr,element)
    expected = [42,8,15,16,23,42]
    assert actual == expected

def test_array_insert_shift_three():
    arr =[1]
    element = 2
    actual = insertShiftArray(arr,element)
    expected = [1,2]
    assert actual == expected

# array insert shift tests

def test_remove_middle_element_one():
    arr =[2,4,6,-8]
    actual = remove_middle_element(arr)
    expected = [2,-8]
    assert actual == expected

def test_remove_middle_element_two():
    arr =[42,8,15,23,42]
    actual = remove_middle_element(arr)
    expected = [42,8,23,42]
    assert actual == expected

def test_remove_middle_element_three():
    arr =[1]
    actual = remove_middle_element(arr)
    expected = []
    assert actual == expected
