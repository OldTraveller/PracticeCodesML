import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# MEAN MODE AND MEDIAN in NUMPY 
arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,5,5,6] 

mean = np.mean(arr) 
print ("MEAN : ", mean) 

median = np.median(arr) 
print ("MEDIAN : ", median) 

mode = stats.mode(arr) 
print ("MODE : ", mode) 

# FIND THE STANDARD DEVIATION 
std = np.std(arr) 
print ("DEVIATION : ", std) 
var = np.var(arr) 
print ("VAIRINCE : ", var)  
print ("SQUARE OF STD : ", (std * std)) 

# TO FIND THE PERCENTILE 
per1 = np.percentile(arr, 1)
print ("PERCENTILE 1 : ", per1) 
per3 = np.percentile(arr, 3)
print ("PERCENTILE 3 : ", per3) 
per4 = np.percentile(arr, 4)
print ("PERCENTILE 4 : ", per4) 
per5 = np.percentile(arr, 6)
print ("PERCENTILE 5 : ", per5) 

print ("THE DATASET REPRESENTATION USING HISTOGRAM!") 
print ("WE CAN USE MATPLOTLIB FOR PLOTTING THE HISTOGRAM") 
plt.hist(arr, len(set(arr)))
plt.show()


