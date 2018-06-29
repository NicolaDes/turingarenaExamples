#include <vector>
#include <climits>
#include <cassert>
#include <stdlib.h>

#define IMAX 32767

std::vector<int> sat3;
bool taken[IMAX];

int getUnusedLiteral()
{
    int i = 1;
    for (; i < IMAX; ++i)
    {
        if (!taken[i])
            break;
    }
    assert(i != 0);
    return i;
}

int reduce(int size, int *clause)
{

    for (int i = 0; i < size; ++i)
        taken[abs(clause[i])] = true;

    int nLiterals = 0;

    switch (size)
    {
    case 1:
    {
        int u = getUnusedLiteral();
        taken[u] = true;
        int v = getUnusedLiteral();
        taken[v] = true;
        sat3.push_back(clause[0]);
        sat3.push_back(u);
        sat3.push_back(v);

        sat3.push_back(0); //separator

        sat3.push_back(clause[0]);
        sat3.push_back(u);
        sat3.push_back(-v);

        sat3.push_back(0); //separator

        sat3.push_back(clause[0]);
        sat3.push_back(-u);
        sat3.push_back(v);

        sat3.push_back(0); //separator

        sat3.push_back(clause[0]);
        sat3.push_back(-u);
        sat3.push_back(-v);

        sat3.push_back(0); //separator

        nLiterals = 16;
        break;
    }
    case 2:
    {
        int u = getUnusedLiteral();
        taken[u] = true;
        sat3.push_back(clause[0]);
        sat3.push_back(clause[1]);
        sat3.push_back(u);

        sat3.push_back(0); //separator

        sat3.push_back(clause[0]);
        sat3.push_back(clause[1]);
        sat3.push_back(-u);

        sat3.push_back(0); //separator

        nLiterals = 8;
        break;
    }
    case 3:
    {
        sat3.push_back(clause[0]);
        sat3.push_back(clause[1]);
        sat3.push_back(clause[2]);

        sat3.push_back(0); //separator

        nLiterals = 4;
        break;
    }
    default:
    {
        int u = getUnusedLiteral();
        taken[u] = true;

        sat3.push_back(clause[0]);
        sat3.push_back(clause[1]);
        sat3.push_back(u);

        sat3.push_back(0); //separator

        nLiterals = 4;

        for (int i = 2; i < size - 2; ++i, nLiterals += 4)
        {
            int v = getUnusedLiteral();
            taken[v] = true;

            sat3.push_back(clause[i]);
            sat3.push_back(-u);
            sat3.push_back(v);

            sat3.push_back(0);

            u = v;
        }

        sat3.push_back(clause[size - 2]);
        sat3.push_back(clause[size - 1]);
        sat3.push_back(-u);
        sat3.push_back(0);

        nLiterals += 4;
        break;
    }
    }
    return nLiterals;
}
int getLiteral(int i)
{
    return sat3[i];
}
