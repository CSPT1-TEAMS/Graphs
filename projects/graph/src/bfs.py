#!/usr/bin/python

from queue import *
from graph import Graph

def bfs(graph, start):
    nodes = []
    queue = Queue()
    queue.put(start)
    nodes.append(start)

    while not queue.empty():
        curr = queue.get()
        neighbors = graph.vertices[curr]
        for n in neighbors:
            if not n in nodes:
                nodes.append(n)
                queue.put(n)

    return nodes

def dfs(graph, start):
    nodes = []
    nodes.append(start)

    def recur(start):
        neighbors = graph.vertices[start]
        for n in neighbors:
            if n not in nodes:
                nodes.append(n)
                recur(n)
    
    recur(start)
    return nodes
    

def main():
    graph = Graph()

    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_edge(1,2)
    graph.add_edge(1,6)
    graph.add_edge(2,6)
    graph.add_edge(2,3)
    graph.add_edge(3,5)
    graph.add_edge(1,4)

    print('breadth first order: ', bfs(graph, 1))
    # [1, 2, 4, 6, 3, 5]
    print('depth first order:   ', dfs(graph, 1))
    # [1, 2, 3, 5, 6, 4]

if __name__ == '__main__':
    # TODO - parse argv
    main()
