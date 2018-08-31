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

    bidirectional = bool(random.randint(0,1))
    for _ in range(edges):
        pair = random.choices(vertices, k=2)
        graph.add_edge(pair[0], pair[1], bidirectional=bidirectional)
    return graph

def print_graph(graph):
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

"""Elissa's depth first search"""
def depth_first_search(graph, start):
    def dfs_visit(vertex):
        colors[vertex] = 'gray'
        nodes.append(vertex)

        for edge in graph.vertices[vertex]:
            if colors[edge] == 'white':
                dfs_visit(edge)
        colors[vertex] = "black"

    nodes = []
    colors = {vertex : "white" for vertex in graph.vertices.keys()}
    for vertex in graph.vertices.keys():
        if colors[vertex] == 'white':
            dfs_visit(vertex)
    return nodes


def dfs(graph, start):
    """
    Depth first search traversal from a specified
    starting node
    """
    def find_unexplored_edge(vertex):
        """
        Helper function that returns an unexplored edge.
        If all edges are explored the function returns None
        """
        for edge in graph.vertices[vertex]:
            if colors[edge] == "white":
                colors[edge] = "gray"
                return edge
        return None

    visited = []
    stack = deque()
    colors = {
        vertex : "white"
        for vertex in graph.vertices.keys()
    }

    stack.append(start)
    visited.append(start)
    colors[start] = 'gray'

    while len(stack) > 0:
        vertex = stack[-1]
        edge = find_unexplored_edge(vertex)
        if edge:
            visited.append(edge)
            stack.append(edge)
            continue
        colors[vertex] = 'black'
        stack.pop()
    return visited


def main():
    graph = Graph()
    graph = draw_random_graph(graph, 5, 10)
    vertices = list(graph.vertices.keys())
    print_graph(graph)
    print('BFS:', breadth_first_search(graph, vertices[0]))
    print('Elissa DFS: ', depth_first_search(graph, vertices[0]))
    print("DFS: ", dfs(graph, vertices[0]))
    bg = BokehGraph(graph)
    bg.show()


if __name__ == "__main__":
    # TODO - parse argv
     main()
    # graph = Graph()
    # draw_random_graph(graph, 10, 20)
