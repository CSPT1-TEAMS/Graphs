#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import random
from sys import argv
from graph import Graph
from draw import BokehGraph

def draw_random_graph(graph, vertices, edges):
    vertices = random.sample(range(1, 100), vertices)
    for vertex in vertices:
        graph.add_vertex(vertex)
    for _ in range(edges):
        pair = random.choices(vertices, k=2)
        graph.add_edge(pair[0], pair[1])
    return graph 

def main():
    pass  # TODO
    graph = Graph()  # Instantiate your graph
    graph = draw_random_graph(graph, 10, 10)
    # graph.add_vertex('0')
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # graph.add_edge('0', '1')
    # graph.add_edge('0', '3')
    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    # TODO - parse argv
    main()
