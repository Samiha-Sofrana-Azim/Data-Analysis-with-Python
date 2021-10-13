class Vertex:

    def __init__(self, label):
        self.label = label
        self.edges = []
        self.step = -1

    def add_neighbour(self, edge):
        self.edges.append(edge)


class Edge:

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2