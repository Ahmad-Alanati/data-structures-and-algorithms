import pytest
from graph import Graph

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