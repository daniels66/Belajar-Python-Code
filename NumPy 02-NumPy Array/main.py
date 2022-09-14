# array pada package numpy
import numpy as np

# membuat  vector
a = np.array([1, 2, 3, 4])
b = np.array(
    [1, 2.5, 3, 4.5]
)  # akan membuat semua menjadi float tetapi tidak tampil angka 0

# membuat vector dengan range
c = np.arange(1, 11, 2)  # dari nilai 1 sampai 10 dengan jarak 2 angka

# membuat multidimensi array
d = np.array([(1, 2, 3), (4, 5, 6)])  # akan membuat matrik 3 x 3

# membuat matrix dengan nilai zeros
e = np.zeros((3, 3))  # akan membuat matrix 3 x 3 dengan semua nilai 0

# membuat matrix dengan nilai zeros
f = np.ones((3, 3))  # akan membuat matrix 3 x 3 dengan semua nilai 1

# membuat matrix identitas
g = np.identity((3))  # akan membuat matrix identitas 3 x 3

# tampilkan data
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
