class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}:".format(i), end=" ")
            for j, w in self.adj[i]:
                print("({} —> {}, {})".format(i, j, w), end=" ")
            print("")

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 6)
    g.add_edge(1, 2, 7)
    g.add_edge(2, 0, 5)
    g.add_edge(2, 1, 4)
    g.add_edge(3, 2, 10)
    g.add_edge(4, 5, 1)
    g.add_edge(5, 4, 3)
    g.print_graph()
