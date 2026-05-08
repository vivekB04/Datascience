import numpy as np
from numpy.random.mtrand import random_sample

np.random.seed(42)

all_users = np.arange(1000)

night_user= np.random.choice(all_users, size=150, replace=False)

biased_sample = np.random.choice(night_user,size=50,replace=False)

ramdom_sample = np.random.choice(all_users,size=50,replace=False)

print("biased sample:")
print(biased_sample)
print("\nRandom sample(All_users):")
print(random_sample)

