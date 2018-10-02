import random
import collections
from collections import defaultdict
import networkx as nx

from turingarena import *


def create_random_instance(n):
    N = random.randint(2, n)
    M = random.randint(1, 4*N)
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

    return [N,M,conoscenzeA, conoscenzeB]

def run(algorithm, N, M, conoscenzeA, conoscenzeB):
    with run_algorithm(submission.source) as process:
        ret= process.functions.invita(N, M, conoscenzeA, conoscenzeB)
    print(f"Time usage: {process.time_usage}")
    return ret

def get_opt_cpp(N,M,conoscenzeA, conoscenzeB):
    corretc_algo = os.environ["PWD"]+"/solutions/correct.cpp"
    return run(corretc_algo, N,M,conoscenzeA,conoscenzeB)

def get_opt(N, M, conoscenzeA, conoscenzeB):
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

def main():
    algorithm = submission.source
    goals = {
        "exponential": True,
        "quadratic": True,
        "n_log_n": True,
    }

    for gs, ns in [
        (["exponential", "quadratic", "n_log_n"], [10] * 3),
        (["quadratic", "n_log_n"], [1000]),
        (["n_log_n"], [10000]),
    ]:
        for n in ns:
            if not any(goals[g] for g in gs):
                break

            print(f"Testing n={n}")
            [N, M, conoscenzeA, conoscenzeB] = create_random_instance(n)
            opt = get_opt_cpp(N, M, conoscenzeA, conoscenzeB)
            try:
                submitted = run(algorithm, N, M, conoscenzeA, conoscenzeB)
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
