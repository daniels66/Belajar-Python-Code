# operasi aritmatika dalam ufunc
"""
add()
subtract()
multiplay()
divide()
power()
mod()
reminder()
divmod()
absolute()
"""
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print(f"add = {np.add(a,b)}")
print(f"subtract = {np.subtract(a,b)}")
print(f"multiply = {np.multiply(a,b)}")
print(f"divide = {np.divide(b,a)}")
print(f"power = {np.power(a,b)}")  # dipangkatkan
print(f"mod = {np.mod(b,a)}")  # sisa modulus
print(f"remainder = {np.remainder(b,a)}")  # sisa modulus
print(f"divmod = {np.divmod(b,a)}")
"""
akan menghasilkan 2 buah array, dengan array 1 menghasilkan hasil bagi modulus,
array 2 menghasilkan nilai sisa dari modulus
"""
a = np.array([-1, -2, 3, -4, 5])
b = np.array([6, 7, -8, -9, -10])
print(f"abs = {np.abs(a)}")  # hanya menerima 1 parameter
print(f"absolute = {np.absolute(b)}")  # hanya menerima 1 parameter
"""
lebih baik menggunakan fungsi absolute() agar tidak terjadi 
kebinggungan dari fungsi abs() di package math
absolute membuat nilai negatif menjadi positif
"""
