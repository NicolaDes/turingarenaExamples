import random
import collections
from collections import defaultdict
import networkx as nx

from turingarena import *

Task = [True]*4


def evaluate():

    # Task 2

    for i in range(0, 10):
        N = random.randint(2, 10)
        M = random.randint(1, N*N)  # metti 2n anzichè n^2

        G = nx.gnm_random_graph(N, M)

        M = len(G.edges())

        conoscenzeA = [
            item[0]
            for item in G.edges()
        ]
        conoscenzeB = [
            item[1]
            for item in G.edges()
        ]

        ret = compute(N, M, conoscenzeA, conoscenzeB)
        correct = solve(N, M, conoscenzeA, conoscenzeB)
        if ret == correct:
            print(f"Task 2 -- > (correct)")
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)")
            Task[2] = False

    # Task 3

    for i in range(0, 2):
        N = random.randint(2, 1000)
        M = random.randint(1, 100000)

        G = nx.gnm_random_graph(N, M)

        M = len(G.edges())

        conoscenzeA = [
            item[0]
            for item in G.edges()
        ]
        conoscenzeB = [
            item[1]
            for item in G.edges()
        ]

        ret = compute(N, M, conoscenzeA, conoscenzeB)
        correct = solve(N, M, conoscenzeA, conoscenzeB)
        if ret == correct:
            print(f"Task 3 -- > (correct)")
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)")
            Task[3] = False

    # Task 4

    for i in range(0, 1):
        N = random.randint(2, 10000)
        M = random.randint(1, 100000)

        G = nx.gnm_random_graph(N, M)

        M = len(G.edges())

        conoscenzeA = [
            item[0]
            for item in G.edges()
        ]
        conoscenzeB = [
            item[1]
            for item in G.edges()
        ]

        ret = compute(algorithm, N, M, conoscenzeA, conoscenzeB)
        correct = solve(N, M, conoscenzeA, conoscenzeB)
        if ret == correct:
            print(f"Task 4 -- > (correct)")
        else:
            print(f"Task 4-- > {ret}!={correct}(wrong)")
            Task[4] = False


def compute(N, M, conoscenzeA, conoscenzeB):
    try:
        with run_algorithm(submission.source) as process:
            return process.functions.invita(N, M, conoscenzeA, conoscenzeB)
    except AlgorithmError as e:
        print(e)
        return -1


def solve(N, M, conoscenzeA, conoscenzeB):
    degree = [0]*(N)
    g = defaultdict(list)
    for i in range(0, M):
        g[conoscenzeA[i]].append((conoscenzeB[i]))
        g[conoscenzeB[i]].append((conoscenzeA[i]))
        degree[conoscenzeA[i]] = degree[conoscenzeA[i]]+1
        degree[conoscenzeB[i]] = degree[conoscenzeB[i]]+1
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

evaluate()
