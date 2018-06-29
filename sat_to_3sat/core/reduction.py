# def solve(assignment, cnf):
#     sat = True
#     for c in cnf:
#         sat_clause = False
#         for x in c:
#             if (assignment[x] == 1 and x > 0) or (assignment[x] == 0 and x < 0):
#                 sat_clause = True
#         sat = sat & sat_clause
#     return sat


# def verify(cnf, cnf_3):
#     variables_original = set()
#     for c in cnf:
#         for x in c:
#             if x not in variables_original and (-x) not in variables_original:
#                 variables_original.add(abs(x))

#     variables_new = set()
#     for c in cnf3:
#         for x in c:
#             if x not in variables_original and (-x) not in variables_original:
#                 variables_original.add(abs(x))

#     variables_new.difference_update(variables_original)
#     if len(cnf) == 1:
#         print("len(cnf)==1")
#     elif len(cnf) == 2:
#         print("len(cnf)==2")
#     elif len(cnf) > 3:
#         if cnf[0] > 0 or cnf[1] > 0:


#     else:
#         print("len(cnf)==3")

def unify(c1, c2):
    ret = list()
    for x1 in c1:
        if x1 not in ret:
            ret.append(x1)
        for x2 in c2:
            if x2 not in ret:
                ret.append(x2)
    for x1 in ret:
        if -x1 in ret:
            ret.remove(x1)
            ret.remove(-x1)
   
    return ret
    

def verify(cnf, cnf_3):
    
    variables_original = set()
    for c in cnf:
        for x in c:
            if x not in variables_original and (-x) not in variables_original:
                variables_original.add(abs(x))

    if len(cnf[0])==1:
        return False
    elif len(cnf[0])==2:
        return False
    elif len(cnf[0])==3:
        return True
    elif len(cnf[0]) >3:
        sat_original = cnf_3
        for i in range(len(cnf_3)-1):
            for j in range(i,len(cnf_3)):
                for x in cnf_3[i]:
                    if (-x) in cnf_3[j] and abs(x) not in variables_original:
                        sat_original = [unify(sat_original[0],cnf_3[j])]

        if len(sat_original)>1:
            sys.exit('Error!')

        if set(sat_original[0]) == set(cnf[0]):
            return True
        else:
            return False




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
            # for i in range(2, len(c)-2):
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
