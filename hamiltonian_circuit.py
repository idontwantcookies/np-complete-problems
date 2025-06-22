from graph import Vertex, Edge, Path, Graph
from example_graph import G


def valid_path(G: Graph, P: Path):
    n = len(P)
    if n != len(G.V): return False         # o caminho deve ter o mesmo número que arestas que o número de vértices de G
    for i in range(1, n):
        if P.index(P[i]) != i: return False
        if not G.get_edge(P[i-1], P[i]): return False
    if not G.get_edge(P[n-1], P[0]): return False
    return True

def hamiltonian_circuit(G, P: Path) -> Path | None:
    if P == []: raise ValueError("O caminho passado não pode ser vazio.")
    if valid_path(G, P):
        return P
    u = P[-1]
    u.visited = True
    for v in u.adj:
        if v.visited: continue
        circuit = hamiltonian_circuit(G, P + [v])
        if circuit: return circuit
    u.visited = False

c = G.get_vertex("c")
if c is None: raise RuntimeError("Vertice c faltando")
P = hamiltonian_circuit(G, [c])
if P:
    for u in P:
        print(u.label)
