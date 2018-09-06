"""
Simple graph implementation compatible with BokehGraph class.
"""
import queue 

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

    def connected_components(self):
        components = []
        visited = set()

        for vertex in self.vertices.keys():
            if vertex not in visited:
                component = self.b_f_s( vertex )
                components.append(component)
                for c in component:
                    visited.update(component)

        return components

    def b_f_s(self, startVert):

        visited = []
        colors = {}

        q = queue.Queue()

        for v in self.vertices:
            colors[v] = 'White'

        # print(self.vertices)
        # startVert.colors = '666666'
        q.put(startVert) # The same as q = [start]


        while not q.empty():

            curr_node = q.get() # The same as q.pop(0)
            neighbors = self.vertices[curr_node]

            if curr_node not in visited:
                colors[curr_node] = 'Black'
                visited.append(curr_node)


                for n in neighbors:
                    if n not in visited:
                        if colors[n] == 'White':
                            colors[n] = 'Grey'
                        q.put(n)
                        # print('colors', colors)


        return visited




# graph = Graph()
# v1 = Vertex('V1')
# graph.add_vertex(v1)
# v2 = Vertex('V2')
# graph.add_vertex(v2)
# v3 = Vertex('V3')
# graph.add_vertex(v3)
# # graph.add_edge('3', '4')
# graph.add_edge(v1, v2)
# graph.add_edge(v1, v3)
# print(graph.vertices)

