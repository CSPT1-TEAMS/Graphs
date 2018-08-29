"""Graph representation using adjacency list."""

class Edge:
    """Edges in the adjacency list are just a destination."""
    # Using simple classes for illustrative purposes
    # pylint: disable=too-few-public-methods
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    """Vertices have a label and a set of edges."""
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label
        self.edges = set()
    def __repr__(self):
        return str( self.label )    

class Graph:
    """The graph itself is simply a set of vertices."""
    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.vertices = set()
    def add_edge(self, start, end):
        start.edges.add(end)
    def add_vertex(self, vertex):
        self.vertices.add(vertex) 
    def draw_rep(self):
        rep = ''
        for v in self.vertices:
            rep += str(v) + "-> [ "
            for e in v.edges:
                rep += str(e.label) + " "
            rep += "]"
            print(rep)
            rep = ""    


my_graph = Graph()
v1 = Vertex('A')
v2 = Vertex('B')
v3 = Vertex('C')
my_graph.add_vertex(v1)
my_graph.add_vertex(v2)
my_graph.add_vertex(v3)
my_graph.add_edge(v1, v2)
my_graph.add_edge(v1, v3)
my_graph.draw_rep()
