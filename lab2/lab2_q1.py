class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def addEdge(self, u, v):
        self.adj[u].append(v)

    def printGraph(self):
        for i in range(self.V):
            print(i, "--->", end=" ")
            for j in self.adj[i]:
                print(j, end=" ")
            print("")

if __name__ == '__main__':
    
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0) 
    g.addEdge(2, 1)
    g.addEdge(3, 2)
    g.addEdge(4, 5)
    g.addEdge(5, 4)
    g.printGraph()

