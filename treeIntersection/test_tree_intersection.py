import pytest
from tree_intersection import tree_intersection
from tree import BinaryTree,Node

tree1 = BinaryTree()
tree2 = BinaryTree()
tree3 = BinaryTree()
tree4 = BinaryTree()
tree1.root = Node(150)
tree1.root.left = Node(100)
tree1.root.left.left = Node(75)
tree1.root.left.right = Node(160)
tree1.root.left.right.left = Node(125)
tree1.root.left.right.right = Node(175)
tree1.root.right = Node(250)
tree1.root.right.left = Node(200)
tree1.root.right.right = Node(350)
tree1.root.right.right.left = Node(300)
tree1.root.right.right.right = Node(500)

tree2.root = Node(42)
tree2.root.left = Node(100)
tree2.root.left.left = Node(15)
tree2.root.left.right = Node(160)
tree2.root.left.right.left = Node(125)
tree2.root.left.right.right = Node(175)
tree2.root.right = Node(600)
tree2.root.right.left = Node(200)
tree2.root.right.right = Node(350)
tree2.root.right.right.left = Node(4)
tree2.root.right.right.right = Node(500)


def test_hash_table_one():
    actual =  tree_intersection(tree1,tree2)
    expected = [100, 160, 125, 175, 200, 350, 500]
    assert actual == expected

def test_hash_table_two():
    actual =  tree_intersection(tree3,tree4)
    expected = []
    assert actual == expected

def test_hash_table_three():
    actual =  tree_intersection(tree1,tree3)
    expected = []
    assert actual == expected

def test_hash_table_four():
    actual =  tree_intersection(tree4,tree2)
    expected = []
    assert actual == expected