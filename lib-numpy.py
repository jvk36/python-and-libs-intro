import numpy as np

# 1. Creating arrays
print("1. Creating arrays:")
a = np.array([1, 2, 3, 4, 5])
print("1D array: np.array([1, 2, 3, 4, 5]): ", a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array: np.array([[1, 2, 3], [4, 5, 6]]): \n", b)

c = np.zeros((3, 3))
print("3x3 zero matrix: np.zeros((3, 3)): \n", c)

d = np.ones((2, 2))
print("2x2 ones matrix: np.ones((2, 2)): \n", d)

e = np.arange(0, 10, 2)
print("Array with step size: np.arange(0, 10, 2): ", e)

x = np.linspace(0, 100, num=9)
print("9 evenly spaced numbers between 0 and 100: x = np.linspace(0, 100, num=9): \n", x)

# 2. Array operations
print("\n2. Array operations:")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("x = np.array([1, 2, 3])")
print("y = np.array([4, 5, 6])")
print("x + y =", x + y)
print("x * y =", x * y)
print("x ** 2 =", x ** 2)

# 2a. N-Dimensional Array Operations
print("\n2a. N-Dimensional Array operations:")
mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])
print(f"mystery_array: {mystery_array}")
print(f'mystery_array.ndim: {mystery_array.ndim}')
print(f'myster_array.shape: {mystery_array.shape}')
# Axis 0: 3rd element. Axis 1: 2nd Element. Axis 3: 4th Element
print("Axis 0: 3rd element. Axis 1: 2nd Element. Axis 3: 4th Element")
print(f"mystery_array[2, 1, 3]: {mystery_array[2, 1, 3]}")
print("Get all elements on the 3rd axis that are at position 2 on the first axis and position 1 on the second axis.")
print(f"myster_array[2, 1, :]: {mystery_array[2, 1, :]}")
print("Get all first elements from axis number 3:")
print(f"myster_array[:, :, 0]: {mystery_array[2, 1, :]}")
print("NOTE: You can use : operator just as with python lists")


# 3. Broadcasting
print("\n3. Broadcasting:")
a = np.array([1, 2, 3])
b = 2
print("a = np.array([1, 2, 3])")
print("b = 2")
print("a * b =", a * b)

# 4. Indexing and slicing
print("\n4. Indexing and slicing:")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:\n", arr)
print("arr[1, 1] =", arr[1, 1])
print("arr[:, 1] =", arr[:, 1])
print("arr[1:3, 1:3] =\n", arr[1:3, 1:3])

# 5. Reshaping arrays
print("\n5. Reshaping arrays:")
a = np.arange(12)
print("Original array: a = np.arange(12): ", a)
b = a.reshape((3, 4))
print("Reshaped to 3x4: b = a.reshape((3, 4)): \n", b)
print(f"Shape of Reshaped array b: {b.shape}")
print(f"# of dimensions in the reshaped array, b: {b.ndim}")

# 6. Statistical operations
print("\n6. Statistical operations:")
arr = np.array([1, 2, 3, 4, 5])
print("Array: arr = np.array([1, 2, 3, 4, 5]): ", arr)
print("Mean: np.mean(arr)): ", np.mean(arr))
print("Median: np.median(arr)): ", np.median(arr))
print("Standard deviation: np.std(arr)): ", np.std(arr))

# 7. Linear algebra
print("\n7. Linear algebra:")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix multiplication A @ B:\n", A @ B)
print("Determinant of A: np.linalg.det(A)): ", np.linalg.det(A))
print("Inverse of A: np.linalg.inv(A)): \n", np.linalg.inv(A))

# 8. Random number generation
print("\n8. Random number generation:")
print("5 Random integers 1-10: np.random.randint(1, 11, 5)): ", np.random.randint(1, 11, 5))
print("Random floats 0-1: np.random.random(5)): ", np.random.random(5))
print("Random 3-dimensional array: np.random((3, 3, 3)): ", np.random.random((3, 3, 3)))

# 9. Logical Operations
print("\n9. Logical Operations:")
array1 = np.array([[True, False, True], [False, True, False]])
array2 = np.array([[True, True, False], [False, False, True]])
print(f"array1: {array1}")
print(f"array2: {array2}")

# Compare the two arrays element-wise
compared_array = array1 == array2
print(f"compared_array = array1 == array2: {compared_array}")

# Find the elements where the two arrays are not equal
not_equal_elements = ~compared_array
print(f"not_equal_elements = ~compared_array: {not_equal_elements}")

# 10. Vectorization
print("\n10. Vectorization:")
# Vectorize the addition operation
vfunc = np.vectorize(lambda x, y: x + y)
print("vfunc = np.vectorize(lambda x: x + 1)")
print(f"vfunc([1, 2, 3, 4, 5], [1, 2]): {vfunc([1, 2, 3, 4, 5], [1])}")
print('''
NOTE: vectorized function takes a nested sequence of objects or numpy arrays 
      as inputs and returns a single numpy array or a tuple of numpy arrays. 
      The vectorized function evaluates pyfunc over successive tuples of the 
      input arrays like the python map function, except it uses the 
      broadcasting rules of numpy.
''')

# 11. Fourier Analysis
print("\n11. Fourier Analysis:")
# Create a 1D array of 100 evenly spaced numbers
time_domain_signal = np.linspace(0, 1, 100)
print(f"time_domain_signal = np.linspace(0, 1, 100): {time_domain_signal}")
# Calculate the Fourier transform of the signal
fourier_transform = np.fft.fft(time_domain_signal)
print(f"fourier_transform = np.fft.fft(time_domain_signal): {fourier_transform}")

