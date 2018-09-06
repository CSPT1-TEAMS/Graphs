#!/usr/bin/python

import random
import queue
from draw import BokehGraph
from graph import Graph, Vertex

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv

def draw_random_graph(graph, vertices, edges):
    vertices = random.sample(range(1, 100), vertices)
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    for _ in range(edges):
        pair = random.choices(vertices, k = 2)
        graph.add_edge(pair[0], pair[1])

    return graph


def main():
    graph = Graph()
    graph = draw_random_graph(graph, 60, 120)
    # graph.add_vertex('0')
    # graph.add_vertex('2')
    # graph.add_vertex('5')
    # graph.add_vertex('6')
    # graph.add_vertex('9')
    # graph.add_vertex('4')
    # graph.add_vertex('1')
    # graph.add_edge('6', '4')
    # graph.add_edge('5', '0')
    # graph.add_edge('5', '9')
    # graph.add_edge('4', '0')
    # graph.add_edge('4', '1')
    # graph.add_edge('2', '1')



    bg = BokehGraph(graph)
    # print( b_f_s( graph, '0' ) )
    # print(connected_components(graph))
    bg.show()

# def connected_components(graph):
#     components = []
#     visited = set()

#     for vertex in graph.vertices.keys():
#         if vertex not in visited:
#             component = b_f_s( graph, vertex )
#             components.append(component)
#             for c in component:
#                 visited.update(component)

#     return components

# def b_f_s(graph, startVert):

#     visited = []
#     colors = {}

#     q = queue.Queue()

#     for v in graph.vertices:
#         colors[v] = 'White'

#     print(graph.vertices)
#     # startVert.colors = '666666'
#     q.put(startVert) # The same as q = [start]


#     while not q.empty():

#         curr_node = q.get() # The same as q.pop(0)
#         neighbors = graph.vertices[f'{curr_node}']

#         if curr_node not in visited:
#             colors[curr_node] = 'Black'
#             visited.append(curr_node)


#             for n in neighbors:
#                 if n not in visited:
#                     if colors[n] == 'White':
#                         colors[n] = 'Grey'
#                     q.put(n)
#                     print('colors', colors)


#     return visited

# def d_f_s(graph, startVert):

#     visited = []
#     colors = {}

#     s = [startVert]

#     for v in graph.vertices:
#         colors[v] = 'White'

#     print(graph.vertices)


#     while len(s) is not 0:

#         curr_node = s.pop()
#         neighbors = graph.vertices[f'{curr_node}']
#         for n in neighbors:
#             if n not in visited:
#                 visited.append(n)
#                 colors[curr_node] = 'Black'
#                 s.append(n)
#             if colors[n] == 'White':
#                 colors[n] = 'Grey'
    

#     return print("When it ends", visited, colors)


if __name__ == '__main__':
    # TODO - parse argv
    main()
    pass
