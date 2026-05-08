#Function Behaviour & properties
#code 2.2 : Continuous and Discontinuous training
import numpy as np


def training_process(x):
    return 2*x if x<5 else 0
print(f"At 4.9: {training_process(4.9)}, \nAt 5.0: {training_process(5.0)}")

