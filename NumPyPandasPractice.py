# Python program to demonstrate  
# basic array characteristics 
import numpy as np 
  
# Creating array object 
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] ) 

# Flatten Array (Combines different rows into one row)
# arr = arr.flatten()        left to right, top to bottom
arr = arr.flatten('F')     top to bottom, left to right

# Printing type of arr object 
print("Array is of type: ", type(arr)) 
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 
  
# Printing shape of array 
print("Shape of array: ", arr.shape) 
  
# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 
  
# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype)