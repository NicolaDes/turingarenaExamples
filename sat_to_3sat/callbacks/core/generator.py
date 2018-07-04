import random

def pigeonhole(literals):
    formula = list()
    for i in range(1,literals+2):
        c = list()
        for j in range(1,literals+1):
            c.append(literals*(i-1)+j)
        formula.append(c)
    for j in range(1,literals+1):
        for i in range(1,literals+1):
            for k in range(i+1,literals+2):
                formula.append([-(literals*(i-1)+j),-(literals*(k-1)+j)])
    return formula

def isSat(formula, certificate):
    sat = True
    for c in formula:
        c_sat = False
        for l in c:
            if l in certificate:
                c_sat=True
        sat = sat & c_sat
    return sat

def generate_formula(literals,clauses,max_c_size,sat=True):
    formula = list()

    variables = set(range(1,literals+1))

    certificate = set()

    for l in variables:
        certificate.add(random.choice([1,-1])*l)
    
    if sat:
        for _ in range(clauses):
            c = set()
            c_size = random.randint(1,max_c_size)
            c_true = random.randint(1,c_size)
            for l in range(c_true):
                c.add(random.choice(list(certificate)))
            for l in range(c_size-c_true):
                c.add(random.choice(list(variables)))
            
            formula.append(list(c))
    else:
       formula = pigeonhole(literals)
    
    return [formula,certificate]