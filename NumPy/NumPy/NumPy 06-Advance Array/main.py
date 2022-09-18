# membuat array secara advance

import numpy as np

# merubah tipe data pada matrix sesuai yang diinginkan
print("ubah tipe data".center(30, "-"))
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
b = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
c = np.array([[1, 2, 3], [4, 5, 6]], dtype=bool)

print(a)
print(b)
print(c)

# membuat matrix dengan menggunakan fuction
print("buat matrix dengan fuction".center(30, "-"))


def kuadrat(kolom, baris):
    return kolom**2


"""
np.fromfunction(nama fungsi, (kolom,baris), (type matrix))
*ubah urutan kolom dan baris agar didapatkan hasil yang diinginkan
"""
d = np.fromfunction(kuadrat, (1, 5), dtype=int)
print(d)
d = np.fromfunction(kuadrat, (5, 1), dtype=int)
print(d)

print("buat matrix dengan iterasi".center(30, "-"))

e = (x * x for x in range(5))  # apabila for loop tidak panjang
f = np.fromiter(e, dtype=int)
print(f)
e = (x * 5 for x in range(5))
f = np.fromiter(e, dtype=int)
print(f)

print("multi type array".center(30, "-"))  # isi dalam array tidak terbatas angka
type = [
    ("nama", "S100"),
    ("tinggi_bdn", int),
]  # s100 adalah nilai string dengan nilai maximal 100 char
data = [("daniel", 168), ("bili", 164), ("alil", 160)]

print(data)
h = np.array(data, dtype=type)
print(h)
