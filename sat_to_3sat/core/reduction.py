
def reduce(formula, max):
    variables = set()
    variables_unused = {
        _
        for _ in range(1, max+1)
    }
    nVariables = 0
    for c in formula:
        for x in c:
            if x not in variables:
                nVariables = nVariables+1

                variables.add(x)
                variables.add(-x)

    variables_unused = variables_unused-variables

    phi = list()
    for c in formula:
        if len(c) == 1:
            nVariables = nVariables+2

            u = variables_unused.pop()
            v = variables_unused.pop()

            variables.add(u)
            variables.add(-u)
            variables.add(v)
            variables.add(-v)

            # adding tautologies to make the clause depend on c[0] (2^2 = 4)
            phi.append([c[0], u, v])
            phi.append([c[0], u, -v])
            phi.append([c[0], -u, v])
            phi.append([c[0], -u, -v])
        elif len(c) == 2:
            nVariables = nVariables+1

            u = variables_unused.pop()
            variables.add(u)
            variables.add(-u)

            # adding tautologies to make the clause depend on c[0] and c[1] (2^1=2)
            phi.append([c[0], c[1], u])
            phi.append([c[0], c[1], -u])
        elif len(c) > 3:
            nVariables = nVariables+1

            u = variables_unused.pop()
            variables.add(u)

            # following the general breaking rule
            phi.append([c[0], c[1], u])
            #for i in range(2, len(c)-2):
            for l_k in c[2:len(c)-2]:
                nVariables = nVariables+1

                v = variables_unused.pop()
                variables.add(v)
                variables.add(-v)
                
                phi.append([l_k, -u, v])

                u = v

            phi.append([c[len(c)-2], c[len(c)-1], -u])
        else:
            # nothing to do
            phi.append(c)

    # phi is now a conjuction of all c' constructed in loop
    return phi
