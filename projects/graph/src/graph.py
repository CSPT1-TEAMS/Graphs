"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        if not set(edges).issubset(self.vertices):
            print('Error')
        else:
            self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            print('Cannot connect vertices that are not in the graph')
            return False
        elif end in self.vertices[start]:
            print('Edge already exists')
            return False
        else:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)
            return True


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)
