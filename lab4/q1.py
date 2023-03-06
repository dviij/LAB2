from collections import defaultdict, deque

# Define the graph
graph = defaultdict(list)
graph[5].extend([2, 0])
graph[4].extend([0, 1])
graph[2].append(3)
graph[3].append(1)

# Calculate in-degree of each vertex
in_degree = {v: 0 for v in graph}
for v in graph:
    for neighbor in graph[v]:
        if neighbor not in in_degree:
            in_degree[neighbor] = 0
        in_degree[neighbor] += 1
    if v not in in_degree:
        in_degree[v] = 0

# Enqueue all vertices with in-degree 0
queue = deque([v for v in in_degree if in_degree[v] == 0])

# Perform BFS and generate the sorted list
sorted_list = []
while queue:
    u = queue.popleft()
    sorted_list.append(u)
    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

# Print the sorted list
print(sorted_list)
