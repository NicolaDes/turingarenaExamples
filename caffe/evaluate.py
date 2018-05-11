import random

from turingarena import *

all_passed = True

def evaluate(algorithm):
    i = 10
    for _ in range(1, 10):
        N = random.randint(2, i)
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
            print(f"size: {i} -- > (correct)")
        else:
            print(f"size: {i} -- > {ret}!={correct}(wrong)")
            all_passed = False
        i = i + 20
    

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

