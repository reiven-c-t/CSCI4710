# from https://scipy.github.io/old-wiki/pages/Additional_Documentation/New_SciPy_Tutorial.html
from scipy import sparse
import scipy.sparse.linalg.dsolve as linsolve
from numpy import random, linalg

# Construct a 1000x1000 lil_matrix
A = sparse.lil_matrix((1000, 1000))
A[0, :100] = random.rand(100)
A[1, 100:200] = A[0, :100]
A.setdiag(random.rand(1000))

b = random.rand(1000)

A = A.tocsr()  # TODO: it already fulfill question.
# .T computes the transpose of A (shortcut for A.transpose)
x = linsolve.spsolve(A * A.T, b)
print(x[0:9])
