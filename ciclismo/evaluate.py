import random
import collections
from collections import defaultdict
import networkx as nx

from turingarena import *

Task = [False] * 4


def generate_random_dag(n, m):
    random_graph = nx.gnm_random_graph(n, m, directed=True)
    random_dag = nx.DiGraph(
        [
            (u, v) for (u, v) in random_graph.edges() if u < v
        ]
    )
    source_exist = False
    for item in random_dag.edges():
        if item[0] == 0:
            source_exist = True
    if not source_exist:
        random_dag.add_edge(0, random.randint(1, n))
    return random_dag


def evaluate(algorithm):

    # Task 2
    for i in range(0, 10):
        N = random.randint(2, 10)
        M = random.randint(1, 100000)

        G = generate_random_dag(N-1, M-1)

        M = len(G.edges())

        # Graph generation
        H = [
            random.randint(1, 1000000)
            for _ in range(0, N)
        ]
        da = [
            item[0]
            for item in G.edges()
        ]
        a = [
            item[1]
            for item in G.edges()
        ]

        ret = compute(algorithm, N, M, H, da, a)
        correct = solve(N, M, H, da, a)
        if ret == correct:
            print(f"Task 2 -- > (correct)")
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)")
            Task[2]=False

    # Task 3
    for i in range(0, 5):
        N = random.randint(2, 100)
        M = random.randint(1, 100000)

        G = generate_random_dag(N-1, M-1)

        M = len(G.edges())

        # Graph generation
        H = [
            random.randint(1, 1000000)
            for _ in range(0, N)
        ]
        da = [
            item[0]
            for item in G.edges()
        ]
        a = [
            item[1]
            for item in G.edges()
        ]

        ret = compute(algorithm, N, M, H, da, a)
        correct = solve(N, M, H, da, a)
        if ret == correct:
            print(f"Task 3 -- > (correct)")
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)")
            Task[3]=False

    # Task 4
    for i in range(0, 2):
        N = random.randint(2, 10000)
        M = random.randint(1, 100000)

        G = generate_random_dag(N-1, M-1)

        M = len(G.edges())

        # Graph generation
        H = [
            random.randint(1, 1000000)
            for _ in range(0, N)
        ]
        da = [
            item[0]
            for item in G.edges()
        ]
        a = [
            item[1]
            for item in G.edges()
        ]

        ret = compute(algorithm, N, M, H, da, a)
        correct = solve(N, M, H, da, a)
        if ret == correct:
            print(f"Task 4 -- > (correct)")
        else:
            print(f"Task 4 -- > {ret}!={correct}(wrong)")
            Task[4]=False


def compute(algorithm, N, M, H, da, a):
    with algorithm.run() as process:
        return process.call.pedala(N, M, H, da, a)


def solve(N, M, H, da, a):
    g = defaultdict(list)
    for i in range(0,M):
        g[da[i]].append((a[i]))
        g[a[i]].append((da[i]))

    visited = set()
    sol = dfs(0, H, -1, visited, g)
    return sol


def dfs(curr, H, last, visited, adj):
    visited.add(curr)
    min_so_far = 1000000
    n = -1
    for x in adj[curr]:
        if H[x] < min_so_far and x != last:
            min_so_far = H[x]
            n = x
    if n == -1:
        return curr
    elif n not in visited:
        return dfs(n, H, curr, visited, adj)
    elif n in visited:
        return n


algorithm = submitted_algorithm()


evaluate(algorithm)
