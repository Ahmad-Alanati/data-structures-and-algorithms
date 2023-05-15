class Node:
    def __init__(self,value,_next=None,_back=None):
        self.value = value
        self.next = _next
        self.back = _back
    
    def __str__(self):
        return "{ "+str(self.value)+" }"

class DoublyLinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self,value):
        if not isinstance(value,Node):
            new_node = Node(value)
            new_node.next = self.head
            if self.head != None:
                self.head.back = new_node
            self.head = new_node
        else:
            current = value
            while current.next != None:
                current = current.next
            current.next = self.head
            if self.head != None:
                self.head.back = current
            self.head = value


    def includes(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False
    
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
        values+="\nNow from the back\nNull"
        while True:
            values += " -> "+str(current)
            if current.back == None:
                break
            else:
                current = current.back
        return values
