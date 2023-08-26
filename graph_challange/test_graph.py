import pytest
from graph import Graph
from graph_business_trip import business_trip

# graph tests

def test_graph_one():
    g = Graph()
    a = g.add_vertex('A')
    actual =  g.breadth_first(a)
    expected = ['A']
    assert actual == expected

def test_graph_two():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    g.add_edge(a,b) 
    actual =  g.breadth_first(a)
    expected = ['A','B']
    assert actual == expected

def test_graph_three():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    actual =  g.breadth_first(a)
    expected = ['A']
    assert actual == expected

def test_graph_four():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    actual = [str(vertex) for vertex in g.get_vertices()]
    expected = ['A','B']
    assert actual == expected

def test_graph_five():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    c = g.add_vertex('C')
    g.add_edge(a,b) 
    g.add_edge(b,c)
    actual =  [str(vertex) for vertex in g.get_neighbors(a)]
    expected = ['B']
    assert actual == expected


def test_graph_six():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    c = g.add_vertex('C')
    g.add_edge(a,b,100) 
    g.add_edge(b,c)
    actual =  {str(vertex):vertex.weight for vertex in g.get_neighbors(a)}
    expected = {'B':100}
    assert actual == expected

def test_graph_seven():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    c = g.add_vertex('C')
    g.add_edge(a,b,100) 
    g.add_edge(b,c)
    actual =  g.size()
    expected = 3
    assert actual == expected

def test_graph_eight():
    g = Graph()
    a = g.add_vertex('A')
    
    g.add_edge(a,a) 
    actual =  g.breadth_first(a)
    expected = ['A']
    assert actual == expected

# business_trip tests

def test_graph_nine():
    graph = Graph()
    a = graph.add_vertex('Metroville')
    b = graph.add_vertex('Pandora')
    c = graph.add_vertex('Arendelle')
    
    graph.add_edge(a,b,82) 
    graph.add_edge(a,c,99)
    graph.add_edge(b,a,82)
    graph.add_edge(c,a,99)
    cities = ["Metroville", "Pandora"]

    actual =  business_trip(graph,cities)
    expected = 82
    assert actual == expected


def test_graph_ten():
    graph = Graph()
    a = graph.add_vertex('Metroville')
    b = graph.add_vertex('Pandora')
    c = graph.add_vertex('Arendelle')
    
    graph.add_edge(a,b,82) 
    graph.add_edge(a,c,99)
    graph.add_edge(b,a,82)
    graph.add_edge(c,a,99)
    cities = ["Pandora", "Metroville" ,"Arendelle"]

    actual =  business_trip(graph,cities)
    expected = 181
    assert actual == expected

def test_graph_eleven():
    graph = Graph()
    a = graph.add_vertex('Metroville')
    b = graph.add_vertex('Pandora')
    c = graph.add_vertex('Arendelle')
    
    graph.add_edge(a,b,82) 
    graph.add_edge(a,c,99)
    graph.add_edge(b,a,82)
    graph.add_edge(c,a,99)
    cities = ["Metroville", "Pandora","Arendelle"]

    actual =  business_trip(graph,cities)
    expected = "null"
    assert actual == expected

# depth_first tests

def test_graph_twelve():
    graph = Graph()
    a = graph.add_vertex('A')
    b = graph.add_vertex('B')
    c = graph.add_vertex('C')
    d = graph.add_vertex('D')
    
    graph.add_edge(a,b) 
    graph.add_edge(a,d)
    graph.add_edge(b,c)
    graph.add_edge(b,d)

    actual =  graph.depth_first(a)
    expected = ['A', 'B', 'C', 'D']
    assert actual == expected


def test_graph_thirteen():
    graph = Graph()
    a = graph.add_vertex('A')
    b = graph.add_vertex('B')
    c = graph.add_vertex('C')
    d = graph.add_vertex('D')
    actual =  graph.depth_first(a)
    expected = ['A']
    assert actual == expected

def test_graph_fourteen():
    graph = Graph()
    a = graph.add_vertex('A')
    b = graph.add_vertex('B')
    c = graph.add_vertex('C')
    d = graph.add_vertex('D')
    
    graph.add_edge(a,b) 
    graph.add_edge(a,d)
    graph.add_edge(b,c)
    graph.add_edge(b,d)

    actual =  graph.depth_first(d)
    expected = ['D', 'A', 'B', 'C']
    assert actual == expected