
int new_vars[5];

void reduceClause(int sizeL, int *literals, int sizeC, int *clause, int requestVariable(), void addClause(), void addVariable(int l))
{
    for (int i = 0; i < 5; ++i)
    {
        new_vars[i] = requestVariable();
    }
    addClause();
    for (int i = 0; i < 5; ++i)
        addVariable(new_vars[i]);
}

void reduceCertificate(int certificateLiteral, void addCertificateVariable(int l))
{
    addCertificateVariable(certificateLiteral);
}
