#Differentiation
#code 4.1 : sensitivity analysis

import sympy as sp
w= sp.Symbol('w')
L=w**2
derivative = sp.diff(L,w)
print(f'derivative at 4: {derivative.subs(w,4)}')