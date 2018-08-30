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
    print( b_f_s( graph, 0 ) )
    bg.show()


def b_f_s(graph, startVert):

    visited = []
    colors = {}

    q = queue.Queue()

    # for v in graph.vertices:
    #     colors[v] = 'FFFFFF'
    print(graph.vertices)
    # startVert.colors = '666666'
    q.put(graph.vertices[f'{startVert}']) # The same as q = [start]

    while not q.empty():

        curr_node = q.get() # The same as q.pop(0)

        if curr_node not in visited:
            a = list(curr_node)

            visited.append(a[0])

            print("current", curr_node)
            print("visit", visited)
            # neighbors = graph[curr_node]

            for n in curr_node:
                q.put(n)
                
                print("Q", q)

    return print("When it ends", visited)


#     visited = []

#     colors = {}

#   for v of graph.vertexes:
#     color[v] = white

#   startVert.color = gray
#   queue.enqueue(startVert) # queue = [startVert]

#   while !queue.isEmpty():
#     u = queue[0]  // Peek at head of queue, but do not dequeue!

#     for v of u.neighbors:
#       if v.color == white:
#         v.color = gray
#         queue.enqueue(v)
    
#     nodes.append(queue.dequeue())
#     u.color = black


if __name__ == '__main__':
    # TODO - parse argv
    main()
    pass
