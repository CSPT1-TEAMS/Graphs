#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import randint
from draw import BokehGraph
from graph import Graph
from sys import argv

def draw_random_graph(graph, vertices, edges):
    for i in range(vertices):
        graph.add_vertex(str(i))

    j = 0
    while j <= edges:
        graph.add_edge(
            str(randint(0, vertices - 1)),
            str(randint(0, vertices - 1))
        )
        j += 1

def main():
    graph = Graph()
    draw_random_graph(graph, 10, 20)

    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    # TODO - parse argv
    main()

