#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import randint
from draw import BokehGraph
from queue import *
from graph import Graph
from sys import argv

def draw_random_graph(graph, vertices, edges):
    for i in range(vertices):
        graph.add_vertex(str(i))

    j = 0
    while j <= edges:
        graph.add_edge(
            str(randint(0, vertices - 1)),
            str(randint(0, vertices - 1))
        )
        j += 1

class CheckableQueue(Queue):
    def contains(self, item):
        with self.mutex:
            return item in self.queue

def bfs(graph, start):
    nodes = []
    queue = CheckableQueue()
    queue.put(start)

    while not queue.empty():
        # print(queue.qsize())
        curr = queue.get()
        neighbors = graph.vertices[curr]

        for neighbor in neighbors:
            if not neighbor in nodes and not queue.contains(neighbor):
                queue.put(neighbor)

        nodes.append(curr)

    return nodes



def main():
    graph = Graph()
    #draw_random_graph(graph, 10, 20)
    #bg = BokehGraph(graph)
    #bg.show()

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
    print(bfs(graph, 1))




if __name__ == '__main__':
    # TODO - parse argv
    main()

