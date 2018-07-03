import core.parser
import core.reduction
from turingarena import *

import random

Tasks = [50]*4

def main():

    print(f"Computing submission...")
    # n==1
    print(f"Task n == 1")
    for i in range(50):
        formula = [random.randint(1, 100)]
        correct = core.reduction.reduce([formula], 32767)
        request = compute(len(formula), formula)
        if core.reduction.verify([formula], request):
            # print(f"Correct!!")
            x = 1
        else:
            # print(f"Wrong!! {formula} -> {request} != {correct}")
            Tasks[0]=Tasks[0]-1

    # n==2
    print(f"Task n == 2")
    for i in range(50):
        formula = [random.randint(1, 100) for _ in range(2)]
        correct = core.reduction.reduce([formula], 32767)
        request = compute(len(formula), formula)
        if core.reduction.verify([formula], request):
            # print(f"Correct!!")
            x = 1
        else:
            # print(f"Wrong!! {formula} -> {request} != {correct}")
            Tasks[1]=Tasks[1]-1

    # n>3
    print(f"Task n == 3")
    for i in range(50):
        formula = [random.randint(1, 100) for _ in range(3)]
        correct = core.reduction.reduce([formula], 32767)
        request = compute(len(formula), formula)
        if core.reduction.verify([formula], request):
            # print(f"Correct!!")
            x = 1
        else:
            # print(f"Wrong!! {formula} -> {request} != {correct}")
            Tasks[2]=Tasks[2]-1

    # n>3
    print(f"Task n > 3")
    for i in range(50):
        formula = [random.randint(1, 100) for _ in range(100)]
        correct = core.reduction.reduce([formula], 32767)
        request = compute(len(formula), formula)
        if core.reduction.verify([formula], request):
            # print(f"Correct!!")
            x = 1
        else:
            # print(f"Wrong!! {formula} -> {request} != {correct}")
            Tasks[3]=Tasks[3]-1


    print(f"Results:")

    print(f"Task n == 1: {Tasks[0]}/50")
    print(f"Task n == 2: {Tasks[1]}/50")
    print(f"Task n == 3: {Tasks[2]}/50")
    print(f"Task n  > 3: {Tasks[3]}/50")

def compute(literals, formula):
    with run_algorithm(submission.source) as process:

        size = process.functions.reduce(literals, formula)

        b = [process.functions.getLiteral(i) for i in range(size)]

        result = list()

        i = 0
        while i < size:
            c = list()
            while b[i] != 0:
                c.append(b[i])
                i = i+1
            result.append(c)
            i = i+1

        return result


main()
