"""
Solução branch-and-bound do problema do knapsack.

Essa solução não deve ser usada em conjunto com paralelismo, pois ela faz uso de globais.
É fortemente recomendado que cada execução desse script seja feita em um processo separado.
"""

from generics import Number
from bitmask import Bitmask


best_mask: Bitmask = Bitmask(0, 0)
best_total: Number = 0


class Item:
    def __init__(self, weight: Number, value: Number):
        if weight == 0: raise ValueError("Peso não pode ser 0.")
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def reset_globals():
    global best_mask, best_total
    best_mask.mask = 0
    best_total = 0


def upper_bound(items: list[Item], C: Number, i: int, acc: Number) -> Number:
    # TODO: Melhorar essa função para achar um UB mais realista (considerando itens subsequentes)
    if i == len(items) - 1: return acc
    elif 0 <= i < len(items) - 1: return acc + items[i].value + (C - items[i+1].weight) * items[i+1].ratio
    else: raise IndexError(f"i deve estar entre 0 <= i < {len(items)}, mas foi recebido i={i}.")


def solve_knapsack(items: list[Item], C: Number):
    items.sort(key=lambda i: i.ratio, reverse=True)
    mask = Bitmask(len(items))
    solve_knapsack_aux(items, C, mask, 0, 0)


def solve_knapsack_aux(items: list[Item], C: Number, mask: Bitmask, i: int, acc: Number):
    global best_total, best_mask
    N = len(mask)

    if i == N:
        if acc > best_total:
            print(f"Novo ótimo encontrado: {acc}, {mask}")
            best_total, best_mask.mask = acc, mask.mask
        return

    if upper_bound(items, C, i, acc) <= best_total: return      # Não promissor
    if C >= items[i].weight:
        mask[i] = True
        solve_knapsack_aux(items, C - items[i].weight, mask, i+1, acc + items[i].value)
    mask[i] = False
    solve_knapsack_aux(items, C, mask, i+1, acc)


if __name__ == "__main__":
    # Problema 5 da seção 11.2 do livro do Levitin
    items = [
        Item(10, 100),
        Item(7, 63),
        Item(8, 56),
        Item(4, 12)
    ]
    C = 16
    solve_knapsack(items, C)
    print(best_total, best_mask)

    reset_globals()

    items = [
        Item(4, 40),
        Item(7, 42),
        Item(5, 25),
        Item(3, 12)
    ]
    C = 10
    solve_knapsack(items, C)
    print(best_total, best_mask)

    reset_globals()

