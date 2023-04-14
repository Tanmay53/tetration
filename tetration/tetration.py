from IPython.display import display
from sympy import symbols

# Tetrate the given number to the given power
def tetrate(num, power):
    if power > 0 :
        return num ** tetrate(num, power - 1)
    else :
        return 1

# Tetrate and show every step in tetration
def tetrate_solve(num, power) :
    for n in range(1, power + 1) :
        display(
            tetrate(symbols('{}'.format(num)), power - n) ** symbols('{}'.format(tetrate(num, n))) if n < power else tetrate(num, n)
        )
    return tetrate(num, power)
