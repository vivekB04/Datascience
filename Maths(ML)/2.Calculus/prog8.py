#Differentiation
#code 4.2 : Direction change

import numpy as np
t_vals = np.array([1,2,3])
d_vals = 10-2*t_vals
slope =np.diff(d_vals)/np.diff(t_vals)

print(f"rate of change: {slope[0]}")


