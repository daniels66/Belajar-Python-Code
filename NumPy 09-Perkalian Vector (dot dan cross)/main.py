# perkalian vector dot dan cross produk
# untuk pembelajaran materi inilebih lanjut silahkan pelajari aljabar linear

import numpy as np

a = np.array([1, 3])
b = np.array([3, 0])

# perkalian dot produk
c = np.dot(a, b)
print(c)

# perkalian cross produk
d = np.array([1, 2, 0])
e = np.array([2, 1, 0])

f = np.cross(d, e)
print(f)
f = np.cross(e, f)
print(f)
