import random
import collections
from collections import defaultdict
import itertools
import networkx as nx

from turingarena import *

Tasks = [False] * 5


def evaluate(algorithm):

    # Task1
    N = random.randint(0, 100)
    M = random.randint(5, 200)
    pairs = set()
    for e in range(0,M):
        pairs.add((e,random.randint(e+1,M)))
    M = len(pairs)
    A=[
        item[0]
        for item in pairs
    ]
    B=[
        item[1]
        for item in pairs
    ]
    end = [1]*N
    for i in range(0,M):
        end[A[i]]=0
    P = 0
    for i in range(0,M):
        P=P+end[i]

    request = compute(algorithm,N,M,P,A,B)
    print(request)

def convert_dag_to_array(DAG, A, B):
    A = [
        item[0]
        for item in DAG.edges()
    ]
    B = [
        item[1]
        for item in DAG.edges()
    ]


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


def compute(algorithm, N, M, P, A, B):
    with algorithm.run() as process:
        return process.call.find_pool(N, M, P, A, B)


# ----------- Solution code -----------
def solve(N, M, P, A, B):
    edges = [None]*M
    for i in range(0, M):
        edges[i] = (A[i], B[i])
    g = defaultdict(list)
    for l, r in edges:
        g[l].append((r))
    topological = []
    visited = [False]*N

    dfs(0, g, topological, visited)

    cumulate = [0.0]*N
    cumulate[0] = 1.0

    for i in range(N-1, -1, -1):
        prop = cumulate[topological[i]]/len(g[topological[i]])
        cumulate[topological[i]] = 0.0
        for x in g[topological[i]]:
            cumulate[x] = cumulate[x]+prop
    return cumulate


def dfs(s, adj, topological, visited):
    if visited[s]:
        return
    visited[s] = True
    for x in adj[s]:
        dfs(x, adj, topological, visited)
    topological.append(s)
# ----------- Solution code -----------


algorithm = submitted_algorithm()


evaluate(algorithm)
