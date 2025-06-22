from graph import Graph, Vertex, Edge, Path
from example_graph import G

def valid_color(u: Vertex, c: int) -> bool:
    if c == -1: return False
    for v in u.adj:
        if c == v.color: return False
    return True


def k_color(u: Vertex, k: int) -> bool:
    colors = set(range(k))
    for v in u.adj:
        if v.color in colors: colors.remove(v.color)
    if colors == []: return False
    for c in colors:
        u.color = c
        for v in u.adj:
            if v.color != -1: continue
            if not k_color(v, k): break
        else:
            return True
    else:
        u.color = -1
        return False

v = G.get_vertex("a")
if v is None: raise RuntimeError("Vertice não encontrado")
result = k_color(v, 3)
print(result)
for v in G.V:
    print(v.label, v.color)
