satisfiable = False

def isSat(formula, certificate):
    sat = True
    for c in formula:
        c_sat = False
        for l in c:
            if l in certificate:
                c_sat = True
        sat = sat and c_sat
    return sat


def search(variables, assignment, formula):
    global satisfiable
    if len(variables) == 0:
        if isSat(formula, assignment):
            satisfiable = True
        return
    x = variables.pop()
    assignment.append(x)
    search(variables, assignment, formula)
    assignment.remove(x)
    assignment.append(-x)
    search(variables, assignment, formula)
    variables.add(x)
    assignment.remove(-x)



# input: formula, output: True (sat), False (unsat)
def exaustive_search(formula):
    variables = set()
    assignment = list()
    for c in formula:
        for x in c:
            if x not in variables and (-x) not in variables:
                variables.add(abs(x))
    
    global satisfiable 
    satisfiable = False
    search(variables,assignment,formula)
    return satisfiable
    
