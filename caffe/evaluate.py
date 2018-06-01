import random

from turingarena import *

Task = [False]*4

def evaluate(algorithm):
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
        ret = compute(algorithm, N, A, B)
        correct = solve(N,A,B)
        if ret == correct:
            print(f"Task 2 -- > (correct)")
            Task[2]=True
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
        ret = compute(algorithm, N, A, B)
        correct = solve(N,A,B)
        if ret == correct:
            print(f"Task 3 -- > (correct)")
            Task[2]=True
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
        ret = compute(algorithm, N, A, B)
        correct = solve(N,A,B)
        if ret == correct:
            print(f"Task 4 -- > (correct)")
            Task[2]=True
        else:
            print(f"Task 4 -- > {ret}!={correct}(wrong)")
    

def compute(algorithm, N, A, B):
    with algorithm.run() as process:
        return process.call.pausa(N, A, B)


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


algorithm = submitted_algorithm()


evaluate(algorithm)

