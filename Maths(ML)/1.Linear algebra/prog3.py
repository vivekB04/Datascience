import numpy as np
user_a=np.array([2,3])
user_b=np.array([5,7])

distance = np.linalg.norm(user_a - user_b)
print(f"Distance: {distance}")