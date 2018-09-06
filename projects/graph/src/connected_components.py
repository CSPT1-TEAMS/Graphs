#!/usr/bin/python

from graph import Graph
from bfs import bfs
from dfs import dfs

def connected_components(graph):
    components = []
    visited = set()

    for vertex in graph.vertices.keys():
        if vertex not in visited:
            component = bfs(graph, vertex)
            visited.update(component)
            components.append(component)

    return components


def main():
    graph = Graph()

    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_edge(1,2)
    graph.add_edge(1,6)
    graph.add_edge(2,6)
    graph.add_edge(2,3)
    graph.add_edge(3,5)
    graph.add_edge(1,4)
    graph.add_edge(8,9)

    print('breadth first order: ', bfs(graph, 1))
    # [1, 2, 4, 6, 3, 5]
    print('depth first order: ', dfs(graph, 1))
    # [1, 2, 4, 6, 3, 5]
    print('depth first order: ', bfs(graph, 7))
    # [1, 2, 4, 6, 3, 5]
    print('depth first order: ', dfs(graph, 8))
    # [1, 2, 4, 6, 3, 5]

    print('connected components: ', connected_components(graph))

if __name__ == '__main__':
    # TODO - parse argv
    main()


