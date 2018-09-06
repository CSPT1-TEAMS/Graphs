#!/usr/bin/python

from graph import WeightedGraph

def dijkstra(graph, start, end):
    pass
    

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
    
    print(graph.vertices)
    print(dijkstra(graph, 1, 6))

if __name__ == '__main__':
    # TODO - parse argv
    main()


