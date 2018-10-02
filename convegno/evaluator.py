import random
import collections
from collections import defaultdict

from turingarena import *

def generate_unbalanced_tree(source, C, N):

    choosen = set()
    choosen.add(source)

    for i in range(0, N):
        if i not in choosen and i != source:
            x = random.sample(choosen, 1)[0]
            C[i] = x
            choosen.add(i)


def create_random_instance(n):
    N = random.randint(2, n)
    direttore = random.randint(0, N-1)
    C = [-1]*N
    generate_unbalanced_tree(direttore, C, N)
    return [N, C, direttore]


def run(algorithm, N, C):
    with run_algorithm(algorithm) as process:
        ret = process.functions.coppie(N, C)
    print(f"Time usage: {process.time_usage}")
    return ret


def get_opt_cpp(N, C):
    corretc_algo = os.environ["PWD"]+"/solutions/correct.cpp"
    return run(corretc_algo, N, C)


def get_opt(N, C, direttore):
    adj = defaultdict(list)
    for i in range(0, N):
        if i != direttore:
            adj[C[i]].append((i))
    cumulate = [0]*N
    cumulate[direttore] = -1
    dfs(direttore, direttore, cumulate, adj)
    sum = 0
    for i in range(0, N):
        sum = sum+cumulate[i]

    return sum


def dfs(s, e, cumulate, adj):
    cumulate[s] = cumulate[e]+1
    for u in adj[s]:
        dfs(u, s, cumulate, adj)


def main():
    algorithm = submission.source
    goals = {
        "exponential": True,
        "quadratic": True,
        "n_log_n": True,
    }

    for gs, ns in [
        (["exponential", "quadratic", "n_log_n"], [200] * 3),
        (["quadratic", "n_log_n"], [5000]),
        (["n_log_n"], [10000]),
    ]:
        for n in ns:
            if not any(goals[g] for g in gs):
                break

            print(f"Testing n={n}")
            [N, C, direttore] = create_random_instance(n)
            opt = get_opt_cpp(N, C)
            try:
                submitted = run(algorithm, N, C)
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
