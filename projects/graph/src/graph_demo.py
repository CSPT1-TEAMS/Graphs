#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import queue
from sys import argv
import random
from graph import Graph, Vertex
from draw import BokehGraph


def main(draw_components=True):
    graph = Graph()
    graph = graph.draw_random_graph(10, 15)

    # for vertex in range(5):
    #     graph.add_vertex(Vertex(label=str(vertex)))

    # for _ in range(10):
    #     vertices = random.sample(range(1, 100), k=2)
    #     graph.add_edge(vertices[0], vertices[1])
    # graph.add_edge('0', '1')
    # graph.add_edge('0', '2')
    # graph.add_edge('0', '3')
    # graph.add_edge('4', '5')
    # graph.add_edge('4', '6')
    # graph.add_edge('4', '7')
    # graph.add_edge('8', '9')
    # graph.add_edge('8', '8')
    print("Graph", graph.print_graph())
    graph.print_graph()
    vertices = list(graph.vertices.keys())
    print("test", vertices)
    # print('BFS:', breadth_first_search(graph, vertices[0]))
    # print('Elissa DFS: ', depth_first_search(graph, vertices[0]))
    # print("DFS: ", dfs(graph, vertices[0]))
    print("Connected_comp: ", graph.connected_components())

    bg = BokehGraph(graph,  draw_components=draw_components)
    bg.show()


if __name__ == "__main__":
    # TODO - parse argv
    main()
