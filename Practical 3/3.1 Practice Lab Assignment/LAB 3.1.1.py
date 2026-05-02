import numpy as np

# write your code here...
rows, cols = map(int,input().split())
elements=[]
for _ in range(rows):
	elements.extend(map(int,input().split()))

array=np.array(elements)
array=array.reshape(rows,cols)
print(array)
print(array.ndim)
print(array.shape)
print(array.size)