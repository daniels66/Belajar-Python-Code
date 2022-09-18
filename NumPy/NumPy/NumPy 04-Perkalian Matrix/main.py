# perkalian matrix
import numpy as np

# matrix = (kolom x baris)
"""
untuk perkalian matrix dalam python menggunakan aturan yang sama
seperti perkalian matrix pada umumnya yaitu
jumlah kolom matrix 1 harus sama dengan jumlah baris pada matrix 2
"""

a = np.array([[1, 2, 3], [4, 5, 6]])
print("matrix a =")
print(a)
b = np.ones((3, 2))
print("matrix b =")
print(b)

# perkalian matrix cara 1
c = np.dot(a, b)
print("hasil matrix a*b =")
print(c)
d = np.dot(b, a)
print("hasil matrix b*a =")
print(d)
e = a.dot(b)  # objek b dimasukkan ke dalam fungsi dot yang menempel di objek a
print("hasil matrix a*b =")
print(e)
f = b.dot(a)  # objek a dimasukkan ke dalam fungsi dot yang menempel di objek b
print("hasil matrix b*a =")
print(f)
