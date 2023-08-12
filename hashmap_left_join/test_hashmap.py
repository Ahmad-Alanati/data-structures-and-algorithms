import pytest
from hashmap import HashTable,left_join

hashmap1 = HashTable()
hashmap2 = HashTable()
hashmap3 = HashTable()

hashmap1.set("diligent","employed")
hashmap1.set("font","enamored")
hashmap1.set("guide","usher")
hashmap1.set("outfit","garb")
hashmap1.set("wrath","anger")

hashmap2.set("diligent","idle")
hashmap2.set("font","averse")
hashmap2.set("guide","follow")
hashmap2.set("flow","jam")
hashmap2.set("wrath","delight")

def test_hashmap_one():
    actual =  left_join(hashmap1,hashmap2)
    expected = [['diligent', 'employed', 'idle'], ['font', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outfit', 'garb', None], ['wrath', 'anger', 'delight']]
    assert actual == expected

def test_hashmap_two():
    actual =  left_join(hashmap3,hashmap2)
    expected = []
    assert actual == expected

def test_hashmap_three():
    actual =  left_join(hashmap1,hashmap3)
    expected = [['diligent', 'employed', None], ['font', 'enamored', None], ['guide', 'usher', None], ['outfit', 'garb', None], ['wrath', 'anger', None]]
    assert actual == expected

