import numpy as np

scores =np.array([80,90])
weights = np.array([0.7,0.3])

total = np.dot(scores,weights)
print(f"Total: {total}")
