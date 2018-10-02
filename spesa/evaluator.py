import random
import collections
from collections import defaultdict
import networkx as nx

from turingarena import *


def create_random_instance(n):
    N = random.randint(3, n)
    M = random.randint(N-1, 100000)
    K = random.randint(1, N-2)
    assert(K >= 1)
    random_list = [
        i
        for i in range(0, N)
    ]
    random.shuffle(random_list)  # random.sample(range(N),K)
    # Graph generation
    supermercati = random_list[0:K]
    # gnp, (unione tra albero e grafo generato networkx)
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
    return [N, M, K, supermercati, da, a]

def run(algorithm, N, M, K, supermercati, da, a):
    with run_algorithm(algorithm) as process:
        ret = process.functions.compra(N, M, K, supermercati, da, a)
    print(f"Time usage: {process.time_usage}")
    return ret


def get_opt_cpp(N, M, K, supermercati, da, a):
    corretc_algo = os.environ["PWD"]+"/solutions/correct.cpp"
    return run(corretc_algo, N, M, K, supermercati, da, a)


def get_opt(N, M, K, supermercati, da, a):

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


def main():
    algorithm = submission.source
    goals = {
        "exponential": True,
        "quadratic": True,
        "n_log_n": True,
    }

    for gs, ns in [
        (["exponential", "quadratic", "n_log_n"], [100] * 3),
        (["quadratic", "n_log_n"], [1000]),
        (["n_log_n"], [10000]),
    ]:
        for n in ns:
            if not any(goals[g] for g in gs):
                break

            print(f"Testing n={n}")
            [N, M, K, supermercati, da,a] = create_random_instance(n)
            opt = get_opt_cpp(N, M, K, supermercati, da,a)
            try:
                submitted = run(algorithm, N, M, K, supermercati, da,a)
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
