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

    def add_vertex(self, vertex):
        self.vertices.update({ vertex: set() })

    def add_edge(self, start, end, is_directed = True):

        self.vertices[start].add(end)
        if not is_directed:
            self.vertices[end].add(start)


# v1 = Vertex('A')
# v2 = Vertex('B')
# v3 = Vertex('C')
# g = Graph()
# g.add_vertex(v1)
# g.add_vertex(v2)
# g.add_vertex(v3)

