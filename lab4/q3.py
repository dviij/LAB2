from Queue import Queue

# Define the graph
graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 3},
    'D': {'A': 1, 'B': 2, 'C': 3}
}

# Define the TSP using BFS function
def tsp_bfs(graph, start):
    n = len(graph)
    q = Queue()
    q.put((start, [start], 0))

    cycles = []
    while not q.empty():
        node, path, cost = q.get()

        if len(path) == n:
            if node == start:
                cycles.append((path, cost))
        else:
            for neighbor, weight in graph[node].iteritems():
                if neighbor not in path:
                    q.put((neighbor, path + [neighbor], cost + weight))

    shortest_cycle = min(cycles, key=lambda x: x[1])
    return shortest_cycle

# Test the function with the given graph
start_node = 'A'
shortest_cycle = tsp_bfs(graph, start_node)
print(f"The shortest cycle starting from node {start_node} is: {shortest_cycle}")
