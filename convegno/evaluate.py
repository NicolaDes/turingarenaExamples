import random
import collections
from collections import defaultdict

from turingarena import *

Task = [False]*4


def evaluate(algorithm):
    # Task 2

    for i in range(0, 10):
        N = random.randint(2, 200)
        direttore = random.randint(0, N-1)
        pairs = [None]*N
        for i in range(0, N):
            a = random.randint(0, N-1)
            b = random.randint(0, N-1)
            if a != b:
                pairs[i] = (a, b)
            else:
                pairs[i] = (1, 0)

        C = [0]*N
        for item in pairs:
            C[item[0]] = item[1]
        C[direttore] = -1
    
        ret = compute(algorithm, N, C)
        print(ret)


def compute(algorithm, N, C):
    with algorithm.run() as process:
        return process.call.coppie(N, C)


algorithm = submitted_algorithm()


evaluate(algorithm)
