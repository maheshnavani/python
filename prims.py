import priority_dict
from graph import  *

def spanning_tree(graph,source):
    # A dictionary mapping from vertex number to a tuple of
    # (distance from source, last vertex on path from source
    distance_table = {}

    for i in range(graph.numVertices):
        distance_table[i]  = (None,None)

    # The distance to source from itself is 0
    distance_table[source] = (0,source)

    # Holds mapping from source

    priority_queue = priority_dict.priority_dict()
    priority_queue[source] = 0

    visited_vertices = set()
    # Set of edges where each is represented as a string
    # "1->2" : is a edge between 1 and 2
    spanning_tree = set()
    while len(priority_queue.keys()) > 0:
        current_vertex = priority_queue.pop_smallest()

        # if we've visited a vertex earlier then we have
        # all outbound edges from it cover, so we need not visit again
        if current_vertex in visited_vertices:
            continue
        visited_vertices.add(current_vertex)

        # if the current vertex is the source, we haven't traversed the
        # edge yet, no edge to add to our spanning tree
        if current_vertex != source:
            last_vertex = distance_table[current_vertex][1]

            edge = str(last_vertex) + "->" + str(current_vertex)
            if ( edge not in spanning_tree):
                spanning_tree.add(edge)

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            distance = graph.get_edge_weight(current_vertex,neighbor)
            last_know_distance = distance_table[neighbor][0]

            if last_know_distance is None or last_know_distance > distance:
                distance_table[neighbor] = (distance, current_vertex)
                priority_queue[neighbor] = distance
    for edge in spanning_tree:
        print (edge)


g = AdjacencyMatrixGraph(8,False)
g.add_edge(0, 1,1)
g.add_edge(1,2,2)
g.add_edge(1,3,2)
g.add_edge(2,3,2)
g.add_edge(1,4,3)
g.add_edge(3,5,1)
g.add_edge(5,4,3)
g.add_edge(3,6,1)
g.add_edge(6,7,1)
g.add_edge(7,0,1)

spanning_tree(g,1)



