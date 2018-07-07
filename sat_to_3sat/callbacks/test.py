import core.parser
import core.reduction
import core.solver
import core.generator
import sys

def main():
    nLiterals = 5
    nClauses = 10

    [formula_sat,formula_unsat] = core.generator.generate_sat_unsat_random_formula(nLiterals,nLiterals-1)

    certificate=list()
    core.solver.exaustive_search(formula_sat, certificate)

    print("SAT: ",formula_sat,certificate)
    print("UNSAT: ",formula_unsat)

    variables_original = set()
    for c in formula_sat:
        for x in c:
            if x not in variables_original and (-x) not in variables_original:
                variables_original.add(abs(x))
main()