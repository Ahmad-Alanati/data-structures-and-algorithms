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
        # self.__adjacent_list[vertex1].append(edge2)
        

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

if __name__ == "__main__":
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    c = g.add_vertex('C')
    d = g.add_vertex('D')
    e = g.add_vertex('E')

    g.add_edge(a,b) 
    g.add_edge(a,c)
    g.add_edge(b,d)
    g.add_edge(b,e)
    g.add_edge(e,d)
    g.add_edge(e,c)
    print(g.size())
    for edge in g.get_vertices():
        print(str(edge),end=" ")
    print()
    for edge in g.get_neighbors(b):
        print(str(edge),end=" ")
    print()
    print(g.breadth_first(a))
    
    #     a   b   c   d   e
    # a   [0  1   1   0   0]
    # b   [0  0   0   1   1]
    # c   [0  0   0   0   0]
    # d   [0  0   0   0   0]
    # e   [0  0   1   1   0]