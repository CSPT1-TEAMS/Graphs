"""
Simple graph implementation compatible with BokehGraph class.
"""

    

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

class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices.update({ vertex: dict() })

    def add_edge(self, start, end, weight):
        self.vertices[start].update({ end: weight })
        self.vertices[end].update({ start: weight })

        #print('start:', start)
        #print('end:', end)
        #print('weight:', weight)
        #print('also weight:', self.vertices[start][end])
        #print('also weight:', self.vertices[end][start])
        #print('\n')

        
