import parser
import reduction
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    exit(1)

formula_s = parser.read_from_file(filename)
print(formula_s)
print("now reducing to 3sat problem...")
formula_3s = reduction.reduce(formula_s,100)
print(formula_3s)
print("------------------")

reduction.verify(formula_s,formula_3s)
