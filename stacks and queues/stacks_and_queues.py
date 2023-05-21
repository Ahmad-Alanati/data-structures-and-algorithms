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
        new_node = Node(value,self.top)
        self.top = new_node

    def pop(self):
        try:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp
        except:
            return "you can't pop from an empty stack"

    def peek(self):
        try:
            if self.top:
                return self.top
            else:
                raise Exception("stack error")
        except:
            return "the stack is empty"
        
    def is_empty(self):
        return True if self.top == None else False
        
        

class Queue:
    def __init__(self,front=None) :
        self.front = front
        self.back = front
    
    def enqueue(self,value):
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
         except:
             return "you can't dequeue form an empty queue"

    def peek(self):
        try:
            if self.front:
                return self.front
            else:
                raise Exception("queue error")
        except:
            return "the queue is empty"
        
    def is_empty(self):
        return True if self.front == None else False



if __name__ == "__main__":
    # new_stack = Stack()
    # print(new_stack.is_empty())
    # print(new_stack.peek())
    # new_stack.push(5)
    # print(new_stack.is_empty())
    # print(new_stack.peek())
    # new_stack.push(6)
    # print(new_stack.peek())
    # print(new_stack.pop())
    # print(new_stack.pop())
    # print(new_stack.pop())
    new_queue = Queue()
    #print(new_queue.is_empty())
    # print(new_queue.peek())
    new_queue.enqueue(5)
    #print(new_queue.is_empty())
    new_queue.enqueue(4)
    # print(new_queue.peek())
    new_queue.enqueue(3)
    new_queue.enqueue(2)
    # print(new_queue.peek())
    print(new_queue.dequeue())
    print(new_queue.dequeue())
    print(new_queue.dequeue())
    print(new_queue.dequeue())
    print(new_queue.dequeue())
