"""
Simple graph implementation compatible with BokehGraph class.
"""
import queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional=False):
        if start not in self.vertices and end not in self.vertices:
            raise ValueError("One or more vertices do not exist")
        else:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('4', '1')
    print(graph.vertices)
