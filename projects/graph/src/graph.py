"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __str__(self):
        return self.label

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        # Will this check work given that self.vertices is a dict & not a set?
        #if not set(edges).issubset(self.vertices)
        self.vertices[vertex] = set(edges)
        self.vertices.add(item)

    def add_edge(self, start, end, is_directed = True):

        # Make sure vertices exist in graph:
        #if start not in self.vertices

        # Make sure edge doesn't already exist

        self.vertices[start].add(end)
        if not is_directed:
            self.vertices[end].add(start)
    


v1 = Vertex('A')
v2 = Vertex('B')
v3 = Vertex('C')
g = Graph()
g.add_vertex(v1)
g.add_vertex(v2)
g.add_vertex(v3)

