#include <vector>
#include <climits>
#include <cassert>
#include <stdlib.h>

std::vector<int> formula;

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
        formula.push_back(clause[0]);
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
        formula.push_back(clause[0]);
        formula.push_back(clause[1]);
        break;
    }
    case 3:
    {
        addClause();
        addVariable(clause[0]);
        addVariable(clause[1]);
        addVariable(clause[2]);
        formula.push_back(clause[0]);
        formula.push_back(clause[1]);
        formula.push_back(clause[3]);
        break;
    }
    default:
    {
        int u = requestVariable();

        addClause();
        addVariable(clause[0]);
        addVariable(clause[1]);
        addVariable(u);
        formula.push_back(clause[0]);
        formula.push_back(clause[1]);
        formula.push_back(u);

        for (int i = 2; i < sizeC - 2; ++i)
        {
            int v = requestVariable();
            formula.push_back(clause[i]);
            formula.push_back(-u);
            formula.push_back(v);
            addClause();
            addVariable(clause[i]);
            addVariable(-u);
            addVariable(v);

            u = v;
        }

        addClause();
        addVariable(-u);
        addVariable(clause[sizeC - 2]);
        addVariable(clause[sizeC - 1]);
        formula.push_back(-u);
        formula.push_back(clause[sizeC - 2]);
        formula.push_back(clause[sizeC - 1]);
        break;
    }
    }
}

void reduceCertificate(int certificateLiteral, void addCertificateVariable(int l))
{

    switch (formula.size())
    {
    case 1:
        addCertificateVariable(certificateLiteral);
        break;
    case 2:
        addCertificateVariable(certificateLiteral);
        break;
    case 3:
        addCertificateVariable(certificateLiteral);
        break;

    default:
        // if z_1 or z_2, assign all other to false
        // if z_{k-1} or z_k assign all other to true
        // otherwise l_j for 1<=j<=l-2 to false, other to true
        if (formula[0] == certificateLiteral or formula[1] == certificateLiteral)
        {
            for (int i = 3; i < formula.size() - 3; i+=3)
            {
                addCertificateVariable(formula[i+1]);
            }
            addCertificateVariable(formula[formula.size()-3]);
            break;
        }
        else if (formula[formula.size() - 1] == certificateLiteral or formula[formula.size() - 1] == certificateLiteral)
        {
            for (int i = 0; i < formula.size() - 3; i+=3)
            {
                addCertificateVariable(formula[i+2]);
            }
            break;
        }
        int i = 0;
        for (; i < formula.size() - 3; i+=3)
        {
            if (formula[i] == certificateLiteral)
                break;
            addCertificateVariable(formula[i+2]);
        }
        i+=3;
        for (; i < formula.size()-3; i+=3)
        {
            addCertificateVariable(formula[i+1]);
        }
        addCertificateVariable(formula[formula.size()-3]);
        break;
    }
}