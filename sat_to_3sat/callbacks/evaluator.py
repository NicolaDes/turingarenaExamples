import core.parser
import core.reduction
import core.solver
import core.generator
from turingarena import *

import random

Tasks = [50]*4


def main():
    print(f"SAT testing")
    literals = [_ for _ in range(1, 6)]
    clauses = 20
    max_c_size = 10
    [formula, certificate] = core.generator.generate_formula(
        len(literals), clauses, max_c_size)

    new_formula = formula.copy()

    for c in formula:

        # test_case = formula[random.randint(0,len(formula)-1)]
        test_case = c

        request = compute(literals, test_case)

        for x in request:
            new_formula.append(x)

    req = core.solver.exaustive_search(new_formula)
    corr = core.solver.exaustive_search(formula)
    if req == corr:
        print("Reduction is correct!!")
    else:
        print(f"Reduction is not correct, {request} make formula {new_formula} unsat!!")



    print(f"UNSAT testing")
    pigeonhole_size = 3
    [formula, certificate] = core.generator.generate_formula(pigeonhole_size, clauses, max_c_size, False)

    literals = set()
    for c in formula:
        for x in c:
            if x not in literals and (-x) not in literals:
                literals.add(abs(x))

    new_formula = list()

    for c in formula:

        # test_case = formula[random.randint(0,len(formula)-1)]
        test_case = c

        request = compute(list(literals), test_case)

        for x in request:
            new_formula.append(x)

    print(new_formula)
    req = core.solver.exaustive_search(new_formula)
    corr = core.solver.exaustive_search(formula)
    if req == corr:
        print("Reduction is correct!!")
    else:
        print(f"Reduction is not correct, {request} make formula {new_formula} unsat!!")


def compute(literals, formula):
    
    with run_algorithm(submission.source) as process:
        formula_raw = list()

        def addVariable(i):
            formula_raw.append(i)

        process.procedures.reduce(len(literals), literals, len(formula), formula, callbacks=[addVariable])

        formula = list()
        i = 0
        while i < len(formula_raw):
            c = list()
            while formula_raw[i] != 0:
                c.append(formula_raw[i])
                i = i+1
            formula.append(c)
            i = i+1
        return formula


main()
