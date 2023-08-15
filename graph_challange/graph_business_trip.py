from graph import Graph

def business_trip(graph,cities):
    """
    this function takes a graph and a list of cities and then it will return the cost of the trip
    """
    nodes = graph.get_vertices()
    cost = 0
    vertex = None
    for node in nodes:
        if node.value == cities[0]:
            vertex = node
            break

    for i in range(len(cities)-1):
        neighbors = graph.get_neighbors(vertex)
        check_if_any = True
        for neighbor in neighbors:
            if neighbor.vertex.value == cities[i+1]:
                cost+= neighbor.weight
                vertex = neighbor.vertex
                check_if_any = False
        if check_if_any:
            return "null"
    return cost

if __name__ == "__main__":
    cities = ["Arendelle", "Monstropolis", "Naboo"]
    graph = Graph()
    a = graph.add_vertex('Metroville')
    b = graph.add_vertex('Pandora')
    c = graph.add_vertex('Arendelle')
    d = graph.add_vertex('Monstropolis')
    e = graph.add_vertex('Naboo')
    f = graph.add_vertex('Narnia')

    graph.add_edge(a,b,82) 
    graph.add_edge(a,c,99)
    graph.add_edge(a,d,105)
    graph.add_edge(a,e,26)
    graph.add_edge(a,f,37)
    graph.add_edge(b,a,82)
    graph.add_edge(b,c,150)
    graph.add_edge(c,a,99)
    graph.add_edge(c,b,150)
    graph.add_edge(c,d,42)
    graph.add_edge(d,a,105)
    graph.add_edge(d,c,42)
    graph.add_edge(d,e,73)
    graph.add_edge(e,a,26)
    graph.add_edge(e,d,73)
    graph.add_edge(e,f,250)
    graph.add_edge(f,a,37)
    graph.add_edge(f,e,250)

    print(business_trip(graph,cities))
