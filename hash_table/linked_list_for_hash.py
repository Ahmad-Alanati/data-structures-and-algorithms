class Node:
    def __init__(self,value,_next=None,_back=None):
        """constructor
        it will build an object from this class with value and next and back nodes 
        """
        self.value = value
        self.next = _next
        self.back = _back
    
    def __str__(self):
        """
        this function will return a string with the value of the node everytime you call a string
        """
        return "{ "+str(self.value)+" }"
    
class LinkedList:
    def __init__(self,head=None):
        """constructor
        it will build an object from this class with head as a node
        """
        self.head = head

    def insert(self,value):
        """
        this function will take a value and add it to the beginning of the linked list
        """
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
        """
        this function will take a value and check if that value is in the linked list
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False
    
    def append(self,value):
        """
        this function will take a value and add it to the end of the linked list
        """
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
        """
        this function will take a value and add it before a givin element in the linked list
        """
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
        """
        this function will take a value and add it after a givin element in the linked list
        """
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
        """
        this function will return the linked list as a string
        """
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
        """
        this function will take a value and get the kth element in the linked list
        """
        current = self.head
        length = 0
        while current:
            length+=1
            current = current.next
        current = self.head
        if  k >= length:
            raise Exception("out of scope")
        if k<0:
            raise Exception("Negative value not accepted")
        length-=k
        while length!=1 and current:
            current = current.next
            length-=1
        return current.value
    
    @staticmethod
    def zipLists(linked_list1,linked_list2):
        """algorithm steps:
1- create a two pointer that point to the head of every list
2- if pointer1 and pointer2 is none raise exception
3- create a Boolean with value = True and an empty linked list
4- while pointer1 and pointer2 are not none
5- if boolean is true and pointer1 is not none
6- new linked list append the value for pointer2
7- pointer1 = pointer1.next
8- if pointer2 is not none
9- boolean = false
10- if the boolean is false or pointer1 is none
11- new linked list append the value for pointer2
12- pointer2 = pointer2.next
13- if pointer1 is not none
14- boolean = true
15- end of loop
16- return new linked"""
        list1_current = linked_list1.head
        list2_current = linked_list2.head
        if not list1_current and not list2_current:
            raise Exception("you can't zip two empty linked list")
        switch = True
        new_linked_list = LinkedList()
        while list1_current or list2_current:
            if switch and list1_current:
                new_linked_list.append(list1_current.value)
                list1_current = list1_current.next
                if list2_current:
                    switch = False
            else:
                new_linked_list.append(list2_current.value)
                list2_current = list2_current.next
                if list1_current:
                    switch = True
        return new_linked_list