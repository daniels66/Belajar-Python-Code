# merubah urutan array menggunakan shuffle dan permutation
import numpy as np
from numpy import random

# shuffle
a = np.array([1, 2, 3, 4, 5, 6])
print("array a =\n", a)
random.shuffle(a)  # untuk shuffle tidak perlu dimasukkan kedalam variable
print("array a shuffle =\n", a)

# permutation
a = np.array([1, 2, 3, 4, 5, 6])
print("array a =\n", a)
b = random.permutation(a)  # untuk permutaion perlu dimasukkan ke dalam variable
print("array a permutation =\n", b)
