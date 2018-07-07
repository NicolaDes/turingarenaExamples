import core.reduction
import core.solver
import core.generator
import core.checker
from turingarena import *

import random




def main():
    nLiterals = 5
    nClauses = 10

    [formula_sat,formula_unsat] = core.generator.generate_sat_unsat_random_formula(nLiterals,nLiterals-1)

    certificate=list()
    core.solver.exaustive_search(formula_sat, certificate)

    variables_original = set()
    for c in formula_sat:
        for x in c:
            if x not in variables_original and (-x) not in variables_original:
                variables_original.add(abs(x))

    i = 0
    [submitted_formula,certificate_local] = compute(list(variables_original), formula_sat[i],certificate)
    print(submitted_formula," | ",certificate_local)


def compute(variables_original, formula, certificate):
    
    print("original: ",formula)

    with run_algorithm(submission.source) as process:
        formula_raw = list()
        certificate_local = list()
        variables_requested = set()

        def requestVariable():
            variables_requested.add(len(variables_original)+1+len(variables_requested))
            return len(variables_original)+len(variables_requested)

        def addClause():
            nonlocal formula_raw
            formula_raw.append(list())

        def addVariable(i):
            nonlocal formula_raw
            formula_raw[len(formula_raw)-1].append(i)

        process.procedures.reduceClause(len(variables_original), variables_original, len(formula), formula, callbacks=[requestVariable,addClause,addVariable])

        def addCertificateVariable(l):
            nonlocal certificate_local
            certificate_local.append(l)

        variableCertificate = []
        done = False
        for l in formula:
            for cert in certificate:
                if l in cert:
                    variableCertificate = [l,cert]
                    done = True
                    break
            if done:
                break
                    

        process.procedures.reduceCertificate(l,callbacks=[addCertificateVariable])

        if not core.checker.local_check(formula,formula_raw,certificate,certificate_local,variables_requested):
            print("System abort!!")
            # return [False,False]

        return [formula_raw,certificate_local]

main()
