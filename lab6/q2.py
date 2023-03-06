import random

def f(x):
    return x**3 - 4*x**2 + 3*x + 1

def hill_climbing():
    current_node = random.uniform(-10, 10)
    step_size = 0.1
    max_iterations = 1000
    for i in range(max_iterations):
        current_value = f(current_node)
        neighbor = current_node + random.uniform(-step_size, step_size)
        neighbor_value = f(neighbor)
        if neighbor_value < current_value:
            current_node = neighbor
    return f(current_node)

print(hill_climbing())
