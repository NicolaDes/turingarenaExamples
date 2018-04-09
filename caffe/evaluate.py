import random

def evaluate(algorithm):

    for _ in range(1, 10):
        N = random.randint(2, 50)
        A = [
            random.randint(0, N-1)
            for _ in range(0, N)
        ]
        B = [
            random.randint(A[_], N)
            for _ in range(0, N)
        ]
        ret = compute(algorithm, N, A, B)
        if ret == solve(N, A, B):
            print("correct!")
        else:
            print("WRONG!")
    

def compute(algorithm, N, A, B):
    with algorithm.run() as process:
        memory_usage = process.sandbox.get_info().memory_usage
        memory_usage = (memory_usage/1024)/1024
        print(f"memory usage: {memory_usage} MB")
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
