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
    graph.add_vertex('7')
    graph.add_vertex('10')
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
    graph.add_edge('6', '7')
    graph.add_edge('1', '10')


    # b_f_s( graph, '0' )
    graph_comps = c_components(graph)
    print(graph_comps)
    bg = BokehGraph(graph, graph_comps)
    bg.show()


def b_f_s(graph, startVert):

    visited = []
    colors = {}

    q = queue.Queue()

    for v in graph.vertices:
        colors[v] = 'White'

    print(graph.vertices)
    # startVert.colors = '666666'
    q.put(startVert) # The same as q = [start]


    while not q.empty():

        curr_node = q.get() # The same as q.pop(0)
        neighbors = graph.vertices[f'{curr_node}']

        if curr_node not in visited:
            colors[curr_node] = 'Black'
            visited.append(curr_node)


            for n in neighbors:
                if n not in visited:
                    if colors[n] == 'White':
                        colors[n] = 'Grey'
                    q.put(n)


    return visited

def c_components(graph):
    graph_comps = []
    visited_comps = set()

    for v in graph.vertices.keys():
        if v not in visited_comps:

            component = b_f_s(graph, v)

            graph_comps.append(component)

            for c in component:
                visited_comps.update(component)


    return graph_comps

if __name__ == '__main__':
    # TODO - parse argv
    main()
    pass
