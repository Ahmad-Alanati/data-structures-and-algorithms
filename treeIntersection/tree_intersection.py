from hash_table_tree import HashTable
from tree import BinaryTree,Node

def tree_intersection(tree1,tree2):
    hash_tree = HashTable()
    tree1_element = tree1.pre_order()
    tree2_element = tree2.pre_order()
    for element in tree1_element:
        hash_tree.set(element,0)
    list_of_intersection = []
    for element in tree2_element:
        if hash_tree.has(element):
            list_of_intersection.append(element)
    return list_of_intersection

    
if __name__ == "__main__":
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    # tree1.root = Node(150)
    # tree1.root.left = Node(100)
    # tree1.root.left.left = Node(75)
    # tree1.root.left.right = Node(160)
    # tree1.root.left.right.left = Node(125)
    # tree1.root.left.right.right = Node(175)
    # tree1.root.right = Node(250)
    # tree1.root.right.left = Node(200)
    # tree1.root.right.right = Node(350)
    # tree1.root.right.right.left = Node(300)
    # tree1.root.right.right.right = Node(500)

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

    print(tree_intersection(tree1,tree2))