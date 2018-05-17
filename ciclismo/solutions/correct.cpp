#include <stdio.h>
#include <assert.h>
#include <vector>
#include <bits/stdc++.h>

#define MAXN 10001
#define MAXM 100001
#define MAXH 1000001

std::vector<int> adj[MAXN];
bool visited[MAXN];

int last_position = -1;

std::vector<int> path;

void dfs(int curr, int H[], int last)
{
    visited[curr] = true;
    path.push_back(curr);

    int min_so_far = MAXH;
    int next = -1;
    for (auto x : adj[curr])
    {
        if (H[x] < min_so_far && x != last)
        {
            min_so_far = H[x];
            next = x;
        }
    }

    if (next == -1)
    {
        last_position = curr;
        return;
    }
    last_position = next;
    if (!visited[next])
        dfs(next, H, curr);
}

int pedala(int N, int M, int H[], int da[], int a[])
{
    for (int i = 0; i < M; ++i)
    {
        adj[da[i]].push_back(a[i]);
        adj[a[i]].push_back(da[i]);
    }

    memset(visited, false, sizeof visited);

    dfs(0, H, -1);

    return last_position;
}
