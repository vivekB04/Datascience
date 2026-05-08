import numpy as np
from sympy.physics.units import second

w_vals =np.linspace(-5,5,100)
loss=w_vals**2

print("sample weight(w):",w_vals[::20])
print("sample loss(w^2):",loss[::20])
second_derivative=2
if second_derivative>0:
    print("\n Result: the second derivative is Positive(+2).")
