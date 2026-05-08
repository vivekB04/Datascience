import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

true_ctr=0.05

results=[]
views_range=range(1,1000)

for n in views_range:
    clicks=np.random.binomial(1,true_ctr,n)
    ctr_estimate =np.mean(clicks)
    results.append(ctr_estimate)

plt.plot(views_range,results)
plt.axhline(true_ctr)

plt.title("Law of Large Numbers : CTR convergence")
plt.xlabel("No. of AD Views")
plt.ylabel("Estimated CTR")
plt.show()