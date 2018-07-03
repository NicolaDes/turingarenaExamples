
def read_from_file(file_path):
    s_formula = list()
    with open(file_path, "r") as f:
        for item in f.readlines():
            if item[0] != 'c' and item[0] != 'p':
                s_formula.append(item.strip('\n').strip(' 0'))

    formula = list()
    for s in s_formula:
        s_c = s.split(' ')
        c = list()
        for s_l in s_c:
            c.append(int(s_l))
        formula.append(c)
    return formula
