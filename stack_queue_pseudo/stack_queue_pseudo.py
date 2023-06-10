class Node:
    def __init__(self,value,_next=None) :
        self.value = value
        self.next = _next
    def __str__(self) :
        return str(self.value)
    


class PseudoQueue:
    def __init__(self,top=None):
        self.top = top

    def enqueue(self,value):
        if not isinstance(value,Node):
            new_node = Node(value,self.top)
            self.top = new_node
        else:
            value.next = self.top
            self.top = value
        

    def dequeue(self):
        if not self.top:
            raise Exception("queue is empty")
        new_stack = PseudoQueue()
        value = None
        while self.top.next:
            # print(self)
            new_stack.enqueue(self.top.value)
            self.top = self.top.next
        value = self.top.value
        self.top = None
        while new_stack.top:
            # print(new_stack)
            self.enqueue(new_stack.top.value)
            new_stack.top = new_stack.top.next
        # print(self)
        return value
        


    def __str__(self):
        current = self.top
        queue_value = ""
        while current:
            queue_value+= str(current.value) + " -> "
            current = current.next
        queue_value += "None"
        return queue_value
    
if __name__ == "__main__":
    _queue = PseudoQueue()
    _queue.enqueue(20)
    _queue.enqueue(15)
    _queue.enqueue(10)
    # _queue.enqueue(4)
    # _queue.enqueue(5)
    # nodeA = Node(6)
    # _queue.enqueue(nodeA)
    print(_queue)
    # print(_queue.dequeue())
    # print(_queue)