"""Graph representation using adjacency matrix."""
import math

class Vertex:
    """Vertices just need a label, the matrix will track edges."""
    # Using simple classes for illustrative purposes
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label


class Graph:
    """The graph is a matrix of 0s/1s indicating existence of edges."""
    # pylint: disable=too-few-public-methods
    def __init__(self, num_vertices):
        # * copying is shallow, so need explicit iteration for unique rows
        # matrix_dict = {}
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        # for row in self.matrix:
        #     matrix_dict[row.index] = row
        # self.matrix = matrix_dict


    def connect_vertex(self, row, col):
        """Add an edge between vertices indicated by row/col of matrix."""
        self.matrix[row][col] = 1
        self.matrix[col][row] = 1
    
    def add_vertex(self, vertex):
        new_row = [0] * (len(self.matrix)+1)

        matrix_clone = self.matrix[:]
        for i in matrix_clone:
            i.append(0)

        matrix_clone.append(new_row)
        self.matrix = matrix_clone

    def print_matrix(self):
        for row in self.matrix:
            print(row)


graph = Graph(5)
graph.add_vertex(6)
graph.connect_vertex(0,1)
graph.connect_vertex(1,2)
graph.connect_vertex(2,3)
graph.connect_vertex(3,4)
graph.connect_vertex(4,5)
graph.connect_vertex(0,4)
graph.connect_vertex(1,3)
graph.connect_vertex(5,1)
graph.connect_vertex(4,2)


graph.print_matrix()
