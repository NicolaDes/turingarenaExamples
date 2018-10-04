import random

def create_random_instance(n):
    N = random.randint(2, n)
    A = [
        random.randint(0, N-1)
        for _ in range(0, N)
    ]
    B = [
        random.randint(A[_], N)
        for _ in range(0, N)
    ]
    return [N,A,B]