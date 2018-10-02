import random
import collections
from collections import defaultdict
import networkx as nx

from turingarena import *


def generate_random_dag(n, m):
    random_graph = nx.gnm_random_graph(
        n, m, directed=True)
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


def create_random_instance(n):
    N = random.randint(2, n)
    M = random.randint(1, 10000)

    G = generate_random_dag(N-1, M-1)
    M = len(G.edges())

    H = [
        random.randint(1, 100000)
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
    return [N, M, H, da, a]


def run(algorithm, N, M, H, da, a):
    with run_algorithm(algorithm) as process:
        ret = process.functions.pedala(N, M, H, da, a)
    print(f"Time usage: {process.time_usage}")
    return ret



def get_opt_cpp(N,M,H,da,a):
    correct_algo = os.environ["PWD"]+"/solutions/correct.cpp"
    return run(correct_algo,N,M,H,da,a)

def get_opt(N, M, H, da, a):
    g = defaultdict(list)
    for i in range(0, M):
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


def main():
    algorithm = submission.source
    goals = {
        "exponential": True,
        "quadratic": True,
        "linear": True,
    }

    for gs, ns in [
        (["exponential", "quadratic", "linear"], [10] * 3),
        (["quadratic", "linear"], [100]),
        (["linear"], [1000]),
    ]:
        for n in ns:
            if not any(goals[g] for g in gs):
                break

            print(f"Testing n={n}")
            [N, M, H, da, a] = create_random_instance(n)
            opt = get_opt_cpp(N, M, H, da, a)
            try:
                submitted = run(algorithm, N, M, H, da, a)
            except AlgorithmError as e:
                print("Error:", e)
                correct = False
            else:
                print("Your solution:", submitted)
                print("Optimal solution:", opt)
                correct = (
                    opt == submitted
                )
                print("Correct:", correct)
            if not correct:
                for g in gs:
                    goals[g] = False
            print("------------------")
    evaluation.data(dict(goals=goals))


if __name__ == "__main__":
    main()
