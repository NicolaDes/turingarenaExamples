import core.solver
import core.generator
import core.checker
from core import eprint
from turingarena import *

import random

verbose = False

variables_original = set()
variables_requested = set()

Correct = True

## Main function:
# First generate sat and unsat cases
# Second submit with compute
# Third verify the submission with core.checker
def main():
    global variables_original
    global Correct

    nLiterals = 6

    [formula_sat, formula_unsat] = core.generator.generate_sat_unsat_random_formula(
        nLiterals, nLiterals-1)
    certificate = list()
    core.solver.exaustive_search(formula_sat, certificate)

    for c in formula_sat:
        for x in c:
            if x not in variables_original and (-x) not in variables_original:
                variables_original.add(abs(x))

    task_ok = 1
    tot = len(formula_sat)+len(formula_unsat)

    formula_3sat = list()
    formula_3unsat = list()

    for i in range(len(formula_sat)):
        print(f"Computing {task_ok}/{tot} case")
        [submitted_formula, certificate_local] = compute(
            formula_sat[i], certificate)
        if not Correct:
            print("La tua riduzione è sbagliata!")
            return
        formula_3sat.append(submitted_formula)
        task_ok = task_ok+1

    for i in range(len(formula_unsat)):
        print(f"Computing {task_ok}/{tot} case")
        [submitted_formula, certificate_local] = compute(
            formula_unsat[i], certificate, False)
        if not Correct:
            print("La tua riduzione è sbagliata!")
            return
        formula_3unsat.append(submitted_formula)
        task_ok = task_ok+1

    print("Complimenti! hai superato tutti i test, la tua riduzione è giusta!!")

    verboseprint = print if verbose else lambda *a, **k: None

    verboseprint(f"\n\nHai ridotto: ")
    verboseprint(f"phi({variables_original}) = {formula_sat}\n\n in \n\n 3phi({variables_original.union(variables_requested)}) = {formula_3sat}")

    verboseprint("\n\n e ")

    verboseprint(f"\n\nphi({variables_original}) = {formula_unsat}\n\n in \n\n 3phi({variables_original.union(variables_requested)}) = {formula_3unsat}")


# Compute the submission valuating first the formula reduction and then the certificate reduction
# @Warning The evaluation must be by local replacement!
def compute(formula, certificate, sat=True):
    global variables_original
    global variables_requested
    global Correct

    with run_algorithm(submission.source) as process:
        formula_new = list()
        certificate_local = set()

        def requestVariable():
            new_var = len(variables_original)+1+len(variables_requested)
            variables_requested.add(new_var)
            return new_var

        def addClause():
            nonlocal formula_new
            formula_new.append(list())

        def addVariable(i):
            nonlocal formula_new
            formula_new[len(formula_new)-1].append(i)

        process.procedures.reduceClause(len(variables_original), variables_original, len(
            formula), formula, callbacks=[requestVariable, addClause, addVariable])

        def addCertificateVariable(l):
            nonlocal certificate_local
            certificate_local.add(l)

        variableCertificate = []
        done = False
        for l in formula:
            for cert in certificate:
                if l in cert:
                    variableCertificate = [l, cert]
                    done = True
                    break
            if done:
                break

        process.procedures.reduceCertificate(
            l, callbacks=[addCertificateVariable])
        certificate_local.add(l)

        if sat and not core.checker.local_check(formula, formula_new, certificate, list(certificate_local), variables_original, variables_requested):
            eprint("System abort!!")
            Correct = False

        return [formula_new, certificate_local]


main()

evaluation.data(dict(goals=dict(Correct=Correct)))