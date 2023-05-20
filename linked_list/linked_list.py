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
            new_node = Node(value,self.head)
            self.head = new_node
        else:
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
    
    def append(self,value):
        current = self.head
        if not current:
            self.insert(value)
            return
        while current.next:
            current = current.next
        if not isinstance(value,Node):
            new_node = Node(value)
            current.next = new_node
        else:
            current.next = value


    def insert_before(self,list_value,new_value):
        current = self.head
        if current.value == list_value:
            self.insert(new_value)
            return
        while current.next and current.next.value != list_value:
            current = current.next
        if not current.next:
            return
        if not isinstance(new_value,Node):
            new_node = Node(new_value,current.next)
            current.next = new_node
        else:
            new_value_current = new_value
            while new_value_current.next:
                new_value_current = new_value_current.next
            new_value_current.next = current.next
            current.next = new_value

    def insert_after(self,list_value,new_value):
        current = self.head
        if not current:
            self.insert(new_value)
            return
        while current.next and current.value != list_value:
            current = current.next
        if current.value == list_value and not current.next:
            self.append(new_value)
            return
        elif not current.next:
            return
        if not isinstance(new_value,Node):
            new_node = Node(new_value,current.next)
            current.next = new_node
        else:
            new_value_current = new_value
            while new_value_current.next:
                new_value_current = new_value_current.next
            new_value_current.next = current.next
            current.next = new_value
        
    
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
    
    def kth_from_end(self,k):
        current = self.head
        length = 0
        while current:
            length+=1
            current = current.next
        current = self.head
        if  k >= length:
            raise ValueError("out of scope")
        if k<0:
            raise ValueError("Negative value not accepted")
        length-=k
        while length!=1 and current:
            current = current.next
            length-=1
        return current.value


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
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.insert_after(4, 5)
    print(linked_list)
    print(linked_list.kth_from_end(-1))
    # print(linked_list.includes(5))
    # print(linked_list.includes(1))
    # new_node = Node(6)
    # new_node2 = Node(5,new_node)
    # new_node3 = Node(4,new_node2)
    # linked_list.insert_before(4,new_node3)
    # print(linked_list)
    # linked_list2 = LinkedList()
    # linked_list2.append(7)
    # linked_list2.append(8)
    # linked_list2.append(9)
    # linked_list.insert_before(2,linked_list2.head)
    # print(linked_list)