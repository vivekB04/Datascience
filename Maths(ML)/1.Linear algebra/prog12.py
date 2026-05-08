import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import alpha

#1. Define Points using Numpy
benign_proto = np.array([1,1])
malignant_proto = np.array([5,4])
patient = np.array([2,3])

#2. Calculate Distance manually for verification
dist_b= np.linalg.norm(patient-benign_proto)
dist_m= np.linalg.norm(patient-malignant_proto)

#3.Visualize
plt.figure(figsize=(8,5))

#plot prototype and patient
plt.scatter(benign_proto[0],benign_proto[1],color='blue',s=200,marker='s',label='Benign Prototype')

plt.scatter(malignant_proto[0],malignant_proto[1],color='red',s=200,marker='s',label='Malignant Prototype')

plt.scatter(patient[0],patient[1],color='green',s=200,marker='o',edgecolors='black',label='Patient Tumor')

#Draw lines indicating distance
plt.plot([patient[0],benign_proto[0]],[patient[1],benign_proto[1]],'b--',alpha=0.5,label =f'Distance to B :{dist_b:.2f}')

plt.plot([patient[0],malignant_proto[0]],[patient[1],malignant_proto[1]],'r--',alpha=0.5,label =f'Distance to m :{dist_m:.2f}')

# formatting
plt.title("Medical Diagnosis using K-Nearest Neighbors logic")
plt.xlabel("feature 1(Clump thickness)")
plt.ylabel("feature 2(Uniformity)")
plt.xlim(0,6)
plt.ylim(0,5)
plt.legend()
plt.grid (True,alpha=0.3)
plt.show()
