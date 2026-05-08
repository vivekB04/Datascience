import pandas as pd
import numpy as np

data= [20,30,40,50,60,600]
df= pd.DataFrame(data,columns=['WatchTime'])

print(f"Mean: {df['WatchTime'].mean()}")
print(f"Median: {df['WatchTime'].median()}")
print(f"Mode: {df['WatchTime'].mode()[0]}")