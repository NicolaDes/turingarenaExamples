import collections
from collections import defaultdict
import itertools

from turingarena import *

all_passed = True

def evaluate(algorithm):
    for i in range(100, 2000,100):
        N = random.randint(5, i)
        M = random.randint(1, N)

        nodes = [
            _
            for _ in range(0, N)
        ]

        pairs = list(itertools.combinations(nodes, 2))

        random.shuffle(pairs)

        # Graph generation
        conoscenzeA = [
            item[0]
            for item in pairs[:M]
        ]
        conoscenzeB = [
            item[1]
            for item in pairs[:M]
        ]

        ret = compute(algorithm, N, M, conoscenzeA, conoscenzeB)
        correct = solve(N, M, conoscenzeA, conoscenzeB)
        if ret == correct:
            print(f"size: {i} -- > (correct)")
        else:
            print(f"size: {i} -- > {ret}!={correct}(wrong)")
            all_passed = False


def compute(algorithm, N, M, conoscenzeA, conoscenzeB):
    with algorithm.run() as process:
        return process.call.invita(N, M, conoscenzeA, conoscenzeB)


def solve(N, M, conoscenzeA, conoscenzeB):
    edges = [None]*M
    degree = [0]*(N)
    for i in range(0, M):
        edges[i] = (conoscenzeA[i], conoscenzeB[i])
    g = defaultdict(list)
    for l, r in edges:
        g[l].append((r))
        g[r].append((l))
        degree[l] = degree[l]+1
        degree[r] = degree[r]+1
    for i in range(0, N):
        if degree[i] == 1:
            eatBorders(i, degree, g, N)
    result = 0
    for i in range(0, N):
        if degree[i] > 0:
            result = result+1

    return result


def eatBorders(s, degree, adj, N):
    for i in adj[s]:
        if degree[i] > 0:
            degree[i] = degree[i]-1
    degree[s] = degree[s]-1

    for i in range(0, N):
        if degree[i] == 1:
            eatBorders(i, degree, adj, N)


algorithm = submitted_algorithm()


evaluate(algorithm)
