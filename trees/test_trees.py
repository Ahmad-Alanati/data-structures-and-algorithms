import pytest
from tree import BinaryTree,BST,Node

# BinaryTree testing

def test_BinaryTree_one():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    actual = tree.pre_order()
    expected = [2, 7, 2, 6, 5, 11, 5, 9, 4]
    assert actual == expected

def test_BinaryTree_two():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    actual = tree.in_order()
    expected = [2, 7, 5, 6, 11, 2, 5, 4, 9]
    assert actual == expected

def test_BinaryTree_three():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    actual = tree.post_order()
    expected = [2, 5, 11, 6, 7, 4, 9, 5, 2]
    assert actual == expected

def test_BinaryTree_four():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    actual = tree.maximum()
    expected = 11
    assert actual == expected

# BST testing

def test_BST_one():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(1)
    bst.add(4)
    bst.add(7)
    bst.add(6)
    bst.add(8)
    bst.add(5)
    actual = bst.pre_order()
    expected = [5, 3, 1, 4, 7, 6, 5, 8]
    assert actual == expected

def test_BST_two():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(1)
    bst.add(4)
    bst.add(7)
    bst.add(6)
    bst.add(8)
    bst.add(5)
    actual = bst.contains(10)
    expected = False
    assert actual == expected

def test_BST_three():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(1)
    bst.add(4)
    bst.add(7)
    bst.add(6)
    bst.add(8)
    bst.add(5)
    actual = bst.contains(7)
    expected = True
    assert actual == expected