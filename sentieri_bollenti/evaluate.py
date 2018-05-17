import random
from collections import defaultdict
from heapq import *
import itertools
from turingarena import *

all_passed = True
# assumptions
MAXN = 100
MAXM = 1000


def evaluate(algorithm):
    for i in range(10, MAXN, 10):
        N = random.randint(5, i)
        M = random.randint(1, N)
        A = random.randint(1, M)
        B = M-A
        nodes = [
            _
            for _ in range(0, N)
        ]

        pairs = list(itertools.combinations(nodes, 2))

        random.shuffle(pairs)

        # Graph generation
        da = [
            item[0]
            for item in pairs[:M]
        ]
        a = [
            item[1]
            for item in pairs[:M]
        ]


        # No sp from 1 to N, put it an hot one!
        if solve(N, M, A, B, da, a) == float("inf"):
            da[M-1]=1
            a[M-1]=N

        try:
            with algorithm.run() as process:
                sp_ = process.call.minimize(N, M, A, B, da, a)
        except AlgorithmError as e:
            print(f"{a} + {b} --> {e}")
            all_passed = False

        sp = solve(N, M, A, B, da, a)

        if sp == sp_:
            print(f"da: {1} a: {N} -- > (correct) [{sp}={sp_}]")
        else:
            print(f"da: {1} a: {N} -- > {sp}!={sp_} (wrong)")
            all_passed = False


def solve(N, M, A, B, da, a):
    edges = [None]*(M)
    for i in range(0, A):
        edges[i] = (da[i], a[i], 0)
    for i in range(A, M):
        edges[i] = (da[i], a[i], 1)
    return dijkstra(edges, 1, N)


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
        g[r].append((c, l))  # undirected graph

    q, seen = [], set()
    q.append((0, f))
    while q:
        (cost, v1) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            if v1 == t:
                return cost

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2))

    return float("inf")


algorithm = submitted_algorithm()

evaluate(algorithm)
