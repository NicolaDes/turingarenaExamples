import random
import networkx as nx

def evaluate(algorithm):

    for _ in range(1, 10):
        N = random.randint(5, 100)
        A = random.randint(10,999)
        B = random.randint(A,1000)
        M = A+B
        da = [
            random.randint(1,N)
            for _ in range(0,A+B)
        ]
        a = [
            random.randint(1,N)
            for _ in range(0,A+B)
        ]

        ret = compute(algorithm, N, M, A, B, da, a)
        if ret == solve(N, M, A, B, da, a):
            print("correct!")
        else:
            print("WRONG!")
    

def compute(algorithm, N, M, A, B, da, a):
    with algorithm.run() as process:
        memory_usage = process.sandbox.get_info().memory_usage
        memory_usage = (memory_usage/1024)/1024
        print(f"memory usage: {memory_usage} MB")
        return process.call.minimize(N, M, A, B,da,a)


def solve(N, M, A, B, da, a):
    G = nx.Graph()
    for i in range(0,A):
        G.add_edge(da[i],a[i],0)
    for i in range(A,A+B):
        G.add_edge(da[i],a[i],1)
    print(nx.dijkstra_path(G,1,N))
