# sparse spark vector
# performance comparison of sparse data structures
import scipy.sparse
import numpy as np
import timeit

# loop five times
perf_numpy = np.zeros((5, 2))
perf_dict = np.zeros((5, 2))
perf_csrmult = np.zeros((5, 2))
perf_csrdot = np.zeros((5, 2))


# create a 50% sparse vector of random numbers
def mm_numpy(i):
    n = 100 * i
    x = (np.random.rand(n ** 2) * 2).astype(int).astype(float).reshape((n, n))
    np.dot(x, x)


def mm_dict(i):
    n = 100 * i
    x = (np.random.rand(n ** 2) * 2).astype(int).astype(float).reshape((n, n))
    x_csr = scipy.sparse.csr_matrix(x)
    x_dok = scipy.sparse.dok_matrix(x.reshape(x_csr.shape))
    x_dok * x_dok.T


def mm_csrmult(i):
    n = 100 * i
    x = (np.random.rand(n ** 2) * 2).astype(int).astype(float).reshape((n, n))
    x_csr = scipy.sparse.csr_matrix(x)
    x_csr.multiply(x_csr).sum()


def mm_csrdot(i):
    n = 100 * i
    x = (np.random.rand(n ** 2) * 2).astype(int).astype(float).reshape((n, n))
    x_csr = scipy.sparse.csr_matrix(x)
    x_csr * x_csr.T


# matrix multiplication: numpy
for i in range(1, 6):
    t = timeit.timeit("mm_numpy(i)", setup='import numpy as np; from __main__ import mm_numpy; i = (' + str(i) + ')',
                      number=50)
    perf_numpy[i - 1][0] = i
    perf_numpy[i - 1, 1] = t

# matrix multiplication: dictionary of keys
for i in range(1, 6):
    t = timeit.timeit('mm_dict(i)', setup='import numpy as np; from __main__ import mm_dict; i = (' + str(i) + ')',
                      number=50)
    perf_dict[i - 1][0] = i
    perf_dict[i - 1, 1] = t

# matrix multiplication: compressed sparse row multiply sum
for i in range(1, 6):
    t = timeit.timeit("mm_csrmult(i)",
                      setup='import numpy as np; from __main__ import mm_csrmult; i = (' + str(i) + ')', number=50)
    perf_csrmult[i - 1][0] = i
    perf_csrmult[i - 1, 1] = t

# matrix multiplication: compressed sparse row transpose
for i in range(1, 6):
    t = timeit.timeit("mm_csrdot(i)", setup='import numpy as np; from __main__ import mm_csrdot; i = (' + str(i) + ')',
                      number=50)
    perf_csrdot[i - 1][0] = i
    perf_csrdot[i - 1, 1] = t
