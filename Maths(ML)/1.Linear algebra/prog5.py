import numpy as np

king =np.array([1,0])
man =np.array([1,0])
apple =np.array([0,1])

print(f"King-Man similarity:{np.dot(king,man)}")
print(f"King-Apple similarity:{np.dot(king,apple)}")

