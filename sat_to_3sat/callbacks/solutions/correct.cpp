void reduceClause(int sizeL, int *literals, int sizeC, int *clause, int requestVariable(), void addClause(), void addVariable(int l))
{
    int new_vars[10];
    for (int i = 0; i < 10; ++i)
    {
        new_vars[i] = requestVariable();
    }
    addClause();
    for (int i = 0; i < 10; ++i)
        addVariable(new_vars[i]);
    addClause();
    addVariable(100);
}

void reduceCertificate(int certificateLiteral, void addCertificateVariable(int l))
{
    addCertificateVariable(certificateLiteral);
}
