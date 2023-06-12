class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        return self.pre_order_traversal(self.root)

    def pre_order_traversal(self,node):
        if not node:
            return []
        left = self.pre_order_traversal(node.left)
        right = self.pre_order_traversal(node.right)
        return [node.value] + left + right

    def in_order(self):
        return self.in_order_traversal(self.root)
    
    def in_order_traversal(self,node):
        if not node:
            return []
        left = self.in_order_traversal(node.left)
        right = self.in_order_traversal(node.right)
        return left + [node.value] + right

    def post_order(self):
        return self.post_order_traversal(self.root)
    
    def post_order_traversal(self,node):
        if not node:
            return []
        left = self.post_order_traversal(node.left)
        right = self.post_order_traversal(node.right)
        return left + right + [node.value]
    
class BST(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self,value):
        if not self.root:
            self.root = Node(value)
            return
        pointer = self.root
        while True:
            if pointer.value > value and pointer.left:
                pointer = pointer.left
            elif pointer.value <= value and pointer.right:
                pointer = pointer.right
            elif pointer.value > value:
                pointer.left = Node(value)
                break
            else:
                pointer.right = Node(value)
                break

    def contains(self,value):
        pointer = self.root
        while True:
            # print(pointer.value)
            if  not pointer:
                break
            elif pointer.value == value:
                return True
            elif pointer.value >= value:
                pointer = pointer.left
            else:
                pointer = pointer.right

        return False
            


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    tree.root.right.right = Node("G")
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(1)
    bst.add(4)
    bst.add(7)
    bst.add(6)
    bst.add(8)
    bst.add(5)
    print("Traversal pre-order")
    print(tree.pre_order())
    print("Traversal in-order")
    print(tree.in_order())
    print("Traversal post-order")
    print(tree.post_order())
    print("BST Traversal pre-order")
    print(bst.pre_order())
    print(bst.contains(10))