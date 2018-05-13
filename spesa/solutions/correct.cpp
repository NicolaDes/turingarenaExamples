#include <stdio.h>
#include <assert.h>
#include <vector>
#include <list>
#include <bits/stdc++.h>

#define MAXK 10000
#define MAXM 100000
#define MAXN 10001

std::vector<int> adj[MAXN + 1];
bool visited[MAXN + 1];

void bfs(int src, int distance[])
{
    std::list<int> Q;
    Q.push_back(src);
    visited[src] = true;
    distance[src] = 0;

    while (!Q.empty())
    {
        int node = Q.front();
        Q.pop_front();

        for (auto x : adj[node])
        {
            if (!visited[x])
            {
                visited[x] = true;
                distance[x] = distance[node] + 1;
                Q.push_back(x);
            }
        }
    }
}

int compra(int N, int M, int K, int supermercati[], int da[], int a[])
{

    int distanceSource[MAXN];
    int distanceTarget[MAXN];

    memset(distanceSource, 0, MAXN);
    memset(distanceTarget, 0, MAXN);

    int cost_path = 2 * MAXM;

    for (int i = 0; i < M; ++i)
    {
        adj[da[i]].push_back(a[i]);
        adj[a[i]].push_back(da[i]);
    }

    memset(visited, false, MAXN);
    bfs(1, distanceSource);
    memset(visited, false, MAXN);
    bfs(N, distanceTarget);

    for (int i = 0; i < K; ++i)
    {
        int cost = distanceSource[supermercati[i]] + distanceTarget[supermercati[i]];
        cost_path = (cost < cost_path) ? cost : cost_path;
    }

    return cost_path;
}