from typing import Generator


def valid(n: int, X: list) -> bool:
    if len(set(X)) != n: return False
    for i in range(1, len(X)):
        if X[i] == X[i-1] + 1 or X[i] == X[i-1] - 1: return False
    return True


def promising(n: int, X: list) -> Generator[int]:
    last = X[-1] if X else -1
    for i in range(1, n+1):
        if i in X + [last - 1, last + 1]:
            continue
        else:
            yield i


def queens_backtrack(n: int, X: list = []) -> int:
    if len(X) < n:
        count = 1
        for i in promising(n, X):
            count += queens_backtrack(n, X + [i])
        return count
    if valid(n, X):
        print(X)
    return 1

def queens_exaustive(n: int, X: list = []) -> int:
    if len(X) < n:
        count = 1
        for i in range(1, n+1):
            count += queens_exaustive(n, X + [i])
        return count
    if valid(n, X):
        print(X)
    return 1

N_QUEENS = 4
print(queens_backtrack(N_QUEENS))
print(queens_exaustive(N_QUEENS))
