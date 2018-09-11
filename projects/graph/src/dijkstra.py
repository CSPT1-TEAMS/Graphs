#!/usr/bin/python

from graph import WeightedGraph
from math import inf

def dijkstra(graph, start, end):
    #def distance_btwn(start, end):
    #    return graph.vertices[start][end]

    shortest_distance = {}
    parent = {}
    vertices = [v for v in graph.vertices.keys()]

    print('vertices:', vertices)

    for vertex in vertices:
        shortest_distance[vertex] = inf
    shortest_distance[start] = 0

    print('shortest distance before:', shortest_distance)

    while vertices:
        minimum = None
        for vertex in vertices:
            if minimum is None:
                minimum = vertex
            elif shortest_distance[vertex] < shortest_distance[minimum]:
                minimum = vertex

        for child, weight in graph.vertices[minimum].items():
            if weight + shortest_distance[minimum] < shortest_distance[child]:
                # relax shortest distance at child node:
                shortest_distance[child] = weight + shortest_distance[minimum]
                parent[child] = minimum

        print('minimum at end of while loop:', minimum)
        print('vertices in while loop; popping', vertices)
        vertices.pop(minimum)

        print('parent:', parent)

    return shortest_distance
                
    

def main():
    graph = WeightedGraph()

    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)

    graph.add_edge(1,2,4)
    graph.add_edge(1,3,3)
    graph.add_edge(1,5,7)
    graph.add_edge(2,3,6)
    graph.add_edge(2,4,5)
    graph.add_edge(3,4,11)
    graph.add_edge(3,5,8)
    graph.add_edge(4,5,2)
    graph.add_edge(4,6,2)
    graph.add_edge(4,7,10)
    graph.add_edge(5,7,5)
    graph.add_edge(6,7,3)
    
    print('weighted graph: \n start : \n\t end : \n\t\t weight:', graph.vertices)

    print(dijkstra(graph, 1, 6)) # distance: 11, path: 1, 2, 4, 6

if __name__ == '__main__':
    # TODO - parse argv
    main()


