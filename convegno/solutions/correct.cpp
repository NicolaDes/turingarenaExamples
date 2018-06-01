#include <vector>
#define MAXN 100000

std::vector<int> adj[MAXN];
int cumulate[MAXN];

void dfs(int s, int e)
{
    cumulate[s]=cumulate[e]+1;
    for (auto u : adj[s])
    {
        dfs(u, s);
    }
}

int coppie(int N, int *C)
{
    int capo = -1;
    for (int i = 0; i < N; ++i)
    {
        if (C[i] == -1)
        {
            capo = i;
            continue;
        }
        adj[C[i]].push_back(i);
    }
    
    cumulate[capo]=-1;
    dfs(capo, capo);
    int sum = 0;
    for (int i = 0; i < N; ++i)
    {
        sum += cumulate[i];
    }
    return sum;
}
