class Node:
    def __init__(self,value,_next=None) :
        self.value = value
        self.next = _next
    def __str__(self) :
        return str(self.value)
    

class Stack:
    def __init__(self,top=None) :
        self.top = top

    def push(self,value):
        """
        this method will add a new node to the top of stack
        """
        new_node = Node(value,self.top)
        self.top = new_node

    def pop(self):
        """
        this method will remove a new node from top of stack and return it
        """
        try:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp
        except KeyError as err:
            return err

    def peek(self):
        """
        this method will return the node on top of stack
        """
        try:
            if self.top:
                return self.top
            else:
                raise Exception("stack error")
        except KeyError as err:
            return err
        
    def is_empty(self):
        """
        this method will return True if the stack is empty and false if the stack is not empty
        """
        return True if self.top == None else False