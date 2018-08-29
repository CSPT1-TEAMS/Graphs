"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = set()
    def __repr__(self):
        return str(self.data)

class Edge:
    def __init__(self, destination):
        self.destination = destination

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = set()
    def add_edge(self, start, end):
        start.edges.add(end)    
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
    def draw_rep(self):
        rep = ''
        for v in self.vertices:
            rep += str(v) + '-> ['
            for e in v.edges:
                rep += str(e.data) + ' '
            rep += ']'
            print(rep)
            rep = ''    

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
print(graph.vertices)
