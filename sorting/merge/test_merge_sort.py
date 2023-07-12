import pytest
from merge_sort import merge_sort


def test_insertion_sort_one():
    array = [8,4,23,42,16,15]
    actual = merge_sort(array)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_insertion_sort_two():
    array = [20, 18, 12, 8, 5, -2]
    actual = merge_sort(array)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_insertion_sort_three():
    array = [5, 12, 7, 5, 5, 7]
    actual = merge_sort(array)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_insertion_sort_four():
    array = [2, 3, 5, 7, 13, 11]
    actual = merge_sort(array)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
