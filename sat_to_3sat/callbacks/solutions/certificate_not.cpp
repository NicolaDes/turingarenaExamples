#include <vector>
#include <climits>
#include <cassert>
#include <stdlib.h>

std::vector<int> certificates;

void reduceClause(int sizeL, int *literals, int sizeC, int *clause, int requestVariable(), void addClause(), void addVariable(int l))
{

    switch (sizeC)
    {
    case 1:
    {
        int u = requestVariable();
        int v = requestVariable();
        addClause();
        addVariable(clause[0]);
        addVariable(u);
        addVariable(v);

        addClause();
        addVariable(clause[0]);
        addVariable(u);
        addVariable(-v);

        addClause();
        addVariable(clause[0]);
        addVariable(-u);
        addVariable(v);

        addClause();
        addVariable(clause[0]);
        addVariable(-u);
        addVariable(-v);
        certificates.push_back(clause[0]);
        break;
    }
    case 2:
    {
        int u = requestVariable();
        addClause();
        addVariable(clause[0]);
        addVariable(clause[1]);
        addVariable(u);

        addClause();

        addVariable(clause[0]);
        addVariable(clause[1]);
        addVariable(-u);
        certificates.push_back(clause[0]);
        certificates.push_back(clause[1]);
        break;
    }
    case 3:
    {
        addClause();
        addVariable(clause[0]);
        addVariable(clause[1]);
        addVariable(clause[2]);
        certificates.push_back(clause[0]);
        certificates.push_back(clause[1]);
        certificates.push_back(clause[3]);
        break;
    }
    default:
    {
        int u = requestVariable();

        addClause();
        addVariable(clause[0]);
        addVariable(clause[1]);
        addVariable(u);
        certificates.push_back(clause[0]);
        certificates.push_back(clause[1]);
        certificates.push_back(u);

        for (int i = 2; i < sizeC - 2; ++i)
        {
            int v = requestVariable();
            certificates.push_back(clause[i]);
            certificates.push_back(-u);
            certificates.push_back(v);
            addClause();
            addVariable(clause[i]);
            addVariable(-u);
            addVariable(v);

            u = v;
        }

        addClause();
        addVariable(clause[sizeC - 2]);
        addVariable(clause[sizeC - 1]);
        addVariable(-u);
        certificates.push_back(clause[sizeC - 2]);
        certificates.push_back(clause[sizeC - 1]);
        certificates.push_back(-u);
        break;
    }
    }
}

void reduceCertificate(int certificateLiteral, void addCertificateVariable(int l))
{
    addCertificateVariable(certificateLiteral);
}