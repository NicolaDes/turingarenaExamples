import random
import collections
from collections import defaultdict

from turingarena import *

Task = [False]*4


def generate_unbalanced_tree(source, C, N):
    remaining = [
        i
        for i in range(0, N)
        if i != source
    ]

    random.shuffle(remaining)

    choosen = set()
    choosen.add(source)

    for i in range(0, N):
        if i not in choosen and i != source:
            x = random.sample(choosen, 1)[0]
            C[i] = x
            choosen.add(i)


def evaluate(algorithm):

    # Task 2

    for i in range(0, 10):
        N = random.randint(2, 200)
        direttore = random.randint(0, N-1)
        C = [-1]*N
        generate_unbalanced_tree(direttore, C, N)

        request = compute(algorithm,N,C)
        correct = solve(N, C, direttore)
        if request == correct:
            print(f"Task 2 -- > (correct)")
        else:
            print(f"Task 2 -- > {request}!={correct}(wrong)")
            Task[2]=False

    # Task 3

    for i in range(0, 5):
        N = random.randint(2, 5000)
        direttore = random.randint(0, N-1)
        C = [-1]*N
        generate_unbalanced_tree(direttore, C, N)

        request = compute(algorithm,N,C)
        correct = solve(N, C, direttore)
        if request == correct:
            print(f"Task 3 -- > (correct)")
        else:
            print(f"Task 3 -- > {request}!={correct}(wrong)")
            Task[3]=False
    
    # Task 4

    for i in range(0, 2):
        N = random.randint(2, 100000)
        direttore = random.randint(0, N-1)
        C = [-1]*N
        generate_unbalanced_tree(direttore, C, N)

        request = compute(algorithm,N,C)
        correct = solve(N, C, direttore)
        if request == correct:
            print(f"Task 4 -- > (correct)")
        else:
            print(f"Task 4 -- > {request}!={correct}(wrong)")
            Task[4]=False


def compute(algorithm, N, C):
    with algorithm.run() as process:
        return process.call.coppie(N, C)


def solve(N, C, direttore):
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


algorithm = submitted_algorithm()


evaluate(algorithm)
