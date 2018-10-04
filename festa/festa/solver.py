from collections import defaultdict


def solve(N, M, conoscenzeA, conoscenzeB):
    degree = [0]*(N)
    g = defaultdict(list)
    for i in range(0, M):
        g[conoscenzeA[i]].append((conoscenzeB[i]))
        g[conoscenzeB[i]].append((conoscenzeA[i]))
        degree[conoscenzeA[i]] = degree[conoscenzeA[i]]+1
        degree[conoscenzeB[i]] = degree[conoscenzeB[i]]+1
    for i in range(0, N):
        if degree[i] == 1:
            eatBorders(i, degree, g, N)
    result = 0
    for i in range(0, N):
        if degree[i] > 0:
            result = result+1

    return result


def eatBorders(s, degree, adj, N):
    for i in adj[s]:
        if degree[i] > 0:
            degree[i] = degree[i]-1
    degree[s] = degree[s]-1

    for i in range(0, N):
        if degree[i] == 1:
            eatBorders(i, degree, adj, N)
