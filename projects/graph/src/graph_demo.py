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
        vertex_data[vertex]= ['white', None]
    for vertex, value in enumerate(graph.vertices):
        print(value)
        if vertex_data[vertex][0] == 'white':
            nodes.append(vertex)
            DFS_visit(vertex)

def DFS_visit(vertex):
    vertex_data[vertex][0] = 'grey'
    for neighbor in vertex:
        if vertex_data[neighbor][0] == 'white':
            vertex_data[neighbor][1] = vertex
            DFS_visit(neighbor)
    vertex_data[vertex][0] = 'black'

def main():
    pass  # TODO
    graph = Graph()  # Instantiate your graph
    graph = draw_random_graph(graph, 10, 10)
    # print(graph.vertices)
    depth_first(graph)
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
