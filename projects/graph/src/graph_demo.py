#!/usr/bin/python

import queue
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
    graph.add_vertex('6')
    graph.add_vertex('9')
    graph.add_vertex('4')
    graph.add_vertex('1')
    # graph.add_edge('3', '4')
    graph.add_edge('0', '2')
    graph.add_edge('5', '0')
    graph.add_edge('5', '9')
    graph.add_edge('4', '0')

    bg = BokehGraph(graph)
    print( b_f_s( graph, '0' ) )
    # bg.show()


def b_f_s(graph, startVert):

    visited = []
    colors = {}

    q = queue.Queue()

    # for v in graph.vertices:
    #     colors[v] = 'FFFFFF'
    print(graph.vertices)
    # startVert.colors = '666666'
    q.put(startVert) # The same as q = [start]


    while not q.empty():

        curr_node = q.get() # The same as q.pop(0)
        neighbors = graph.vertices[f'{curr_node}']

        if curr_node not in visited:

            visited.append(curr_node)

            print("current", curr_node)
            print("visit", visited)

            for n in neighbors:
                if n not in visited:
                    q.put(n)
        
                    print("Q", q.queue)
        

    return print("When it ends", visited)


if __name__ == '__main__':
    # TODO - parse argv
    main()
    pass
