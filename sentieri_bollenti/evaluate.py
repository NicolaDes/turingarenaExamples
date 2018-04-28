import random
from collections import defaultdict
from heapq import *

def evaluate(algorithm):
    for _ in range(1, 10):
        N = random.randint(5, 100)
        A = random.randint(1, 9)
        B = random.randint(A, 10)
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

    slave = compute(algorithm, N, M, A, B, da, a)
    master = solve(N, M, A, B, da, a)

    if master == slave:
        print("Correct!")
    else:
        print("WRONG!")

def compute(algorithm, N, M, A, B, da, a):
    with algorithm.run() as process:
        memory_usage = process.sandbox.get_info().memory_usage
        memory_usage = (memory_usage/1024)/1024
        # print(f"memory usage: {memory_usage} MB")
        return process.call.minimize(N, M, A, B, da, a)


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
                print (cost, path)
                return cost  # (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")
