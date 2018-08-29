#!/usr/bin/python

from draw import BokehGraph
from graph import Graph, Vertex

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv


def main():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('2')
    graph.add_vertex('5')
    # graph.add_edge('3', '4')
    graph.add_edge('0', '2')
    graph.add_edge('5', '0')

    bg = BokehGraph(graph)
    bg.show()


if __name__ == '__main__':
    # TODO - parse argv
    main()
    pass
