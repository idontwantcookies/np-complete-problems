from random import random, seed
from statistics import mean

SEED = 0
MIN_SIZE = 2
MAX_SIZE = 50
REPETITIONS = 1000


class Item:
    def __init__(self, weight: float):
        if not (0 <= weight <= 1): raise ValueError("Peso deve estar entre 0 e 1.")
        self.weight = weight
        self.bin = -1


class BinPackingInstance:
    def __init__(self, *item_weights: float):
        self.pos = 0
        self.bins = []
        self.items = []
        self.N = len(item_weights)
        for w in item_weights:
            self.items.append(Item(w))

    def add_bin(self):
        self.bins.append(1)

    @property
    def B(self):
        return len(self.bins)

    @property
    def item(self):
        return self.items[self.pos]
    
    def put_item(self, item: Item, bin: int):
        if not (0 <= bin < self.B): raise ValueError("Caixa não existe.")
        if self.bins[bin] < item.weight: raise ValueError("Caixa não tem espaço suficiente.")
        item.bin = bin
        self.bins[bin] -= item.weight
    
    def print_items(self):
        for i, item in enumerate(self.items):
            print(i + 1, item.bin + 1, item.weight)


def bin_pack_first_fit(bpi: BinPackingInstance):
    for item in bpi.items:
        for bin, bin_capacity in enumerate(bpi.bins):
            if item.weight < bin_capacity:
                bpi.put_item(item, bin)
                break
        else:
            bpi.add_bin()
            bpi.put_item(item, bpi.B - 1)


def bin_packing_first_fit_decreasing(bpi: BinPackingInstance):
    bpi.items.sort(key=lambda item: item.weight, reverse=True)
    bin_pack_first_fit(bpi)


def random_weights(n: int) -> list[float]:
    weights = []
    for i in range(n):
        weights.append(random())
    return weights


def heuristics(weights: list[float]) -> float:
    bpi_ff = BinPackingInstance(*weights)
    bpi_ffd = BinPackingInstance(*weights)
    bin_pack_first_fit(bpi_ff)
    bin_packing_first_fit_decreasing(bpi_ffd)
    return bpi_ff.B / bpi_ffd.B


if __name__ == "__main__":
    bpi = BinPackingInstance(0.4, 0.7, 0.2, 0.1, 0.5)
    bin_pack_first_fit(bpi)
    bpi.print_items()

    print()

    bpi = BinPackingInstance(0.4, 0.7, 0.2, 0.1, 0.5)
    bin_packing_first_fit_decreasing(bpi)
    bpi.print_items()

    print()

    seed(SEED)
    global_results = {}
    for n in range(MIN_SIZE, MAX_SIZE):
        results = []
        for i in range(REPETITIONS):
            weights = random_weights(n)
            results.append(heuristics(weights))
        global_results[n] = mean(results)
    for n, avg in global_results.items():
        print(n, avg)
