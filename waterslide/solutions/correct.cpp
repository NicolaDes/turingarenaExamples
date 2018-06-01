#include <stdio.h>
#include <assert.h>
#include <vector>
#include <list>
#include <bits/stdc++.h>

#define MAXM 200000

#define MAXN 100001

std::vector<int> adj[MAXN];
std::vector<int> topological;
bool visited[MAXN];
long double cumulate[MAXN];

void dfs(int s)
{
    if(visited[s])
        return;
    
    visited[s]=true;
    for(auto x : adj[s])
    {
        dfs(x);
    }
    topological.push_back(s);
}

int find_pool(int N, int M, int P, int A[], int B[])
{

    for (int i = 0; i < M; ++i)
    {
        adj[A[i]].push_back(B[i]);
    }

    memset(cumulate, 0.0, sizeof cumulate);
    bool end[N];
    memset(end, false, sizeof end);
    memset(visited, false, sizeof visited);

    cumulate[0]=1.0;
    for (int i = 0; i < N; ++i)
    {
        if (adj[i].empty())
        {
            end[i] = true;
        }
    }

    dfs(0);
    cumulate[0]=1.0;
    double max_so_far =-1.0;
    int index = -1;
    for(int i = N-1;i>=0;i--)
    {
        double propagation_val = cumulate[topological[i]]/adj[topological[i]].size();
        cumulate[topological[i]]=0.0;
        for(auto x : adj[topological[i]])
        {
            cumulate[x]+=propagation_val;
            if(end[x] && cumulate[x]>max_so_far)
            {
                max_so_far = cumulate[x];
                index = x;
            }
        }
    }
    assert(index>=0);

    return index;
}