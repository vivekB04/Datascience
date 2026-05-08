#import libraries
import numpy as np

data = np.array([2,3,4,5,5,10])

# Basic Metrics
data_range =np.max(data) - np.min(data)

q1,q3= np.percentile(data,[25,75])
iqr = q3 - q1

print(f"Range:{data_range}")
print(f"Q1(25th percentile):{q1}")
print(f"Q3(75th percentile):{q3}")
print(f"IQR:{iqr}")

#Outlier Detection using IQR rule
lower_bound=q1-1.5*iqr
upper_bound=q3+1.5*iqr

outliers= data[(data<lower_bound) | (data>upper_bound)]
print(f"Lower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}")
print(f"Outliers: {outliers}")