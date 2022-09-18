# distribusi data array
import numpy as np
from numpy import random

print("distribusi data".center(20, "-"))
a = np.array([1, 2, 3, 4, 5])
b = random.choice(a, p=[0.2, 0.15, 0.45, 0, 0.2], size=(10))
"""
membuat array 1D dengan 10 buah nilai dengan nilai ditentukan dari array a,
dengan kemungkinan muncul masing masing nilai berada pada <p> (probability),
total nilai p harus 1
nilai 4 tidak akan pernah muncul dikarenan probability nya bernilai 0
"""
print("data a = ", a)
print("data b =", b)

b = random.choice(a, p=[0.1, 0.3, 0.45, 0.1, 0.05], size=(3, 5))
"""
membuat 2D array dengan 3 kolom dan 5 baris dengan nilai ditentukan dari array a,
dengan kemungkinan muncul masing masing nilai berada pada <p> (probability)
"""
print("data b =\n", b)
