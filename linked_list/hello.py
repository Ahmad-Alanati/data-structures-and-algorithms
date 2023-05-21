

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

def counter(linked_list,linked_list2):
    list_dict = {}
    list_dict2 = {}
    current =linked_list.head
    while current:
        try:
            list_dict[current.value]+=1
        except:
            list_dict[current.value]=1
        finally:
            current=current.next
    current =linked_list2.head
    while current:
        try:
            list_dict2[current.value]+=1
        except:
            list_dict2[current.value]=1
        finally:
            current=current.next
    counters = 0
    for element in list_dict:
        try:
            remaining = abs(list_dict[element]-list_dict2[element])
            counters+= max(list_dict[element],list_dict2[element])-remaining
        except:
            continue
    return counters



if __name__=="__main__":
  linked_list = LinkedList()#7->3->2->2->1->none
  linked_list.insert(1)
  linked_list.insert(2)
  linked_list.insert(2)
  linked_list.insert(3)
  linked_list.insert(7)
  #second list 7->3->2->1->1->none
  linked_list2 = LinkedList()
  linked_list2.insert(1)
  linked_list2.insert(1)
  linked_list2.insert(2)
  linked_list2.insert(3)
  linked_list2.insert(7)
  print(counter(linked_list,linked_list2))
