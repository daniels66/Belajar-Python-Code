# memanipulasi matrix
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)

# transpose matrik
print("transpose matrix".center(20, "-"))
print(a.transpose())
# print(np.transpose(a))
print(f"matrix ukuran = {a.shape}")

# flatten matrix (membuat matrik menjadi list)
print("flatten matrix".center(20, "-"))
print(a.ravel())
print(np.ravel(a))
print(f"matrix ukuran = {a.shape}")

# reshape matrix
print("reshape matrix".center(20, "-"))
print(a.reshape(6, 2))  # menjadi 6 kolom dan 2 baris
print(a.reshape(2, 6))  # menjadi 2 kolom dan 6 baris
print(f"matrix ukuran = {a.shape}")

# resize matrix
print("resize matrix".center(20, "-"))
a.resize(3, 4)  # mengubah matrix a menjadi kolom dan baris yang dinginkan
print(a)
print(f"matrix ukuran = {a.shape}")  # ukuran matrix berubah dari 4 kolom dan 3 baris
"""
dengan menggunakan resize matrix, matrix sebelumnya dirubah sepenuhnya 
mengikuti ukuran yang telah ditentukan
"""
