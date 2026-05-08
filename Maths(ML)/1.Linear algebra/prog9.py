import numpy as np

A=np.array([[5,0],
            [0,1]])

values,vectors=np.linalg.eig(A)
print(f"the multipiler (Eigenvalue) is : {values[0]}")

