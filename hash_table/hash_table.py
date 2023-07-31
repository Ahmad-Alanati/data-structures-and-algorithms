from linked_list_for_hash import Node,LinkedList
from operator import mul,add
from functools import reduce


class HashTable:
    def __init__(self,size=1024):
        """
        this is the constructor it will take a size and by default it is 1024.
        this constructor makes two list buckets with the length of the size and an empty list with None as a value
        """
        self.__size = size
        self.__buckets = [None for i in range(size)]
        self.keys = []


    def set(self,key,value):
        """
        this is the set function it take a key and a value
        it check if the bucket is empty if yes it will make a linked list and save it inside the bucket,
        it check if the key existed in the hash table if yes it will go to the place where the key is then change the value to the new one,
        if not it will add the key and the value to the linked list in the bucket
        """
        value_index = self.__hash_function(key)
        if self.__buckets[value_index] is None:
            self.__buckets[value_index] = LinkedList()
        if not self.has(key):
            self.__buckets[value_index].insert([key,value])
            self.keys.append(key)
        else:
            current = self.__buckets[value_index].head
            while current:
                if current.value[0] == key:
                    current.value[1] = value
                current = current.next
        

    def get(self,key):
        """
        this is the get function it take a key
        it check if the bucket has the key then it will return the value of the key if we don't have the key then return null
        """
        value_index = self.__hash_function(key)
        current = self.__buckets[value_index].head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return "null"
        

    def has(self,key):
        """
        this is the has function it take a key
        it check if the bucket has the key then it will return true else false
        """
        value_index = self.__hash_function(key)
        current = self.__buckets[value_index].head
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def get_keys(self):
        """
        this is the get keys function it take a nothing and return all the keys in the hash table
        """
        return self.keys

    def __hash_function(self,key):
        """
        this is the get hash function it take a key and return an index
        """
        return reduce(mul,[ord(char) for char in str(key)]) * 883 % self.__size
        # reduce(add,[ord(char) for char in key]) * 883 % self.__size
        # return sum([ord(char) for char in key]) * 883 % self.__size

    def __str__(self):
        buckets_str = ""
        for index in range(self.__size):
            if self.__buckets[index]:
                buckets_str += f"bucket {index}: {str(self.__buckets[index])}\n"
        return buckets_str


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.set(1,"hello")
    hash_table.set('1','hello world')
    hash_table.set(12,'ahmad')
    hash_table.set(15,'mohammad')
    print(hash_table.get(1))
    print(hash_table.get('1'))
    print(hash_table.get('15'))
    print(hash_table.get_keys())
    hash_table.set(1,"welcome")
    print(hash_table.get(1))
    print(str(hash_table))

