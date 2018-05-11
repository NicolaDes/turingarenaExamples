import random
from collections import defaultdict
from heapq import *
from turingarena import *

all_passed = True
i = 10
def evaluate(algorithm):
    for _ in range(1, i):
        N = random.randint(5, 100)
        A = random.randint(1, 9)
        B = random.randint(A, i)
        M = A+B

        # Graph generation
        da = [
            random.randint(1, N)
            for _ in range(0, M)
        ]
        a = [
            random.randint(1, N)
            for _ in range(0, M)
        ]

    # No sp from 1 to N, put it an hot one!
    if solve(N, M, A, B, da, a) == float("inf"):
        da[M-1] = 1
        a[M-1] = N

    try:
        with algorithm.run() as process:
            sp_ = process.call.minimize(N, M, A, B, da, a)
    except AlgorithmError as e:
        print(f"{a} + {b} --> {e}")
        all_passed = False

    sp = solve(N, M, A, B, da, a)

    if sp == sp_:
        print(f"da: {1} a: {N} -- > (correct)")
    else:
        print(f"da: {1} a: {N} -- > {sp}!={sp_} (wrong)")
        all_passed = False

def solve(N, M, A, B, da, a):
    edges = [None]*(A+B)
    for i in range(0, A):
        edges[i] = (da[i], a[i], 0)
    for i in range(A, A+B):
        edges[i] = (da[i], a[i], 1)
    return dijkstra(edges, 1, N)


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
        g[r].append((c, l))  # undirected graph

    q, seen = [(0, f, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return cost  # (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")


algorithm = submitted_algorithm()

evaluate(algorithm)