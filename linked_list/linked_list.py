class Node:
    def __init__(self,value,_next=None,_back=None):
        self.value = value
        self.next = _next
        self.back = _back
    
    def __str__(self):
        return "{ "+str(self.value)+" }"
    
class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self,value):
        if not isinstance(value,Node):
            print("hello1")
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            print("hello2")
            current = value
            while current.next != None:
                current = current.next
            current.next = self.head
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
            if current == None:
                values+="NULL"
                break
            values += str(current)+" -> "
            current = current.next
        return values


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

if __name__ == "__main__":
    linked_list = LinkedList()
    print(linked_list)
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    print(linked_list)
    print(linked_list.includes(5))
    print(linked_list.includes(1))
    new_node = Node(4)
    new_node2 = Node(5,new_node)
    new_node3 = Node(6,new_node2)
    linked_list.insert(new_node3)
    print(linked_list)
    linked_list2 = LinkedList()
    linked_list2.insert(7)
    linked_list2.insert(8)
    linked_list2.insert(9)
    linked_list.insert(linked_list2.head)
    print(linked_list)