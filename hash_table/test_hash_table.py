import pytest
from hash_table import HashTable,repeated_word

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


def test_hash_table_six():
    text = "Once upon a time, there was a brave princess who..."
    actual =  repeated_word(text)
    expected = "a"
    assert actual == expected

def test_hash_table_seven():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual =  repeated_word(text)
    expected = "it"
    assert actual == expected

def test_hash_table_eight():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual =  repeated_word(text)
    expected = "summer"
    assert actual == expected