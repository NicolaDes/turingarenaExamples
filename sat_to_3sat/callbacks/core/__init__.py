import sys
"""@package sat_core
Core module to solve, check and verify reduction between sat and 3sat using
gadgets and certificates.
"""

## Print on standard error
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)