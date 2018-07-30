import random
import collections
from collections import defaultdict
import networkx as nx

from turingarena import *

Task = [True]*4


def evaluate():

    # Task 2

    for i in range(0, 10):
        N = random.randint(3, 100)
        M = random.randint(N-1, N*N)
        K = random.randint(1, N-2)
        assert(K >= 1)

        random_list = [
            i
            for i in range(0, N)
        ]
        random.shuffle(random_list) # random.sample(range(N),K)
        # Graph generation
        supermercati = random_list[0:K]
        G = nx.gnm_random_graph(N+1, M) #gnp, (unione tra albero e grafo generato networkx)

        M = len(G.edges())
        da = [
            item[0]
            for item in G.edges()
        ]
        a = [
            item[1]
            for item in G.edges()
        ]

        ret = compute(N, M, K, supermercati, da, a)
        correct = solve(N, M, K, supermercati, da, a)
        if ret == correct:
            print(f"Task 2 -- > (correct)")
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)")
            Task[2] = False
    
    # Task 3

    for i in range(0, 1):
        N = random.randint(3, 10000)
        M = random.randint(N-1,100000)
        K = random.randint(1, 10)
        assert(K >= 1)

        random_list = [
            i
            for i in range(0, N)
        ]
        random.shuffle(random_list)
        # Graph generation
        supermercati = random_list[0:K]
        G = nx.gnm_random_graph(N+1, M)

        M = len(G.edges())
        da = [
            item[0]
            for item in G.edges()
        ]
        a = [
            item[1]
            for item in G.edges()
        ]
        ret = compute(N, M, K, supermercati, da, a)
        correct = solve(N, M, K, supermercati, da, a)
        if ret == correct:
            print(f"Task 3 -- > (correct)")
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)")
            Task[3] = False

    # Task 4

    for i in range(0, 1):
        N = random.randint(3, 10000)
        M = random.randint(N-1,100000)
        K = random.randint(1, N-2)
        assert(K >= 1)

        random_list = [
            i
            for i in range(0, N)
        ]
        random.shuffle(random_list)
        # Graph generation
        supermercati = random_list[0:K]
        G = nx.gnm_random_graph(N+1, M)

        M = len(G.edges())
        da = [
            item[0]
            for item in G.edges()
        ]
        a = [
            item[1]
            for item in G.edges()
        ]
        ret = compute(N, M, K, supermercati, da, a)
        correct = solve(N, M, K, supermercati, da, a)
        if ret == correct:
            print(f"Task 4 -- > (correct)")
        else:
            print(f"Task 4 -- > {ret}!={correct}(wrong)")
            Task[3] = False


def compute(N, M, K, supermercati, da, a):
    try:
        with run_algorithm(submission.source) as process:
            return process.functions.compra(N, M, K, supermercati, da, a)
    except AlgorithmError as e:
        print(e)
        return -1


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

evaluate()
