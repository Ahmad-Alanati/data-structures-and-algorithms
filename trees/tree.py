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
    
    def maximum(self):
        # tree_list = self.pre_order()
        # max_value = tree_list[0]
        # for element in tree_list:
        #     if max_value < element:
        #         max_value = element
        # return max_value
        return self.maximum_recursion(self.root)
    
    def maximum_recursion(self,node):
        if not node:
            return float('-inf')
        maximum_node = node.value
        left_max = self.maximum_recursion(node.left)
        right_max = self.maximum_recursion(node.right)

        if maximum_node < left_max:
            maximum_node = left_max
        elif maximum_node < right_max:
            maximum_node = right_max
        
        return maximum_node

    
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
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
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
    print("maximum value:")
    print(tree.maximum())