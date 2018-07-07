import core.solver
import random


# Generate unsat cnf from famous pigeonhole problem
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


# Generate a random cnf sat and unsat with the following idea:
# Continue to add clauses until the formula is unsat! So return that formula
# less the last clause as sat and the complete formula as unsat.
def generate_sat_unsat_random_formula(literals, max_c_size):
    sat_formula = list()
    unsat_formula = list()

    variables = set(range(1, literals+1))

    sat = True

    formula = list()
    tmp = list()

    while sat:
        c = list()
        c_size = random.randint(2,max_c_size)
        for l in range(1,c_size):
            c.append(random.choice([1,-1])*random.choice(list(variables)))
        last = c
        formula.append(c)
        sat = core.solver.exaustive_search(formula,tmp)

    unsat_formula = formula.copy()
    formula.pop()
    sat_formula=formula
    return [sat_formula, unsat_formula]
