import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)

data=np.random.uniform(0,100,10000)

sample_size=50
num_samples =1000

sample_means=[]

for _ in range(num_samples):
    sample=np.random.choice(data,sample_size)
    sample_means.append(np.mean(sample))

sample_means=np.array(sample_means)

plt.hist(sample_means ,bins=30,density=True,alpha=0.5)

mean =np.mean(sample_means)
std=np.std(sample_means)

x=np.linspace(min(sample_means),max(sample_means),100)

pdf=norm.pdf(x,mean,std)
plt.plot(x,pdf)

plt.title("Centeral limit")
plt.xlabel("Sample mean")
plt.ylabel("Density")
plt.show()

