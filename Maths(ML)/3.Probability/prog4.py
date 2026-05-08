# Distribution

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
session_times=np.random.exponential(scale=2,size=1000)

#histogram
plt.hist(session_times,bins=30,density=True)
plt.title("Distribution of User Session Times")
plt.xlabel("Minutes")
plt.ylabel("Density")
plt.show()


