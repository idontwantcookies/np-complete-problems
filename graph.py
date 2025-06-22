class Vertex:
    def __init__(self, label: str):
        self.label: str = label
        self.adj: list["Vertex"] = []
        self.visited: bool = False
        self.color: int = -1
    
    def __eq__(self, other: "Vertex") -> bool:
        return self.label == other.label


class Edge:
    def __init__(self, u: Vertex, v: Vertex):
        if u.label > v.label: u, v = v, u
        self.u: Vertex = u
        self.v: Vertex = v
        self.visited: bool = False

    def __eq__(self, other: "Edge") -> bool:
        return (self.u, self.v) == (other.u, other.v)


Path = list[Vertex]

class Graph:
    def __init__(self, V: list[Vertex], E: list[Edge]):
        self.V: list[Vertex] = V
        self.E : list[Edge] = []
        for e in E:
            self.add_edge(e)
    
    def add_edge(self, e: Edge):
        e.u.adj.append(e.v)
        e.v.adj.append(e.u)
        self.E.append(e)
    
    def get_edge(self, u: Vertex, v: Vertex) -> Edge | None:
        if u.label > v.label:
            u, v = v, u
        for e in self.E:
            if e.u.label > u.label: return
            if e.u == u and e.v == v:
                return e

    def get_vertex(self, label: str) -> Vertex | None:
        for v in self.V:
            if v.label == label:
                return v
