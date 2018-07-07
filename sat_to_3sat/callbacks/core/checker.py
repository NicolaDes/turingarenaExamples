import core.solver

# Check if local changes, new clauses to be added and partial certificate, are consistent with pre-existent problem definition
def local_check(formula_old, formula_new, certificate_old, certificate_new_local, variables_original, variables_requested):
    if not consistent_formula(formula_old, formula_new):
        print(f"Error! New formula {formula_new} is not consistent with original!")
        return False

    if not consistent_certificate(certificate_old, certificate_new_local, formula_new):
        print(f"Error! New certificate {certificate_new_local} is not consistent with original")
        return False

    if not consistent_variables(variables_original, variables_requested, formula_new):
        print(f"Error! New variables used {variables_original, variables_requested} were not requested!")
        return False

    return True

# Check if new formula generate insconsistence
def consistent_formula(formula_old, formula_new):
    phi = [formula_old.copy()]
    without_ = core.solver.exaustive_search(phi)
    for c in formula_new:
        phi.append(c)
    with_ = core.solver.exaustive_search(phi)
    if with_ != without_:
        return False
    return True

# Check if certificates are consistent one to other
def consistent_certificate(certificate_old, certificate_new_local,formula_new):
    # check if certificate is inside formula given
    for c in formula_new:
        fail = True
        for x in certificate_new_local:
            if x in c:
                fail = fail and False
        if fail:
            print(f"AAAphi_n: {formula_new}, certificate_old: {certificate_old}, new: {certificate_new_local}")
            return False

    # check if get an absurd comparing certificates
    absurd = False
    for cert in certificate_old:
        in_curr_cert = True
        for x in certificate_new_local:
            if -x in cert:
                in_curr_cert = False
        absurd = absurd or in_curr_cert
    print(f"phi_n: {formula_new}, certificate_old: {certificate_old}, new: {certificate_new_local}")
    return absurd

# Check if non requested variables are used
def consistent_variables(variables_original, variables_requested, formula_new):
    for c in formula_new:
        for x in c:
            if x not in variables_original and x not in variables_requested and -x not in variables_original and -x not in variables_requested:
                return False
    return True
