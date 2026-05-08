import numpy as np

#spending data
spending = np.array([100,200,300,400,500,600,700,800,900,1000])

#90th percentile
threshold = np.percentile(spending,90)

print(f"90th percentile Threshold: {threshold:.2f}")

#identify top 10% users

top_users= spending[spending>=threshold]
print(f"Top Spenders: {top_users}")
