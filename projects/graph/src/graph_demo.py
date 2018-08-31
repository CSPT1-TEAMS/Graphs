#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import queue
import random
from sys import argv
from graph import Graph
from draw import BokehGraph

def draw_random_graph(graph, vertices, edges):
    vertices = random.sample(range(1, 100), vertices)
    for vertex in vertices:
        graph.add_vertex(vertex)

    bidirec = [False, True]
    for _ in range(edges):
        i = random.randint(0,1)
        pair = random.choices(vertices, k=2)
        graph.add_edge(pair[0], pair[1], bidirectional=bidirec[i])
    return graph

def print_graph( graph ):
    for v in graph.vertices:
        line = ""
        line += (str(v) + ": " )
        for e in graph.vertices[v]:
            line += str( e ) + " "
        print( line )

def breadth_first_search(graph, start_vertex):
    visted = []
    colors = {vertex : "white" for vertex in graph.vertices.keys()}

    q = queue.Queue()
    q.put(start_vertex)

    while not q.empty():
        vertex = q.get()
        colors[vertex] = "black"
        for edge in graph.vertices[vertex]:
            if colors[edge] == "white":
                colors[edge] = "gray"
                q.put(edge)
        visted.append(vertex)
    return visted

def main():
    graph = Graph()
    graph = draw_random_graph(graph, 5, 10)
    vertices = list(graph.vertices.keys())
    print_graph(graph)
    print(breadth_first_search(graph, vertices[0]))
    # bg = BokehGraph(graph)
    # bg.show()


if __name__ == "__main__":
    # TODO - parse argv
     main()
    # graph = Graph()
    # draw_random_graph(graph, 10, 20)
