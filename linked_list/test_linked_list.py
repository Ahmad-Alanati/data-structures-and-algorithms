from linked_list import Node,LinkedList

def test_linked_list_one():
    test_linked_list = LinkedList()
    actual = str(test_linked_list)
    expected = "there is no element in the list"
    assert actual == expected

def test_linked_list_two():
    test_linked_list = LinkedList()
    test_linked_list.insert(1)
    test_linked_list.insert(2)
    test_linked_list.insert(3)
    actual = str(test_linked_list)
    expected = "{ 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected

def test_linked_list_three():
    test_linked_list = LinkedList()
    test_linked_list.insert(1)
    test_linked_list.insert(2)
    test_linked_list.insert(3)
    actual = test_linked_list.includes(5)
    expected = False
    assert actual == expected

def test_linked_list_four():
    test_linked_list = LinkedList()
    test_linked_list.insert(1)
    test_linked_list.insert(2)
    test_linked_list.insert(3)
    actual = test_linked_list.includes(1)
    expected = True
    assert actual == expected

def test_linked_list_five():
    test_linked_list = LinkedList()
    linked_list2 = LinkedList()
    linked_list2.insert(7)
    linked_list2.insert(8)
    linked_list2.insert(9)
    test_linked_list.insert(linked_list2.head)
    actual = str(test_linked_list)
    expected = "{ 9 } -> { 8 } -> { 7 } -> NULL"
    assert actual == expected

