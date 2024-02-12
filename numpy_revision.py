import numpy as np

arr = np.array([2,4,5,6,7])

print(f"Array is: {arr}")

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr.ndim)

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0,1])