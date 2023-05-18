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

def test_linked_list_six():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(2)
    test_linked_list.append(3)
    actual = str(test_linked_list)
    expected = "{ 1 } -> { 2 } -> { 3 } -> NULL"
    assert actual == expected

def test_linked_list_seven():
    test_linked_list = LinkedList()
    new_node = Node(6)
    new_node2 = Node(5,new_node)
    new_node3 = Node(4,new_node2)
    test_linked_list.append(new_node3)
    actual = str(test_linked_list)
    expected = "{ 4 } -> { 5 } -> { 6 } -> NULL"
    assert actual == expected

def test_linked_list_eight():
    test_linked_list = LinkedList()
    linked_list2 = LinkedList()
    linked_list2.append(7)
    linked_list2.append(8)
    linked_list2.append(9)
    test_linked_list.insert(linked_list2.head)
    actual = str(test_linked_list)
    expected = "{ 7 } -> { 8 } -> { 9 } -> NULL"
    assert actual == expected

def test_linked_list_nine():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    actual = str(test_linked_list)
    expected = "{ 1 } -> NULL"
    assert actual == expected

def test_linked_list_ten():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(3)
    test_linked_list.append(2)
    test_linked_list.insert_before(3,5)
    actual = str(test_linked_list)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 2 } -> NULL"
    assert actual == expected

def test_linked_list_eleven():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(3)
    test_linked_list.append(2)
    test_linked_list.insert_before(1,5)
    actual = str(test_linked_list)
    expected = "{ 5 } -> { 1 } -> { 3 } -> { 2 } -> NULL"
    assert actual == expected

def test_linked_list_twelve():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(2)
    test_linked_list.append(2)
    test_linked_list.insert_before(2,5)
    actual = str(test_linked_list)
    expected = "{ 1 } -> { 5 } -> { 2 } -> { 2 } -> NULL"
    assert actual == expected

def test_linked_list_thirteen():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(3)
    test_linked_list.append(2)
    test_linked_list.insert_before(4,5)
    actual = str(test_linked_list)
    expected = "{ 1 } -> { 3 } -> { 2 } -> NULL"
    assert actual == expected

def test_linked_list_fourteen():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(3)
    test_linked_list.append(2)
    test_linked_list.insert_after(3,5)
    actual = str(test_linked_list)
    expected = "{ 1 } -> { 3 } -> { 5 } -> { 2 } -> NULL"
    assert actual == expected

def test_linked_list_fifteen():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(3)
    test_linked_list.append(2)
    test_linked_list.insert_after(2,5)
    actual = str(test_linked_list)
    expected = "{ 1 } -> { 3 } -> { 2 } -> { 5 } -> NULL"
    assert actual == expected

def test_linked_list_sixteen():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(2)
    test_linked_list.append(2)
    test_linked_list.insert_after(2,5)
    actual = str(test_linked_list)
    expected = "{ 1 } -> { 2 } -> { 5 } -> { 2 } -> NULL"
    assert actual == expected

def test_linked_list_seventeen():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(3)
    test_linked_list.append(2)
    test_linked_list.insert_after(4,5)
    actual = str(test_linked_list)
    expected = "{ 1 } -> { 3 } -> { 2 } -> NULL"
    assert actual == expected

def test_linked_list_eighteen():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(3)
    test_linked_list.append(8)
    test_linked_list.append(2)
    actual = test_linked_list.kth_from_end(0)
    expected = 2
    assert actual == expected

def test_linked_list_nineteen():
    test_linked_list = LinkedList()
    test_linked_list.append(1)
    test_linked_list.append(3)
    test_linked_list.append(8)
    test_linked_list.append(2)
    actual = test_linked_list.kth_from_end(2)
    expected = 3
    assert actual == expected

