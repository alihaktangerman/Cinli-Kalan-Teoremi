from functools import reduce
from math import gcd


def solve(a, b):
    assert(gcd(a[1], b[1]) == 1)
    if not 0 <= a[0] < a[1]: a[0] %= a[1]
    if not 0 <= b[0] < b[1]: b[0] %= b[1]
    for i in range(a[0], a[1]*b[1], a[1]):
        if i % b[1] == b[0]:
            return i, a[1]*b[1]


def crt(*args): return reduce(solve, args)


print(crt((1, 2), (2, 3), (3, 5)))
