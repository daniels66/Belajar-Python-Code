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
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)
newarr = arr.reshape(2, 3, 2)  # 2 buah array, masing masing 3 kolom dan 2 baris
print(newarr)
print(f"matrix ukuran = {newarr.shape}")

# resize matrix
print("resize matrix".center(20, "-"))
a.resize(3, 4)  # mengubah matrix a menjadi kolom dan baris yang dinginkan
print(a)
print(f"matrix ukuran = {a.shape}")  # ukuran matrix berubah dari 4 kolom dan 3 baris
"""
dengan menggunakan resize matrix, matrix sebelumnya dirubah sepenuhnya 
mengikuti ukuran yang telah ditentukan
"""

# stacking matrix
print("stacking matrix".center(20, "-"))
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

c = np.hstack((a, b))  # taruh secara horizontal matrix b disebelah matrix a
print(c)  # matrix b berada di sebelah kanan matrix a
print(f"matrix ukuran = {c.shape}")  # ukuran akan berubah

d = np.vstack((a, b))  # taruh secara vertikal matrix b disebelah matrix a
print(d)  # matrix b berada di bawah matrik a
print(f"matrix ukuran = {d.shape}")  # ukuran akan berubah

d = np.dstack((a, b))  # taruh berdasarkan kedalaman (depth) matrix
print(d)  # akan memanjang mengikuti matrix a disebelah kanan berisi matrix b
print(f"matrix ukuran = {d.shape}")  # ukuran akan berubah

# split matrix
print("split matrix".center(20, "-"))
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(arr)
newarr = np.array_split(arr, 3)  # dari 1 buah array dibagi menjadi 3 buah array
print(newarr)
print(newarr[1])  # ambil nilai pada array kedua
print(newarr[1][1])  # dari array kedua ambil nilai pada baris ke dua
print(newarr[1][1][0])  # pada baris ke dua ambil nilai pada index 0
