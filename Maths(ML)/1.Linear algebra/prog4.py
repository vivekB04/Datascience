import numpy as np
points =np.array([[1,2],[3,4],[5,6]])

centroid = np.mean(points,axis=0)
print(f"Centroid: {centroid}")
