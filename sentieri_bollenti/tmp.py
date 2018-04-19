import random

def evaluate():
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


    sp = solve(N, M, A, B, da, a)
    print(sp)


def solve(N, M, A, B, da, a):
    edges = [None]*(A+B)
    for i in range(0,A):
        edges[i]=(da[i],a[i],0)
    for i in range(A,A+B):
        edges[i]=(da[i],a[i],1)
    return dijkstra(edges,1,N)

def dijkstra(graph, source, target):
    queue = []
    visited = {}
    distance = {}
    shortest_distance = {}
    parent = {}
    
    for node in range(len(graph)):
        distance[node] = None
        visited[node] = False
        parent[node] = None
        shortest_distance[node] = float("inf")
    
    queue.append(source)
    distance[source] = 0
    while len(queue) != 0:
        current = queue.pop(0)
        visited[current] = True
        if current == target:
            break
        for neighbor in graph[current]:
            if visited[neighbor] == False:
                distance[neighbor] = distance[current] + 1
                if distance[neighbor] < shortest_distance[neighbor]:
                    shortest_distance[neighbor] = distance[neighbor]
                    parent[neighbor] = current
                    queue.append(neighbor)
    #print distance
    #print shortest_distance
    #print parent
    return target
    #return shortest_distance
        
   
evaluate()

