"""
https://www.numpy.org/
https://stackabuse.com/numpy-tutorial-a-simple-example-based-guide/
"""
import numpy as np


print('\n\n\nCreate\n')
array1 = np.array((1, 2, 3, 4, 5, 6, 7))
array2D = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])  # create 2D array
array3D = np.array([
    [
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
    ],
    [
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
    ],
    [
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
    ],
])
ranged_array = np.arange(2, 9)  # create array using np.arange(start, stop, step, dataType)
ranged_array2 = np.arange(2, 10, 2)
zeros = np.zeros(5)  # create array of 5 zeros
zeros2D = np.zeros((5, 4))
array5D = np.zeros((2, 3, 4, 2, 3))
ones = np.ones(5)  # create array of 5 ones
ones2D = np.ones((5, 4))
linear_array = np.linspace(1, 10, 10)  # create array of linearly-spaced numbers that you want between the specified range
linear_array2 = np.linspace(1, 10, 20)
identity_matrix = np.eye(4)  # create an identity matrix
uniform_distribution = np.random.rand(2, 3)  # create 2d array with random numbers between 0-1 (uniform distribution)
normal_distribution = np.random.rand(2, 3)  # create 2d array with random numbers between 0-1 (Gaussian distribution)
random = np.random.randint(50, 100, 5)  # create an array of 5 random integers between 50 and 100
print('array2D', array2D)
print('array3D', array3D)
print('ranged_array', ranged_array)
print('ranged_array2', ranged_array2)
print('zeros', zeros)
print('zeros2D', zeros2D)
print('array5D', array5D)
print('ones', ones)
print('ones2D', ones2D)
print('linear_array', linear_array)
print('linear_array2', linear_array2)
print('identity_matrix', identity_matrix)
print('uniform_distribution', uniform_distribution)
print('normal_distribution', normal_distribution)
print('random', random)


print('\n\n\nSimple Math\n')
array2 = array1 + 1  # increment all points by 1
array3 = array1 * 2  # multiply all points by 2
array4 = np.array((-1, -2, -3, -4, -5, -6, -7))
array5 = array1 + array2  # join points of arrays
print('array1 type', type(array1))
print('array2', array2)
print('array3', array3)
print('array5', array5)


print('\n\n\nReshape\n')
array1D = np.arange(1, 11)
array2D = array1D.reshape(5, 2)
print('array1D', array1D)
print('array2D', array2D)


print('\n\n\nFind Min/Max Values\n')
random5 = np.random.randint(1, 100, 5)
random5_min = random.min()
random5_max = random.max()
random5_min_index = random.argmin()
random5_max_index = random.argmax()
print('random5', random5)
print('minimum value & index: ', random5_min, random5_min_index)
print('maximum value & index: ', random5_max, random5_max_index)


print('\n\n\nIndexing\n')
sliced_array = random5[1:3]
print('array1[0]', array1[0])
print('random5[4]', random5[4])
print('random5[-1]', random5[-1])
print('random5[1:3]', random5[1:3])
print('sliced_array = random5[1:3]', sliced_array)
print('array2D[1]', array2D[1])
print('array2D[1, 0]', array2D[1, 0])
print('array2D[0, 2]', array2D[1, 0])
print('retrieve the first column: array2D[:, 0]', array2D[:, 0])
print('retrieve the second column: array2D[:, 1]', array2D[:, 0])
print('retrieve the elements from the first two rows and first two columns: array2D[:2, :2]', array2D[:2, :2])


print('\n\n\nArithmetic Operations\n')
array2pw4 = np.arange(1, 16)
array2pw4x2 = array2pw4 + array2pw4
logn = np.lib.scimath.logn
print('array2pw4 = np.arange(1, 16)', array2pw4)
print('array2pw4x2 = array2pw4 + array2pw4', array2pw4 + array2pw4)
print('add scalar: array2pw4 + 10', array2pw4 + 10)
print('sub scalar: array2pw4 - 10', array2pw4 - 10)
print('div scalar: array2pw4 / 5', array2pw4 / 5)
print('mlt scalar: array2pw4 * 5', array2pw4 * 5)
print('np.ln(a)=np.log(a) -> np.log(array2pw4)', np.log(array2pw4))
print('np.log10(array2pw4)', np.log10(array2pw4))
print('np.log2(array2pw4)', np.log2(array2pw4))
print('np.log10(array2pw4)', np.log10(array2pw4))
print('logn(100, array2pw4)', logn(100, array2pw4))
print('np.log(array2pw4)/np.log(100)', np.log(array2pw4)/np.log(100))
print('np.exp(array2pw4)', np.exp(array2pw4))
print('np.sqrt(array2pw4)', np.sqrt(array2pw4))
print('np.square(array2pw4)', np.square(array2pw4))
print('np.sin(array2pw4)', np.sin(array2pw4))
print('np.sinh(array2pw4)', np.sinh(array2pw4))
print('np.sinh(array2pw4)', np.arcsin(array2pw4))
print('np.cos(array2pw4)', np.cos(array2pw4))
print('np.cos(array2pw4)', np.tan(array2pw4))


print('\n\n\nLinear Algebra Operations\n')
x = np.array([2, 4])
y = np.array([1, 3])
# The dot product of the above two vectors is (2 x 1) + (4 x 3) = 14

# without numpy
dot_product = 0
for a, b in zip(x, y):
    dot_product += a * b
print(dot_product)

# with numpy
print((x * y).sum())
print(x.dot(y))

# Matrix Multiplication
X = np.array(([1, 2, 3], [4, 5, 6]))
Y = np.array(([1, 2], [4, 5], [7, 8]))
Z = np.dot(X, Y)
print(Z)
# also if the dimensions of the two matrices match
Z = np.multiply(X, X)
print(Z)

# Finding the Inverse of a Matrix
Y = np.array(([1, 2], [3, 4]))
Z = np.linalg.inv(Y)
print(Z)

# in order to verify if the inverse has been calculated correctly,
# we can take the dot product of a matrix with its inverse,
# which should yield an identity matrix
W = Y.dot(Z)
# the result as expected, Ones in the diagonal and zeros (or very close to zero) elsewhere
print(W)

# Finding the Determinant of a Matrix
X = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
Z = np.linalg.det(X)
print(Z)  # output should be "6.66133814775094e-16"

# Finding the Trace of a Matrix
X = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# The trace of a matrix is the sum of all the elements in the diagonal of a matrix
Z = np.trace(X)
print(Z)  # output should be "15" since the sum of the diagonal elements of the matrix X is 1 + 5 + 9 = 15
