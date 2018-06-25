#include<vector>

std::vector<int> sat3;

int reduce(int size, int *clause)
{
    sat3.insert(sat3.begin(), clause, clause+size);
    return size;
}
int getLiteral(int i)
{
    return sat3[i];
}
