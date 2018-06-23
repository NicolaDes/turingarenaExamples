import core.parser
import core.reduction
from turingarena import *


Task = [False]*4


def evaluate(algorithm):
    formula_s = core.parser.read_from_file("input_example/simple_v3_c2.cnf")
    print(formula_s)
    print("now reducing to 3sat problem...")
    formula_3s = core.reduction.reduce(formula_s,100)
    print(formula_3s)




def compute(algorithm, nC, nL, phi):
    with algorithm.run() as process:
        return process.call.riduci(nC, nL, phi)


algorithm = submitted_algorithm()


evaluate(algorithm)
