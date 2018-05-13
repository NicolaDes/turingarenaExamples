import random
import collections
from collections import defaultdict

from turingarena import *

all_passed = True


def evaluate(algorithm):
    i = 10
    for _ in range(1, 10):
        N = random.randint(5, i)
        M = random.randint(1, i*10)
        K = random.randint(1, i/2)

        # Graph generation
        supermercati = [
            random.randint(1, N)
            for _ in range(0, K)
        ]
        da = [
            random.randint(1, N)
            for _ in range(0, M)
        ]
        a = [
            random.randint(1, N)
            for _ in range(0, M)
        ]

        ret = compute(algorithm, N, M, K, supermercati, da, a)
        correct = solve(N, M, K, supermercati, da, a)
        if ret == correct:
            print(f"size: {i} -- > (correct)")
        else:
            print(f"size: {i} -- > {ret}!={correct}(wrong)")
            all_passed = False
        i = i + 20


def compute(algorithm, N, M, K, supermercati, da, a):
    with algorithm.run() as process:
        return process.call.compra(N, M, K, supermercati, da, a)


def solve(N, M, K, supermercati, da, a):

    edges = [None]*M
    for i in range(0, M):
        edges[i] = (da[i], a[i])

    distanceSource = [0]*(N+1)
    distanceTarget = [0]*(N+1)

    bfs(1, distanceSource, edges)
    bfs(N, distanceTarget, edges)

    cost_path = -1

    for i in range(0, K):
        cost = distanceSource[supermercati[i]]+distanceTarget[supermercati[i]]
        if cost_path == -1 or cost < cost_path:
            cost_path = cost

    return cost_path


def bfs(s, distance, edges):
    g = defaultdict(list)
    for l, r in edges:
        g[l].append((r))
        g[r].append((l))

    visited, queue = set(), collections.deque([s])
    distance[s] = 0
    visited.add(s)
    while queue:
        v = queue.popleft()
        for n in g[v]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
                distance[n] = distance[v]+1


algorithm = submitted_algorithm()


evaluate(algorithm)
