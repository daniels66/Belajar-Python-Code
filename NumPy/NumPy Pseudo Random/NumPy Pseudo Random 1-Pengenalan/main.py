# pseudo random dan true random
"""
Jika terdapat program untuk membuat bilangan acak dapat diprediksi,
maka fungsi random tidak benar-benar acak.
Angka acak yang dihasilkan melalui algoritma generasi disebut pseudo random.
Untuk menghasilkan angka yang benar-benar acak didaptkan dari beberapa sumber luar, 
seperti penekanan tombol, gerakan mouse, data di jaringan, dll.
"""
import numpy as np
from numpy import random

print("pseudo random".center(20, "-"))
a = random.randint(100)  # membuat nilai int acak dari 0-100
print("nilai acak int (0-100) = ", a)
a = random.randint(
    100, size=(5)
)  # membuat array 1D dengan jumlah 5 buah angka int acak
print("array 1D dari random int =\n", a)
a = random.randint(100, size=(2, 3))  # membuat array 2D dengan 2 kolom dan 3 baris
print("array 2D dari random int =\n", a)
a = random.rand()  # membuat nilai float acak dari 0-1
print("nilai acak float (0-1) = ", a)
a = random.rand(5)  # membuat array 1D dengan jumlah 5 buah angka float acak
print("array 1D dari random float =\n", a)
a = random.rand(2, 3)  # membuat array 2D dengan 2 kolom dan 3 baris
print("array 2D dari random float =\n", a)
b = np.array([1, 3, 5, 7, 9])
c = random.choice(b)
print("array data b =\n", b)
print("nilai random dari data b = ", c)
c = random.choice(b, size=(2, 3))  # size digunakan untuk membuat array 2 kolom 3 baris
print("array 2D acak dari data b =\n", c)
