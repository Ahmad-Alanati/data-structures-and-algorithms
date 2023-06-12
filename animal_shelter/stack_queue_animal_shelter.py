from queue import Queue
import re

class AnimalShelter:
    def __init__(self):
        self.animals = Queue()
        self.waiting  = []

    def enqueue(self, animal):
        self.animals.enqueue(animal)
        self.waiting .append(0)

    def dequeue(self,species=None):
        if not species:
            self.waiting .pop(0)
            return self.animals.dequeue()
        str_test = r"(dog|cat)"
        if not re.match(str_test,species):
            return "null"
        temp_queue = Queue()
        result = None
        counter = 0
        while not self.animals.is_empty():
            if self.animals.front.value.species == species and result == None:
                result =self.animals.dequeue()
                self.waiting .pop(counter)
            else:
                self.waiting [counter]+=1
                counter+=1
                temp_queue.enqueue(self.animals.dequeue())
                
        while not temp_queue.is_empty():
            self.animals.enqueue(temp_queue.dequeue())
        return result  

    def peek(self):
        return self.animals.peek()
    

class Animal:
    def __init__(self,species,name):
        self.species = species
        self.name = name

    def get_species(self):
        return self.species
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return f"the species is {self.species} the name is {self.name}"
    
if __name__ == "__main__":
    shelter = AnimalShelter()
    animal1 = Animal("dog","hello1")
    animal2  = Animal("cat","hello2")
    shelter.enqueue(animal1)
    shelter.enqueue(animal2)
    print(shelter.peek())
    print(shelter.waiting )
    print(shelter.dequeue("dog"))
    print(shelter.waiting )
    #print(shelter.dequeue("cat"))

