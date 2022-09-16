"""
ufunc atau universal funtion adalah sebuah fungsi NumPy yang beroperasi pada objek ndarray.
ufunc digunakan untuk mengimplementasikan vektorisasi di NumPy dengan jauh lebih cepat 
daripada iterasi setiap elemen.
vektorisasi adalah mengubah pernyataan iteratif menjadi operasi berbasis vektor.
"""

# sebelum adanya universal function untuk menjumlahkan setiap array menggunakan cara dibawah
print("sebelum ada ufunc".center(20, "-"))
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
    z.append(i + j)
print(z)

print("setelah ada ufunc".center(20, "-"))
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([4, 5, 6, 7])
z = np.add(x, y)
print(z)
