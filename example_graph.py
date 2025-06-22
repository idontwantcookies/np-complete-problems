from graph import Graph, Vertex, Edge


a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
d = Vertex("d")
e = Vertex("e")
f = Vertex("f")
g = Vertex("g")

G = Graph(
    [a, b, c, d, e, f, g],
    [
        Edge(a, b),
        Edge(a, c),
        Edge(a, d),
        Edge(a, f),
        Edge(b, d),
        Edge(b, e),
        Edge(b, g),
        Edge(c, f),
        Edge(d, f),
        Edge(d, g),
        Edge(e, g),
        Edge(f, g)
    ]
)
