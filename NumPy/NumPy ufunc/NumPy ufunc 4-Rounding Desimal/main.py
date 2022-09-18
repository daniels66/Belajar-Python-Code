# operasi pembulatan angka desimal
"""
trunc()
floor()
ceil()
fix()
around()
"""
import numpy as np

a = np.array([-3.1666, 3.6667])
arr = np.trunc(a)  # menghilangkan nilai desimal dirubah menjadi float
print(f"trunc = {arr}")
arr = np.floor(a)  # dibulatkan ke bawah
print(f"floor = {arr}")
arr = np.ceil(a)  # dibulatkan ke atas
print(f"ceil = {arr}")
arr = np.fix(a)  # menghilangkan nilai desimal dirubah menjadi float
print(f"fix = {arr}")
arr = np.around(
    3.1444
)  # around(angka yang akan dibulatkan, berapa angka dibelakang koma yang ditampilkan)
print(f"around = {arr}")
arr = np.around(3.1444, 2)
print(f"around = {arr}")
arr = np.around(3.1444, 3)
print(f"around = {arr}")
arr = np.around(3.1666, 2)
print(f"around = {arr}")
arr = np.around(3.1666, 3)
print(f"around = {arr}")
"""
around = apabila angka lebih dari 5 akan dibulatkan ke atas,
apabila angka kurang dari 5 akan dibulatkan ke bawah
"""
