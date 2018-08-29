#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from draw import BokehGraph
from graph import Graph
from sys import argv


def main():
    graph = Graph()
    graph.add_vertex(4)
    graph.add_vertex(3)
    graph.add_vertex(9)
    graph.add_vertex(2)
    graph.add_vertex(0)
    graph.add_edge(2,9)
    graph.add_edge(4,3)
    graph.add_edge(4,4)
    graph.add_edge(9,2)
    graph.add_edge(3,9)
    graph.add_edge(9,0)
    graph.add_edge(2,0)
    graph.add_edge(3,0)
    graph.add_edge(4,0)

    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    # TODO - parse argv
    main()

