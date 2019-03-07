#!/usr/bin/python3

from math import sqrt
from functools import lru_cache, reduce
from collections import Counter
from itertools import product

MUL = int.__mul__

def prime_factors(n):
    d = _divs(n)
    d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)

@lru_cache(maxsize=None)
def _divs(n):
    for i in range(2, int(sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]

def proper_divs(n):
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(1)
        divs.remove(n)
    except KeyError:
        pass
    return divs or (set())

def closest(divs, a):
    diff, sol = a, 1
    for i in divs:
        tmp = abs(a - i)
        if diff > tmp:
            diff, sol = tmp, i
    return sol

@lru_cache(maxsize=None)
def low_pairs(n):
    divs, a = proper_divs(n), int(sqrt(n))
    p = closest(divs, a)
    q = n // p
    p, q = min(p, q), max(p, q)
    return (p, q)

N = int(input())
for _ in range(N):
    n = int(input())
    p, q = low_pairs(n)
    print(p, q)
