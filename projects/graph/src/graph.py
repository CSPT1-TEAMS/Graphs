"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end):
        if start not in self.vertices and end not in self.vertices:
            raise ValueError("No valid entries")
        else:
            self.vertices[start].add(end)
            self.vertices[end].add(start)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError("Already in the set")




graph = Graph()
v1 = Vertex('V1')
graph.add_vertex(v1)
v2 = Vertex('V2')
graph.add_vertex(v2)
v3 = Vertex('V3')
graph.add_vertex(v3)
# graph.add_edge('3', '4')
graph.add_edge(v1, v2)
graph.add_edge(v1, v3)
print(graph.vertices)

