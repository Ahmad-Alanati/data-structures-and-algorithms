from collections import deque

class Queue:
    def __init__(self):
        """
        this is the constructor for the queue 
        """
        self.queue = deque()

    def enqueue(self,value):
        """
        this function job is to add an element to the end of a queue
        """
        self.queue.append(value)
    
    def dequeue(self):
        """
        this function job is to remove the first element from a queue
        """
        return self.queue.popleft()
    
    def size(self):
        """
        this function job is to return the size of the queue
        """
        return len(self.queue)
    
class Stack:
    def __init__(self):
        """
        this is the constructor for the stack 
        """
        self.top = deque()

    def push(self,value):
        """
        this function job is to add an element to the top of a stack
        """
        self.top.append(value)
    
    def pop(self):
        """
        this function job is to remove the top element from a stack
        """
        return self.top.pop()
    
    def is_empty(self):
        """
        this function job is to return True if the stack is empty or False if not empty
        """
        return len(self.top) == 0
    

class Vertex:
    def __init__(self,value):
        """
        this is the constructor for the vertex to add it to the graph
        """
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight = 0):
        """
        this is the constructor for the edge to add it to the graph
        """
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return str(self.vertex)

class Graph:
    def __init__(self):
        """
        this is the constructor for the graph
        """
        self.__adjacent_list = {}

    def add_vertex(self,value):
        """
        this function job is to add a vertex to the graph
        """
        vertex = Vertex(value)
        self.__adjacent_list[vertex] = []
        return vertex

    def add_edge(self,vertex1,vertex2,weight = 0):
        """
        this function job is to add a edge to the graph
        """
        if vertex1 not in self.__adjacent_list:
            raise Exception("Starting vertex is not FOUND")
        if vertex2 not in self.__adjacent_list:
            raise Exception("Ending vertex is not FOUND")
        edge1 = Edge(vertex2,weight)
        edge2 = Edge(vertex1)
        self.__adjacent_list[vertex1].append(edge1)
        self.__adjacent_list[vertex2].append(edge2)
        

    def get_vertices(self):
        """
        this function job is to return all the vertex in the graph
        """
        return self.__adjacent_list.keys()

    def get_neighbors(self,vertex):
        """
        this function job is to return the edges for a given vertex
        """
        return self.__adjacent_list.get(vertex,[])

    def size(self):
        """
        this function job is to return the size of the graph
        """
        return len(self.__adjacent_list)
    
    def breadth_first(self,vertex):
        """
        this function job is to return a list with the breadth first traversal starting from the given vertex
        """
        list_of_visted_vertex = []
        visted = set()
        queue = Queue()

        queue.enqueue(vertex)
        visted.add(vertex)

        while queue.size():
            current_vertex = queue.dequeue()
            list_of_visted_vertex.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visted:
                    queue.enqueue(neighbor)
                    visted.add(neighbor)

        return list_of_visted_vertex
    
    def depth_first(self,vertex):
        """
        this function job is to return a list with the depth first traversal starting from the given vertex
        """
        list_of_visted_vertex = []
        visted = set()
        stack = Stack()

        stack.push(vertex)
        visted.add(vertex)
        while not stack.is_empty():
            current_vertex = stack.pop()
            list_of_visted_vertex.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)
            reversed_neighbors = []
            for neighbor in neighbors:
                reversed_neighbors.insert(0,neighbor)
            for edge in reversed_neighbors:
                neighbor = edge.vertex
                if neighbor not in visted:
                    stack.push(neighbor)
                    visted.add(neighbor)
        return list_of_visted_vertex

if __name__ == "__main__":
    graph = Graph()
    a = graph.add_vertex('A')
    b = graph.add_vertex('B')
    c = graph.add_vertex('C')
    d = graph.add_vertex('D')
    e = graph.add_vertex('E')
    f = graph.add_vertex('F')
    g = graph.add_vertex('G')
    h = graph.add_vertex('H')
# A, B, C, G, D, E, H, F
    graph.add_edge(a,b) 
    graph.add_edge(a,d)
    graph.add_edge(b,c)
    graph.add_edge(b,d)
    # graph.add_edge(c,g)
    # graph.add_edge(d,e)
    # graph.add_edge(d,f)
    # graph.add_edge(d,h)
    # print(graph.size())
    # for edge in graph.get_vertices():
    #     print(str(edge),end=" ")
    # print()
    # for edge in graph.get_neighbors(b):
    #     print(str(edge),end=" ")
    # print()
    print(graph.depth_first(d))
    
    #     a   b   c   d   e
    # a   [0  1   1   0   0]
    # b   [1  0   0   1   1]
    # c   [1  0   0   0   1]
    # d   [0  1   0   0   0]
    # e   [0  1   1   1   0]