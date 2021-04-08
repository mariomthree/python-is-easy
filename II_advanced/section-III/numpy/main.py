import numpy

# # view version
# print('version: ',numpy.__version__)

# # Creating arrays
# numbers = numpy.array([1,2,3,4,5,6])
# print(numbers)

# # view type
# print(type(numbers))

# # Use a tuple to create a NumPy array:
# numbers = numpy.array((1,2,3,4,5,6))
# print(numbers)

# dimensions in arrays
# A dimension in arrays is one level of array depth (nested arrays).

# # 0-D Arrays
# # 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
# numbers = numpy.array(42)
# print(numbers)


# # 1-D Arrays
# # An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# numbers = numpy.array([1,2,3,4,5,6])
# print(numbers)

# # 2-D Arrays
# # An array that has 1-D arrays as its elements is called a 2-D array.
# # These are often used to represent matrix or 2nd order tensors.
# numbers = numpy.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(numbers)

# # 3-D arrays
# # An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# # These are often used to represent a 3rd order tensor.
# numbers = numpy.array([
#   [
#     [1,2,3],
#     [4,5,6]
#   ],
#   [
#     [7,8,9],
#     [10,11,12],
#   ]
#])
# print(numbers.ndim)


# NumPy Array Indexing
# Access Array Elements

# numbers = numpy.array([1,2,3,4,5,6])
# print(numbers[0])


# numbers = numpy.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(numbers[1,0])

# numbers = numpy.array([
#   [
#     [1,2,3],
#     [4,5,6]
#   ],
#   [
#     [7,8,9],
#     [10,11,12],
#   ]
# ])
# print(numbers[1,0,1])


arr = numpy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)

# credits
# https://www.w3schools.com/python/numpy/default.asp