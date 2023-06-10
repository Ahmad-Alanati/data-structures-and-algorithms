class Node:
    def __init__(self,value,_next=None) :
        self.value = value
        self.next = _next
    def __str__(self) :
        return str(self.value)

class Queue:
    def __init__(self,front=None) :
        self.front = front
        self.back = front
    
    def enqueue(self,value):
        """
        this method will add a new node to the back of a Queue
        """
        if self.front==None:
            new_node = Node(value)
            self.front = new_node
            self.back = new_node
        elif self.back==self.front:
            new_node = Node(value,self.front)
            self.back = new_node
        else:
            new_node = Node(value,self.back)
            self.back = new_node
           

    def dequeue(self):
        """
        this method will remove a node from the front of a Queue
        """
        try:
            if self.back != self.front:
                temp = self.back
                while temp.next != self.front:
                    temp=temp.next
                    
                self.front =temp
                temp=temp.next
                self.front.next=None
                return temp
            else:
                temp = self.back
                self.back = self.front = self.front.next
                return temp
        except KeyError as err:
             return err

    def peek(self):
        """
        this method will return the node from the front of a Queue
        """
        try:
            if self.front:
                return self.front
            else:
                raise Exception("queue error")
        except KeyError as err:
            return err
        
    def is_empty(self):
        """
        this method will return True if the Queue is empty and false if the Queue is not empty
        """
        return True if self.front == None else False
