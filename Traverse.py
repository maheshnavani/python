from queue import Queue
from graph import *
from collections import deque


def breath_first(graph, start=0):
    queue = Queue();
    queue.put(start)

    visited = np.zeros(graph.numVertices)
    output = []
    while not queue.empty():
        vertex = queue.get()
        if visited[vertex] == 0:
            visited[vertex] = 1
            output.append(vertex)
            for neighbour in graph.get_adjacent_vertices(vertex):
                queue.put(neighbour)
    return output


def depth_first(graph, start=0):
    stack = deque()
    stack.append(start)

    visited = np.zeros(graph.numVertices)
    output = []
    while stack:
        vertex = stack.pop()
        if visited[vertex] == 0:
            visited[vertex] = 1
            output.append(vertex)

            for neighbour in graph.get_adjacent_vertices(vertex):
                stack.append(neighbour)
    return output


g = AdjacencySetGraph(9)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(6,3)
g.add_edge(3,4)
g.add_edge(6,8)

bfs = breath_first(g,2)
print(bfs)

dfs = depth_first(g,0)
print(dfs)
