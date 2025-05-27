import numpy as np

#ARRAYS
array_1d = np.array([1, 2, 3, 4, 5, 5])
print("One-dimensional array:", array_1d)

result_add=array_1d+10
print("Result:", result_add)

a=np.array([1,2,3,4,5,6])
b=np.array([1,2,3,4,5,6])
result_Sum=a+b
print("Result sum:", result_Sum)

result_Diff=a-b
print("Result difference:", result_Diff)

result_Prod=a*b
print("Result product:", result_Prod)



# MATRIX
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix:\n", matrix)

matrix_T = matrix.T
print("Transpose matrix:\n", matrix_T)

matrix_product = np.dot(matrix, matrix_T)
print("Matrix product:\n", matrix_product)



#Indexing,slices and filtering

element = array_1d[2]
print("Third element:", element)

slice_array = array_1d[1:4]
print("Array slice:", slice_array)

first_row = matrix[0,: ]
print("First row of matrix:", first_row)

second_column = matrix[:, 1]
print("Second column of the matrix:", second_column)

data = np.array([10, 15, 7, 22, 9, 18])
filtered_data = data[data > 10]
print("Numbers bigger than 10:", filtered_data)
