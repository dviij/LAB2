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

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0,0, 1)
    g.add_edge(0,1, 2)
    g.add_edge(0,2, 0)
    g.add_edge(0,2, 1)
    g.add_edge(0,3, 2)
    g.add_edge(0,4, 5)
    g.add_edge(0,5, 4)
    g.print_graph()