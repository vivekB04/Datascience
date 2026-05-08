#Straight lines
#problem : the linear Regression "line of best fit"

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Represent Data using Pandas
data= pd.DataFrame({'Size ':[1,2],
                   'Price':[3,5]})

#generate points for the prediction line based on our math (y=2*x+1)
x_line = np.linspace(0,3,100)
y_line =2 * x_line + 1

#Visualize using Matplotlib
plt.figure(figsize=(10,5))
plt.scatter(data['Size '],data['Price'],color='red',s=100,label='Actual data')
plt.plot(x_line,y_line,color='blue',linewidth=3,label='AI model : y=2*x+1')

#formatting
plt.title('House Price Prediction(Linear Regression)')
plt.xlabel('Size (1000 sq ft)')
plt.ylabel('Price ($100K)')
plt.xlim(0,3)
plt.ylim(0,6)
plt.legend()
plt.grid(True,linestyle='--',alpha=0.7)
plt.show()

