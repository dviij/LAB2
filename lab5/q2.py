from queue import PriorityQueue

def ucs(graph, start, goal):
    explored = set()
    queue = PriorityQueue()
    queue.put((0, start, [start]))

    while not queue.empty():
        (cost, node, path) = queue.get()

        if node not in explored:
            explored.add(node)

            if node == goal:
                return path, cost

            for neighbor, edge_cost in graph[node].items():
                if neighbor not in explored:
                    total_cost = cost + edge_cost
                    new_path = path + [neighbor]
                    queue.put((total_cost, neighbor, new_path))

    return None, None
graph = {
    'S': {'A': 5, 'D': 6},
    'A': {'G1': 9,'B':2},
    'B': {'A': 2,'C':1},
    'C': {'G2': 5, 'S': 6,'F':7},
    'D': {'E': 2,'C':2},
    'E': {'G3':7},
    'F':{'G3':8,'D':2},
    'G1': {},
    'G2':{},
    'G3':{}
}

start_node1 = 'S'
goal_node1 = 'G1'
best_path1, best_cost1 = ucs(graph, start_node1, goal_node1)

start_node2 = 'S'
goal_node2 = 'G2'
best_path2, best_cost2 = ucs(graph, start_node2, goal_node2)

start_node3 = 'S'
goal_node3 = 'G3'
best_path3, best_cost3 = ucs(graph, start_node3, goal_node3)

print("Cumilative Cost of G1 =",best_cost1)
print("Cumilative Cost of G2 =",best_cost2)
print("Cumilative Cost of G3 =",best_cost3)


if(best_cost1<best_cost2 and best_cost1<best_cost3):
    print(f"Threfore the Best path is from {start_node1} to {goal_node1} = {' -> '.join(best_path1)}")
    print("Best Cost =",best_cost1)

elif(best_cost2<best_cost1 and best_cost2<best_cost3):
    print(f"Threfore the Best path is from {start_node2} to {goal_node2} = {' -> '.join(best_path2)}")
    print("Best Cost =",best_cost2)
elif(best_cost3<best_cost1 and best_cost3<best_cost2):
    print(f"Threfore the Best path is from {start_node2} to {goal_node2} = {' -> '.join(best_path3)}")
    print("Best Cost =",best_cost3)  