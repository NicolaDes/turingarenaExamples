import core.solver
import random


def pigeonhole(literals):
    formula = list()
    for i in range(1, literals+2):
        c = list()
        for j in range(1, literals+1):
            c.append(literals*(i-1)+j)
        formula.append(c)
    for j in range(1, literals+1):
        for i in range(1, literals+1):
            for k in range(i+1, literals+2):
                formula.append([-(literals*(i-1)+j), -(literals*(k-1)+j)])
    return formula


def verify_cert(formula, certificate):
    sat = True
    for c in formula:
        c_sat = False
        for l in c:
            if l in certificate:
                c_sat = True
        sat = sat & c_sat
    return sat


def generate_sat_unsat_random_formula(literals, max_c_size):
    sat_formula = list()
    unsat_formula = list()

    variables = set(range(1, literals+1))

    sat = True

    formula = list()
    tmp = list()

    while sat:
        c = set()
        c_size = random.randint(4,max_c_size)
        for l in range(1,c_size):
            c.add(random.choice([1,-1])*random.choice(list(variables)))
        last = c
        formula.append(c)
        sat = core.solver.exaustive_search(formula,tmp)

    unsat_formula = formula.copy()
    formula.pop()
    sat_formula=formula
    return [sat_formula, unsat_formula]
