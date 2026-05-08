# Function (Definition ,types,operation)
# ReLU Activation Function
# code 1.2
import numpy as np
def relu(x):
    return np.maximum(0, x)

print(f"ReLU(-5):{relu(-5)}, ReLU(3):{relu(3)}")

