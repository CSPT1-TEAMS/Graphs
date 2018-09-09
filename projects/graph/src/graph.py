"""
Simple graph implementation compatible with BokehGraph class.
"""
import queue
import random
from collections import deque
from draw import BokehGraph

class Vertex:
    """Represent a vertex with a label and possible connected component."""

    def __init__(self, label, component = -1):
        self.label = str(label)
        self.component = component
        self.edges = set()


    def __repr__(self):
        return self.label


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def draw_random_graph(self, vertices, edges):

        grid = []
        rand_vertices = random.sample(range(1, 100), vertices)
        for i in rand_vertices:
            grid.append(Vertex(label=str(i)))

        print("grid?", grid)
        print("vertices?", vertices)

        for i in range(vertices - 1):
            bidirectional = bool(random.randint(0, 1))
            if (random.randrange(vertices) < edges  // 2):
                if(random.randrange(vertices) < edges // 2):
                    print("verts",len(self.vertices)
                        )
                    print(grid)
                    print(grid[i])
                    self.add_edge(grid[i].label, grid[i+1].label, bidirectional=bidirectional)
                    self.add_edge(grid[i].label, grid[i+1].label, bidirectional=bidirectional)
                    # print("verts", len(self.vertices))

                    
        for vertex in grid:
            self.add_vertex(vertex)

    # def draw_random_graph(self, vertices, edges):
    #     vertices = random.sample(range(1, 100), vertices)
    #     for vertex in vertices:
    #         self.add_vertex(vertex)

    #     bidirectional = bool(random.randint(0, 1))
    #     for _ in range(edges):
    #         success = False
    #         while not success:
    #             pair = random.choices(vertices, k=2)
    #             success = self.add_edge(
    #                 pair[0], pair[1], bidirectional=bidirectional
    #             )
        return self

    def add_vertex(self, vertex, edges=()):
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: adding vertex that already exists')
        else:        
            self.vertices[vertex] = set(edges)
        # if not isinstance(vertex, Vertex):
        #     vertex = Vertex(vertex)
        # if vertex.label in self.vertices:
        #     raise Exception("Error: Vertex already exists.")
        # self.vertices[vertex.label] = vertex

    def add_edge(self, start, end, bidirectional=True):
        print("start", start)
        if start not in self.vertices or end not in self.vertices:
            print('Vertices to connect not in graph!')
            return False
        elif end in self.vertices[start]:
        #  or start in self.vertices[end]:
            return False
        else:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)
            return True
        # if isinstance(start, Vertex):
        #     start = start.label
        #     print("start.label", start)
        # if isinstance(end, Vertex):
        #     end = end.label
        # if start not in list(self.vertices.keys()):
        #     self.add_vertex(Vertex(start))
        # if end not in list(self.vertices.keys()):
        #     self.add_vertex(Vertex(end))

        # return True

        # bidirectional = bool(random.randint(0, 1))
        # for _ in range(edges):
        #     success = False
        #     while not success:
        #         pair = random.choices(rand_vertices, k=2)
        #         success = self.add_edge(
        #             pair[0], pair[1], bidirectional=bidirectional
        # #         )
        # #     return True
        # """Add a edge (default bidirectional) between two vertices."""
        # if start not in self.vertices or end not in self.vertices:
        #     print('Vertices to connect not in graph!')
        #     return False
        # self.vertices[start].add(end)
        # if bidirectional:
        #     self.vertices[end].add(start)
        #     return True


    # def draw_random_graph(self, vertices, edges):

    #     grid = []
    #     rand_vertices = random.sample(range(1, 100), vertices)
    #     for i in rand_vertices:
    #         grid.append(Vertex(label=str(i)))

    #     print("grid?", grid)
    #     print("vertices?", vertices)



    #     for i in range(vertices - 1):
    #         bidirectional = bool(random.randint(0, 1))
    #         if (random.randrange(vertices) < edges  // 2):
    #             # if(random.randrange(vertices) < edges // 2):
    #                 print("verts",len(self.vertices.keys())
    #                     )
    #                 print(grid)
    #                 print(grid[i])
    #                 self.add_edge(grid[i].label, grid[i+1].label, bidirectional=bidirectional)
    #                 self.add_edge(grid[i].label, grid[i+1].label, bidirectional=bidirectional)

    #     for vertex in grid:
    #         self.add_vertex(vertex)

    # def connected_components(self, vertex)
    #             print("in_comp", in_component)
    #             for other_vertex in in_component:
    #                 other_vertex.component = current
    #             visited.update(in_component)
    #             current += 1
    #     self.components = current


    def print_graph(self):
        for v in self.vertices:
            line = ""
            line += (str(v) + ": ")
            for e in self.vertices[v]:
                line += str(e) + " "
            print(line)


    def breadth_first_search(self, start_vertex):
        visted = []
        colors = {vertex: "white" for vertex in self.vertices.keys()}

        q = queue.Queue()
        q.put(start_vertex)

        while not q.empty():
            vertex = q.get()
            colors[vertex] = "black"
            for edge in self.vertices[vertex]:
                if colors[edge] == "white":
                    colors[edge] = "gray"
                    q.put(edge)
            visted.append(vertex)
        return visted


    """Elissa's depth first search"""


    def depth_first_search(self, start):
        def dfs_visit(vertex):
            colors[vertex] = 'gray'
            nodes.append(vertex)

            for edge in self.vertices[vertex]:
                if colors[edge] == 'white':
                    dfs_visit(edge)
            colors[vertex] = "black"

        nodes = []
        colors = {vertex: "white" for vertex in self.vertices.keys()}
        for vertex in self.vertices.keys():
            if colors[vertex] == 'white':
                dfs_visit(vertex)
        return nodes


    def dfs(self, start):
        """
        Depth first search traversal from a specified
        starting node
        """
        def find_unexplored_edge(vertex):
            """
            Helper function that returns an unexplored edge.
            If all edges are explored the function returns None
            """
            for edge in self.vertices[vertex]:
                if colors[edge] == "white":
                    colors[edge] = "gray"
                    return edge
            return None

        visited = []
        stack = deque()
        colors = {
            vertex: "white"
            for vertex in self.vertices.keys()
        }
        stack.append(start)
        visited.append(start)
        colors[start] = 'gray'

        while len(stack) > 0:
            vertex = stack[-1]
            edge = find_unexplored_edge(vertex)
            if edge:
                visited.append(edge)
                stack.append(edge)
                continue
            colors[vertex] = 'black'
            stack.pop()
        return visited

    def connected_components(self):
        visited = set()
        current = 0

        for vertex in self.vertices:
            # print("SE>",self.vertices)
            if vertex not in visited:
                in_component = self.breadth_first_search(vertex)
                # print("in_comp", in_component)
                for other_vertex in in_component:
                    other_vertex.component = current
                visited.update(in_component)
                current += 1
        self.components = current


# if __name__ == "__main__":
