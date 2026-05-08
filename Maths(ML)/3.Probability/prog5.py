#Normal Distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu = 5
sigma = 0.5

np.random.seed(42)
seeds=np.random.normal(mu,sigma,1000)

plt.hist(seeds,bins=30,density=True,alpha=0.6)

xmin, xmax = plt.xlim()
x=np.linspace(xmin,xmax,100)
p=norm.pdf(x,mu,sigma)

plt.plot(x,p,)

lower = mu-sigma
upper = mu+sigma
plt.axvline(lower)
plt.axvline(upper)

plt.title("Robot Speed Distribution")
plt.xlabel("Speed (km/s)")
plt.ylabel("Density")

plt.show()