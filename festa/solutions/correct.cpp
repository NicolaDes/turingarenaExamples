#include <stdio.h>
#include <assert.h>
#include <vector>
#include <list>
#include <bits/stdc++.h>


#define MAXM 100001
#define MAXN 10001

std::vector<int> adj[MAXN];
int degree[MAXN];

void dormammu(int curr, int N)
{
    for (auto x : adj[curr])
    {
        if (degree[x] > 0)
            degree[x]--;
    }
    degree[curr]--;

    /// Cercane un'altro da mangiare
    for (int x = 0; x < N; ++x)
    {
        if (degree[x] == 1)
            dormammu(x, N);
    }
}

int invita(int N, int M, int conoscenzeA[], int conoscenzeB[])
{
    memset(degree, 0, sizeof degree);

    for (int i = 0; i < M; ++i)
    {
        adj[conoscenzeA[i]].push_back(conoscenzeB[i]);
        adj[conoscenzeB[i]].push_back(conoscenzeA[i]);
        degree[conoscenzeA[i]]++;
        degree[conoscenzeB[i]]++;
    }
    for (int i = 0; i < N; ++i)
    {
        if (degree[i] == 1)
            dormammu(i, N);
    }

    int avengers = 0;
    for (int i = 0; i < N; ++i)
    {
        if (degree[i] > 0)
            avengers++;
    }

    return avengers;
}