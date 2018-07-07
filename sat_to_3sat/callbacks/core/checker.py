# Check if local changes, new clauses to be added and partial certificate, are consistent with pre-existent problem definition
def local_check(formula_old, formula_new, certificate_old, certificate_new_local, variables_requested):
    if not consistent_formula(formula_old, formula_new):
        print(f"Error! New formula {formula_new} is not consistent with original!")
        return False

    if not consistent_certificate(certificate_old, certificate_new_local):
        print(f"Error! New certificate {certificate_new_local} is not consistent with original")
        return False

    if not consistent_variables(variables_requested, formula_new):
        print(f"Error! New variables used {variables_requested} were not requested!")
        return False

    return True

# Check if new formula generate insconsistence


def consistent_formula(formula_old, formula_new):

    return False

# Check if certificates are consistent one to other


def consistent_certificate(certificate_old, certificate_new_local):

    return False

# Check if non requested variables are used


def consistent_variables(variables_requested, formula_new):

    return False
