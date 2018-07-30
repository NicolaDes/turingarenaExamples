import random

from turingarena import *

Task = [False]*4


def evaluate():
    # Task 2
    for _ in range(1, 10):
        N = random.randint(2, 10)
        A = [
            random.randint(0, N-1)
            for _ in range(0, N)
        ]
        B = [
            random.randint(A[_], N)
            for _ in range(0, N)
        ]
        ret = compute(N, A, B)
        correct = solve(N, A, B)
        if ret == correct:
            print(f"Task 2 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 2 -- > {ret}!={correct}(wrong)")

    # Task 3
    for _ in range(1, 5):
        N = random.randint(2, 1000)
        A = [
            random.randint(0, N-1)
            for _ in range(0, N)
        ]
        B = [
            random.randint(A[_], N)
            for _ in range(0, N)
        ]
        ret = compute(N, A, B)
        correct = solve(N, A, B)
        if ret == correct:
            print(f"Task 3 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 3 -- > {ret}!={correct}(wrong)")

    # Task 4
    for _ in range(1, 2):
        N = random.randint(2, 40000)
        A = [
            random.randint(0, N-1)
            for _ in range(0, N)
        ]
        B = [
            random.randint(A[_], N)
            for _ in range(0, N)
        ]
        ret = compute(N, A, B)
        correct = solve(N, A, B)
        if ret == correct:
            print(f"Task 4 -- > (correct)")
            Task[2] = True
        else:
            print(f"Task 4 -- > {ret}!={correct}(wrong)")


def compute(N, A, B):
    try:
        with run_algorithm(submission.source) as process:
            return process.functions.pausa(N, A, B)
    except AlgorithmError as e:
        print(e)
        return -1


def solve(N, A, B):
    T = [None]*2*N
    for i in range(0, N):
        T[i] = 2*A[i]+1
    for i in range(0, N):
        T[N+i] = 2*B[i]
    T.sort()
    for i in range(0, 2*N):
        T[i] %= 2
    c = 0
    caffe = 0
    for i in range(0, 2*N):
        if T[i] == 1:
            c = c+1
            caffe += c
        else:
            c = c-1
    return caffe


evaluate()
