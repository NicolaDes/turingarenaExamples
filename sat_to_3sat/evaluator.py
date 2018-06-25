import core.parser
import core.reduction
from turingarena import *

import random

def main():

    formula_s = [[1, 3, 4, -5],[1, 2], [4], [1, 4, 9, -8, 10]]

    print(formula_s)
    print("now reducing to 3sat problem...")

    formula_3s = core.reduction.reduce(formula_s,20)

    print(formula_3s)

    for i in range(10):
        formula = [random.randint(1,100) for _ in range(10)]
        print(compute(len(formula), formula))




def compute(literals, formula):
    with run_algorithm(submission.source) as process:

        size = process.functions.reduce(literals, formula)

        b = [process.functions.getLiteral(i) for i in range(size)]
        
        return b

main()
