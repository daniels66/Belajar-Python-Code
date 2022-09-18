# inverse dan determinan dalam matrix
# untuk pembelajaran materi ini lebih lanjut silahkan pelajari aljabar linear

import numpy as np

a = np.array([[1, -1], [1, 1]])

print("matrix a = \n", a)

# inverse matrix
print("inverse matrix".center(20, "-"))
a_inv = np.linalg.inv(a)  # linalg = linear algebra (aljabar linear)
print("matrix inverse dari a = \n", a_inv)
print("pembuktian inverse = \n", np.dot(a, a_inv))

# determinan matrix
print("determinan matrix".center(20, "-"))
a_det = np.linalg.det(a)
print("determinan dari a adalah =\n", a_det)
a_det_inv = np.linalg.det(a_inv)
print("determinan dari a_inv adalah =\n", a_det_inv)
