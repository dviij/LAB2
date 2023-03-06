class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbors(self, vertices):
        for vertex in vertices:
            if vertex not in self.neighbors:
                self.neighbors.append(vertex)
                vertex.neighbors.append(self)
        self.neighbors.sort(key=lambda x: x.name)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.name] = vertex

    def add_edge(self, vertex1, vertex2):
        vertex1.add_neighbors([vertex2])

    def adjacency_list(self):
        return {vertex: [v.name for v in self.vertices[vertex].neighbors] for vertex in self.vertices}

    def adjacency_matrix(self):
        vertex_names = sorted(self.vertices.keys())
        indices = {name: i for i, name in enumerate(vertex_names)}
        matrix = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]

        for vertex in self.vertices.values():
            for neighbor in vertex.neighbors:
                matrix[indices[vertex.name]][indices[neighbor.name]] = 1

        return matrix

def print_graph(g):
    print(g.adjacency_list())
    print()
    print(g.adjacency_matrix())

a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')

a.add_neighbors([b, c, e])
b.add_neighbors([a, c])
c.add_neighbors([b, d, a, e])
d.add_neighbors([c])
e.add_neighbors([a, c])

g = Graph()
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
g.add_edge(b, d)
print_graph(g)
