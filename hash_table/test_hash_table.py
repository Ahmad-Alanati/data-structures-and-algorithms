from hash_table import HashTable
import pytest

def test_hash_table_one():
    hash_table = HashTable()
    hash_table.set(1,"hello")
    actual =  hash_table.get(1)
    expected = "hello"
    assert actual == expected

def test_hash_table_two():
    hash_table = HashTable()
    hash_table.set(1,'hello')
    hash_table.set('1','hello world')
    hash_table.set(12,'ahmad')
    hash_table.set(15,'mohammad')
    actual =  hash_table.get(15)
    expected = "mohammad"
    assert actual == expected

def test_hash_table_three():
    hash_table = HashTable()
    hash_table.set(1,'hello')
    hash_table.set('1','hello world')
    hash_table.set(12,'ahmad')
    hash_table.set(15,'mohammad')
    actual =  hash_table.get('15')
    expected = "null"
    assert actual == expected

def test_hash_table_four():
    hash_table = HashTable()
    hash_table.set(1,'hello')
    hash_table.set('1','hello world')
    hash_table.set(12,'ahmad')
    hash_table.set(15,'mohammad')
    actual =  hash_table.get_keys()
    expected = [1, '1', 12, 15]
    assert actual == expected

def test_hash_table_five():
    hash_table = HashTable()
    hash_table.set(1,'hello')
    hash_table.set('1','hello world')
    hash_table.set(12,'ahmad')
    hash_table.set(15,'mohammad')
    actual =  str(hash_table.get(1))
    expected = "hello"
    assert actual == expected
