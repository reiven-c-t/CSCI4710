a = [1, 2, 3, 4]
square = lambda x: x ** 2
a_2 = [square(x) for x in a]

# Q1&Q2
add = lambda x, y: x + y
add(1, 2)

# Question 3
import re

test = "Joke: what do you call a pig with three eyes? piiig!"
test_re = re.sub(r'pig', r'piiig', test)
print(test_re)

# Question 4
import numpy as np

print(np.eye(3, 3))

# Question 5
a = np.ones((2, 3), dtype=int)
np.random.seed(1)  # set seed to always generate same answer
b = np.random.random((2, 3))
print(a * 2 + b)

# Question 6
np.random.seed(1)  # set seed to always generate same answer
q6 = np.random.rand(3, 4)  # omit init array procedure, cuz rand() could do it at the same time
print(np.mean(q6))

# Question 7
a = np.arange(12).reshape(3, 4)
print(a)
# Q 7-1
print(np.sum(a, axis=0))
# Q 7-2
print(np.min(a, axis=1))
# Q 7-3
print(np.cumsum(a, axis=1))
# Q 7-4
print(a[2, 1])
# Q 7-5
print(a[-1, :])

# Question 8
a = np.arange(12).reshape(3, 4)
# Q 8-1
a_bool = a < 5
# Q 8-2
a_bool_filtered = a[a_bool]
# Q 8-3
print(a_bool_filtered)
# Q 8-4
print("the dimensions of the final matrix is", a_bool_filtered.ndim)

# Q 9
a = np.arange(12).reshape(3, 4)
print("Memory address of a: ", id(a))
import copy

a_copy = copy.deepcopy(a)
print("Memory address of a_copy: ", id(a_copy))
a_address_copy = a
print("a_address_copy,Referenced,(not copy) of a: ", id(a_address_copy))

# Question 10
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
# Q 10-1
print(x.transpose())
# Q 10-2
z = x.dot(y)
print(z)
# Q 10-3
print(np.linalg.inv(z))
# print(z.dot(np.linalg.inv(z))) # confirm to generate inverse


