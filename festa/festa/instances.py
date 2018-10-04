import random
import networkx as nx


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

    return [N, M, conoscenzeA, conoscenzeB]
