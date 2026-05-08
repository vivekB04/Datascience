#Function Behaviour & properties
#code 2.1 : the learning curve(increasing function)

import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,10,100)
accuracy = 1-1/(t+1)

plt.plot(t,accuracy)
plt.title('Increasing Model Accuracy')
plt.show()

