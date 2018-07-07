satisfiable = False

# Verifier of sat formula with certificate
def isSat(formula, certificate):
    sat = True
    for c in formula:
        c_sat = False
        for l in c:
            if l in certificate:
                c_sat = True
        sat = sat and c_sat
    return sat


# Complete search (worst case 2^#variables)
def search(variables, assignment, formula, certificate):
    global satisfiable
    if len(variables) == 0:
        if isSat(formula, assignment):
            satisfiable = True
            certificate.append(assignment.copy())
        return
    x = variables.pop()
    assignment.append(x)
    search(variables, assignment, formula,certificate)
    assignment.remove(x)
    assignment.append(-x)
    search(variables, assignment, formula, certificate)
    variables.add(x)
    assignment.remove(-x)



# Solve a cnf formula and fill a certificate list with the assignment if is SAT, 
# otherwise certificate is empty
# input: formula, output: True (sat), False (unsat)
def exaustive_search(formula,certificate=list()):
    if len(formula)==1:
        return True
    variables = set()
    assignment = list()
    for c in formula:
        for x in c:
            if x not in variables and (-x) not in variables:
                variables.add(abs(x))
    
    global satisfiable 
    satisfiable = False
    search(variables,assignment,formula,certificate)
    if not satisfiable:
        certificate.clear()
    return satisfiable
    
