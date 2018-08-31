#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import random
from sys import argv
from graph import Graph
from draw import BokehGraph
from bokeh.models import (
    GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource)


def draw_random_graph(graph, vertices, edges):
    vertices = random.sample(range(1, 100), vertices)
    for vertex in vertices:
        graph.add_vertex(vertex)
    for _ in range(edges):
        pair = random.choices(vertices, k=2)
        graph.add_edge(pair[0], pair[1])
    return graph


# DFS(graph): pseudocode
#     for v of graph.verts:
#         v.color = white
#         v.parent = null
#     for v of graph.verts:
#         if v.color == white:
#             DFS_visit(v)
# DFS_visit(v):
#     v.color = gray
#     for neighbor of v.adjacent_nodes:
#         if neighbor.color == white:
#             neighbor.parent = v
#             DFS_visit(neighbor)
#     v.color = black

vertex_data = {}


def depth_first(graph):
    nodes = []
    for vertex in graph.vertices:
        vertex_data[vertex] = ['white', None]
        print('VERTEX_DATA', vertex_data)
    for vertex in graph.vertices:
        print('VERTEX::', vertex)
        if vertex_data[vertex][0] == 'white':
            nodes.append(vertex)
            DFS_visit(vertex, graph)
            print('Visiting:', vertex)
    print('Vertex_Data::', vertex_data)


def DFS_visit(vertex, graph):
    vertex_data[vertex][0] = 'grey'
    for neighbor in graph.vertices[vertex]:
        print('VERTEX:', vertex, 'NEIGHBOR:', neighbor)
        print('Vertex_Data::', vertex_data)
        if vertex_data[neighbor][0] == 'white':
            vertex_data[neighbor][1] = vertex
            DFS_visit(neighbor, graph)
    vertex_data[vertex][0] = 'black'

# ```pseudocode
# BFS(graph, startVert):
#   for v of graph.vertexes:
#     v.color = white

#   startVert.color = gray
#   queue.enqueue(startVert)

#   while !queue.isEmpty():
#     u = queue[0]  // Peek at head of queue, but do not dequeue!

#     for v of u.neighbors:
#       if v.color == white:
#         v.color = gray
#         queue.enqueue(v)

#     queue.dequeue()
#     u.color = black
# ```


import queue

vertex_data_b = {}


def breadth_first_search(graph, start):
    for v in graph.vertices:
        vertex_data_b[v] = 'white'

    vertex_data_b[start] = 'gray'
    q = []
    q.append(start)

    while q:
        first = q[0]

        for v in graph.vertices[first]:
            if vertex_data_b[v] == 'white':
                vertex_data_b[v] = 'grey'
                print('VDB', vertex_data_b)
                q.append(v)
        q = q[1:]
        print('Q:::', q)
        vertex_data_b[first] = 'black'
        print('VDB', vertex_data_b)


def main():
    pass  # TODO
    graph = Graph()  # Instantiate your graph
    # graph = draw_random_graph(graph, 10, 10)
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('0', '2')
    graph.add_edge('1', '4')
    graph.add_edge('1', '5')
    graph.add_edge('2', '6')
    # depth_first(graph)
    breadth_first_search(graph, '0')
    bg = BokehGraph(graph)
    bg.show()


if __name__ == '__main__':
    # TODO - parse argv
    main()
