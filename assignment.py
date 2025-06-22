"""
TODO: Otimizações interessantes sugeridas pelo ChatGPT
1. Melhorar o “lower bound”
Em vez de, a cada nó, percorrer toda a matriz remanescente para achar o mínimo de cada linha (O(n²) por chamada), pré-calcule para cada linha uma lista ordenada de custos e vá extraindo o primeiro índice disponível em O(n) ou O(log n) via heap.
2. Redução de matriz (cost matrix reduction)
Na raiz, subtraia de cada linha o seu mínimo e depois de cada coluna o seu mínimo. Isso gera um bound inicial mais forte. Em cada desdobramento, atualize localmente essa redução em O(n) em vez de recalcular do zero.
3. Representação por bitmask em vez de listas
Use um inteiro de 64 bits (bitmask) para marcar colunas já escolhidas. Teste e defina bits em O(1), em vez de i in choices que é O(n).
4. Busca por solução inicial forte
Antes do backtracking, rode um algoritmo heurístico (por exemplo, solução gulosa ou o próprio algoritmo húngaro em O(n³)) para obter um upper bound realista, de modo a podar muito mais cedo no branch-and-bound.
"""


from math import inf
from random import randint


Number = int | float
Matrix = list[list[Number]]


    
def lower_bound(C: Matrix, choices: list[int], partial_sum: Number) -> Number:
    n = len(choices)
    for row in C[n:]:
        m = inf
        for i, c in enumerate(row):
            if i in choices: continue
            if c < m: m = c
        partial_sum += m
    return partial_sum


def assign(C: Matrix, choices: list[int], partial_sum: Number, optimal: Number) -> tuple[Number, list[int] | None]:
    if partial_sum >= optimal: return inf, None
    n = len(choices)
    if len(C) == len(choices): return partial_sum, choices
    child_bounds = []
    for i in range(len(C)):
        if i in choices: continue
        if partial_sum + C[n][i] >= optimal: continue
        lb = lower_bound(C, choices + [i], partial_sum + C[n][i])
        if lb >= optimal: continue
        child_bounds.append((lb, i))
    if child_bounds == []: return inf, None
    child_bounds.sort()
    best_cost = optimal
    best_choice_set = None
    for lb, i in child_bounds:
        if lb >= best_cost: continue
        cost, choice_set = assign(C, choices + [i], partial_sum + C[n][i], best_cost)
        if cost < best_cost:
            print("New best cost!", cost, choice_set)
            best_cost = cost
            best_choice_set = choice_set
    if best_cost < optimal:
        return best_cost, best_choice_set
    else:
        return inf, None

C: Matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

print(assign(C, [], 0, inf))

N = 20
C = []
for i in range(N):
    C.append([randint(0, 100) for j in range(N)])

print(lower_bound(C, [], 0))
print(assign(C, [], 0, inf))
