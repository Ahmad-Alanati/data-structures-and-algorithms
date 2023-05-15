import math

class Node:
    def __init__(self,value,_next=None):
        self.value = value
        self.next = _next
      
    def __str__(self):
        return "{ "+str(self.value)+" }"

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self,value):
        if not isinstance(value,Node):
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            current = value
            while current.next != None:
                current = current.next
            current.next = self.head
            self.head = value
    
    def __str__(self):
        if self.head == None:
            return "there is no element in the list"
        current = self.head
        values = ""
        while True:
            values += str(current)+" -> "
            if current.next == None:
                values+="NULL"
                break
            else:
                current = current.next
        return values

    def max(self):
      current_node = self.head
      max = -math.inf
      while current_node != None:
        if current_node.value > max:
          max = current_node.value
        current_node = current_node.next
      return max


linked_list = LinkedList()
print(linked_list)
linked_list.insert(-1)
linked_list.insert(-2)
linked_list.insert(5)
linked_list.insert(-5)
linked_list.insert(-1)
print(linked_list)
print(linked_list.max())