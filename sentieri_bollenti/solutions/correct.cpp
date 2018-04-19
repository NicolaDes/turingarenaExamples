#include<vector>
#include<queue>
#include<fstream>

using namespace std;

int A,B,N;
vector<pair<int,int64_t> > L[100000];

int64_t D[1000000];

class compare
{
    public:
    bool operator()(pair<int,int64_t> a,pair<int,int64_t> b)const{return a.second>b.second;}
};

int minimize(int N, int M, int A, int B, int from[], int to[])
{
    int s,d;

    s=1;d=N;
   
    int index = 0;
    //create datastructure for dijkstra
    for(;index<A;index++)
    {
        L[from[index]].push_back(make_pair(to[index],0)); //arco ab con costo 0
        L[to[index]].push_back(make_pair(from[index],0));
    }
    for(;index<A+B;index++)
    {
        L[from[index]].push_back(make_pair(to[index],1)); //arco ab con costo 1
        L[to[index]].push_back(make_pair(from[index],1));
    }

    
    for(int i=0;i<=N;++i)
    {
        D[i] = -1; //Dijkstra vector
    }
    
    priority_queue<pair<int, int64_t>, vector<pair<int, int64_t> >,compare> q;
    q.push(make_pair(s,0));
    
    while(q.size()>0)
    {
        pair<int,int64_t> n=q.top();q.pop();
        
        if(D[n.first] >= 0) continue;
        D[n.first]=n.second;
        
        int size = L[n.first].size();
        for(int i=0;i<size;++i)
        {
            if(D[L[n.first][i].first] >= 0)continue;
            
            q.push(make_pair(L[n.first][i].first,n.second+L[n.first][i].second)); //nodo di destinazione settando la distanza come quella attuale + l'arco da percorrere
        }
    }

    return D[d];  
}
