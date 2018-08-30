#!/usr/bin/python

from queue import *
from graph import Graph


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
