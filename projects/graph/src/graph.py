"""
Simple graph implementation compatible with BokehGraph class.
"""

from draw import BokehGraph


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges = ()):
        if not set(edges).issubset(self.vertices):
            print("Error")
        else:
            self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            print("Start or end vertex is invalid.")
            return False
        elif end in self.vertices[start]:
            print("Already connected.")
            return False
        else:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')

bg = BokehGraph(graph)
bg.show()